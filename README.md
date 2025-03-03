# Notebook Publication Template

This repo is a template for Jupyter notebook publications. The template produces a publication rendered and hosted by Quarto, which can be viewed at [this demo URL](https://arcadia-science.github.io/notebook-pub-template/).

## Template Documentation

- [Environment Setup Guide](developer-docs/ENVIRONMENT_SETUP.md) - How to set up your development environment
- [Publishing Guide](developer-docs/PUBLISHING_GUIDE.md) - How to publish your notebook publication
- [Template Architecture](developer-docs/TEMPLATE_ARCHITECTURE.md) - Understanding the template's structure
- [CONTRIBUTING.qmd](CONTRIBUTING.qmd) - How to publish revisions

## Quick Start

1. **Create a repo from this template**

    In the top-right of this GitHub repo, select the green button that says "*Use this template*".

    **IMPORTANT**: When creating your repo from this template, **check the box** that says, "*Include all branches*". This is required because the hosted publication is managed on a separate branch.

2. **Configure your publication**

    * Replace the variables in `_variables.yml`
      - For `google_analytics`, contact the Publishing Team with your repo name to receive a tracking ID
    * Feel free to edit the variables in `authors.yml`
      - Ultimately, Publishing Team will provide you with an `authors.yml` based on the contributor roles they assign for the publication.

3. **Install Quarto**

    The publication is rendered with [Quarto](https://quarto.org/). If you don't have it installed (check with `quarto --version`), you can [install it here](https://quarto.org/docs/get-started/).

4. **Set up your environment**

    See the [Environment Setup Guide](developer-docs/ENVIRONMENT_SETUP.md) for complete instructions.

5. **Register your publication**

    If you intend to publish your analysis, fill out the "*Kick off a new pub*" form on the AirTable [Publishing toolkit](https://www.notion.so/arcadiascience/Publishing-2-0-f0c51bf29d1d4356a86e6cf8a72ae88b?pvs=4#e1de83e8dd2a4081904064347779ed25).

6. **Create your publication**

    Edit `index.ipynb` to create your publication. As you work, render a live preview with:

    ```bash
    make preview
    ```

7. **Publishing**

    See the [Publishing Guide](developer-docs/PUBLISHING_GUIDE.md) for complete instructions on the publishing process.
