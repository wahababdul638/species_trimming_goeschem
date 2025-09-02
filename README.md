# GEOS-Chem Species Trimmer

This repository contains a Python script to **trim GEOS-Chem species NetCDF files** based on a user-defined list of species. It is designed for managing large GEOS-Chem outputs efficiently by creating smaller, focused NetCDF files.

## Features

- Reads a list of species from a YAML file (`species_data_base_trimmed.yml`).
- Processes all `GEOSChem.SpeciesConc.*.nc4` files in the working directory.
- Saves trimmed NetCDF files in an output folder automatically named after the working directory with `_TT` appended.
- Lightweight and easy to run with Python 3.

## Requirements

- Python 3.8+
- `xarray`
- `PyYAML`
- `netCDF4` (optional, for some backends)
- `os` and `sys` (standard library)

Install dependencies via pip:

```bash
pip install xarray pyyaml netCDF4
