# Template Architecture

## TL;DR for Users

If you're **using this template** to create a publication:

- **Only edit these files**:
  - `index.ipynb` - Your main publication content
  - `_variables.yml` - Publication metadata (title, author, etc.)
  - `authors.yml` - Author information and roles
  - `src/` - Custom Python code for your publication
  - `env.yml` - Dependencies for your publication

- **Leave these files alone**:
  - `_extensions/` - Quarto extensions (including the theme)
  - `_freeze/` - Generated execution results
  - `_site/` - Generated website files

That's it! Focus on creating great content in your notebook and let the template handle the rest.

## File Structure Overview

```
notebook-pub-template/
├── index.ipynb        # Your main publication content
├── _variables.yml     # Publication metadata
├── authors.yml        # Author information
├── src/               # Custom Python code
├── env.yml            # Conda environment definition
├── _quarto.yml        # Quarto configuration (rarely edit)
├── _freeze/           # Generated output (don't edit)
├── _extensions/       # Quarto extensions (don't edit)
├── _site/             # Generated website (don't edit)
└── pyproject.toml     # Python configuration (rarely edit)
```

### Content Files

- **`index.ipynb`**: The primary file containing publication content. This Jupyter notebook contains both narrative text (in markdown cells) and executable code (in code cells).

- **`src/`**: Directory for Python modules that contain user code to be imported into your notebook. This helps keep the notebook clean by moving complex functionality into separate files.

### Configuration Files

- **`_variables.yml`**: Contains publication metadata like title, repository information, and Google Analytics ID. This should be customized for the publication.

- **`authors.yml`**: Contains author information and contributor roles. The publishing team will help finalize this file near the end of the publication cycle.

- **`env.yml`**: Defines the Conda environment for the publication.

### Extensions

The `_extensions/` directory contains Quarto extensions. Quarto's extension system works through vendoring. When you run `quarto add`, it downloads the extension and copies it into your project's `_extensions/` directory. There is no global installation; each project contains its own copy of its extensions checked into the repository. This means when you clone a pub from this template repo, it already has all the extensions it needs.

**The contents in `_extensions/` should not be edited directly**. Most important is **`Arcadia-Science/arcadia-pub-theme/`**, our publication theme. It provides all CSS styling, interactive components (sticky header, author reveal, citation modal), and assets like the citation style file. This extension is maintained in the [notebook-pub-theme](https://github.com/Arcadia-Science/notebook-pub-theme) repository.

To update the Arcadia theme, see [notebook-pub-theme](https://github.com/Arcadia-Science/notebook-pub-theme) for detailed instructions.

To update/add any of the other extensions, use [`quarto add`](https://quarto.org/docs/extensions/managing.html).

### Generated Files

These files are generated and should not be edited directly.

- **`_freeze/`**: Contains cached execution results from the notebook. This should be committed to the repository.

- **`_site/`**: Contains the generated static website. This should never be committed to the repository.

### Template Configuration

- **`_quarto.yml`**: Controls the rendering process and website structure. Only edit when specifically instructed.

## How It All Works Together

1. **Content Creation**: Authors edit `index.ipynb` with their analysis and narrative
2. **Rendering**: Quarto converts notebooks to HTML using configurations in `_quarto.yml`
3. **Styling**: The arcadia-pub-theme extension provides CSS, interactive components, and brand assets
4. **Output**: Final website is built in `_site/` and execution cache in `_freeze/`
5. **Publishing**: GitHub Actions automate the publication process when merged to the `publish` branch

## Theme/Styling

Any style changes should be made in the [`notebook-pub-theme`](https://github.com/Arcadia-Science/notebook-pub-theme) repo and added into this repo using Quarto's extension management system (see *Extensions* above). This separation allows styling improvements to be made in the extension and then propagated to all pub repos.

## Setup/Publishing

For more information on how to create and publish content using this template, see:

- [Environment Setup Guide](ENVIRONMENT_SETUP.md)
- [Publishing Guide](PUBLISHING_GUIDE.md)
