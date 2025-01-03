# Notebook pub template

This repo is a template for notebook publications. The publication rendered and hosted by this repository serves as a demo that can be viewed at [this URL](https://arcadia-science.github.io/notebook-pub-template/).

## How to use this template

1. Create a repo from this template

    In the top-right of this GitHub repo, select the green button that says "*Use this template*".

    > [!IMPORTANT]  
    > When creating your repo from this template, you need to **check the box** that says, "*Include all branches*"

1. Config edits 

    * Replace the variables in `_variables.yml`

1. Setup the code environment

    Setup the codebase and compute environment by following the relevant steps in [SETUP.qmd](SETUP.qmd).

    Afterwards, create a branch to work on (don't commit to `main` directly).

1. Create your pub

    Edit `index.ipynb` to create your pub. As you work, render it in a live preview with `make preview`.

    If you already have a notebook written that you're trying to transform into a pub, replace the template `index.ipynb` with your own, but be sure to add the YAML front matter (the first cell of `index.ipynb`) to your notebook.

    Fill in the authorship section appropriately.

## How to publish

Publishing is handled automatically with a GitHub Action that triggers whenever a pull request is merged into `main`. Thus, all the following action items should be completed before your pull request is approved and subsequently merged.

1. Enable read/write permissions for GitHub Actions

    In your repo, go to *Settings* -> *Actions* -> *General* -> *Workflow permissions*, and check the box, "*Read and write permissions*"

1. Populate the `README_TEMPLATE.md`

    Populate `README_TEMPLATE.md` and then rename it to `README.md`.

    > [!NOTE]  
    > The content you're reading now is the current `README.md`, which is to be replaced with `README_TEMPLATE.md`.

1. Remove placeholder package

    If you did not populate `src/analysis` with your own content, remove it (`rm -rf src/analysis`).

1. Remove placeholder version

    Remove `index_v00.ipynb`.

1. Make the repository public

    In order for this pub to be open and reproducible, make the [repo public](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility).

1. Enable comments

    Comments are handled with [Giscus](https://giscus.app/), which Quarto has an integration for. Once enabled, a widget is placed at the bottom of the publication that provides an interface to read, write, react, and respond to [GitHub Discussions](https://docs.github.com/en/discussions) comments. Comments made through the interface are automatically added as comments to a GitHub Discussions thread of your repository.

    First, [enable GitHub Discussions](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/enabling-features-for-your-repository/enabling-or-disabling-github-discussions-for-a-repository) for your repo.

    Second, [install the Giscus App](https://github.com/apps/giscus) for your repository. Click *Configure*, select *Arcadia-Science*, then select your repository from the dropdown. Click *Update access*.

    > [!IMPORTANT]  
    > Do not deselect any of the other Arcadia-Science repositories that already have the Giscus app installed, *e.g.* `Arcadia-Science/notebook-pub-template`.

    Now, edit the comments section in `_quarto.yml` with your repo name:

    ```yaml
    comments:
      giscus:
        repo: Arcadia-Science/notebook-pub-template
        input-position: top
    ```

    You may have to wait a few minutes for `make preview` to properly render the Giscus widget.

1. Final checks

    Complete the steps in the section, "*Final checks*" in [CONTRIBUTING.qmd](CONTRIBUTING.qmd).

## Publishing revisions

See [CONTRIBUTING.qmd](CONTRIBUTING.qmd).
