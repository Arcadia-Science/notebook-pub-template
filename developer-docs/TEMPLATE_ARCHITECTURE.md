# Template Architecture

This document describes the architecture of the notebook publication template, explaining which files are custom, vendored, or generated automatically.

## Directory Structure Overview

```
notebook-pub-template/
├── _extensions/        # Quarto extensions (vendored)
├── _freeze/           # Generated output files (do not edit directly)
├── _site/             # Generated site (do not edit directly)
├── assets/            # Custom assets for publication styling
├── src/               # Custom Python code for the publication
├── _quarto.yml        # Main Quarto configuration file
├── _variables.yml     # Publication variables
├── authors.yml        # Author information
├── *.ipynb            # Jupyter notebook content files
└── various config files (pyproject.toml, env.yml, etc.)
```

## Key Components

### Custom Files (Safe to Edit)

- **Content Files**:
  - `index.ipynb`: Main publication content
  - `demo.ipynb`: Example/demo content
  - Any other `.ipynb` files you create

- **Configuration**:
  - `_quarto.yml`: Main Quarto configuration
  - `_variables.yml`: Publication variables
  - `authors.yml`: Author information
  - `pyproject.toml`: Python project configuration including ruff settings
  - `env.yml`: Conda environment specification

- **Custom Code**:
  - `src/` directory: Contains custom Python code for the publication

- **Custom Assets**:
  - `assets/`: Contains stylesheets, logos, and other publication assets
  - `assets/css/`: CSS styling for the publication

### Vendored Files (Do Not Edit)

- **Extensions**:
  - `_extensions/`: Directory containing Quarto extensions
    - `mcanouil/iconify/`: IconIfy extension
    - `pandoc-ext/abstract-section/`: Abstract section extension
    - `quarto-ext/fontawesome/`: FontAwesome extension

- **Other Vendored Assets**:
  - `assets/arcadia.csl`: Citation style file

### Generated Files (Do Not Edit Directly)

- **Build Artifacts**:
  - `_freeze/`: Contains cached execution results
  - `_site/`: Contains the generated static site

## Publication Flow

1. Content is authored in Jupyter notebooks (primarily `index.ipynb`)
2. Quarto uses the configuration in `_quarto.yml` to render the notebooks
3. The rendered content uses styles from `assets/css/` and extensions from `_extensions/`
4. Generated output is stored in `_freeze/` and `_site/`
5. GitHub Actions automate the publishing process

## Quarto Configuration

The `_quarto.yml` file is the central configuration file that controls:
- Website structure and navigation
- Page layout and styling
- Rendering options
- Extensions configuration

## Customization Points

When modifying the template, focus on:
1. Content in `.ipynb` files
2. Custom styling in `assets/css/`
3. Configuration in `_quarto.yml` and `_variables.yml`
4. Custom code in `src/`

Avoid modifying:
1. Files in `_extensions/`
2. Files in `_freeze/` and `_site/`
