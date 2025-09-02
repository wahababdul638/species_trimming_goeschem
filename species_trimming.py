#!/usr/bin/env python3
import yaml
import xarray as xr
import os
import sys

def main():
    # Input: current directory
    input_dir = "./"
    # Output: parent directory with _TT suffix
    cwd = os.path.basename(os.getcwd())
    output_dir = os.path.join("..", f"{cwd}_TT")

    yaml_file = "species_data_base_trimmed.yml"

    # Load species list from YAML
    try:
        with open(yaml_file, "r") as f:
            species_config = yaml.safe_load(f)
        species = species_config["species"]
        variables = [f"SpeciesConcVV_{sp}" for sp in species]
    except Exception as e:
        print(f"Failed to load species list from {yaml_file}: {e}")
        sys.exit(1)

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Loop through NetCDF files
    for filename in os.listdir(input_dir):
        if filename.startswith("GEOSChem.SpeciesConc.") and filename.endswith(".nc4"):
            input_file = os.path.join(input_dir, filename)
            output_file = os.path.join(output_dir, f"trimmed_{filename}")

            print(f"Processing {filename} ...")
            try:
                dsSpCon = xr.open_dataset(input_file)
                # Subset variables based on species list
                drf = dsSpCon[variables]
                drf.to_netcdf(output_file)
                dsSpCon.close()
                print(f"✅ Saved trimmed file to {output_file}")
            except Exception as e:
                print(f"❌ Error processing {filename}: {e}")

if __name__ == "__main__":
    main()
