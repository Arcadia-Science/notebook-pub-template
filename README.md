# Notebook pub template

WIP

## Getting Started

### Create a repo from this template

In the top-right of this GitHub repo, select the green button that says "*Use this template*".

> [!IMPORTANT]  
> When creating your repo from this template, you need to **check the box**, "*Include all branches*"

After cloning your repo, create a branch to work on (don't commit to `main` directly).

### Edit `_variables.yml`

Replace the values in `_variables.yml`.

### Create your pub

Edit `index.ipynb` to create your pub. As you work, render it in a live preview with `make preview`.

## How to publish

When you're happy with the content, address the following action items.

The publication is auto-published using a GitHub Action that requires read/write permissions. The action


> [!IMPORTANT]  
> This should be done before 


### Enable read/write permissions for GitHub Actions

In your repo, go to *Settings* -> *Actions* -> *General* -> *Workflow permissions*, and check the box, "*Read and write permissions*"

### Populate the `README_TEMPLATE.md`

Populate `README_TEMPLATE.md` and then rename it to `README.md`.

> [!NOTE]  
> The content you're reading now is the current `README.md`, which is to be replaced with `README_TEMPLATE.md`.

### Make the repository public

The pub is hosted using [GitHub Pages](https://pages.github.com/), which requires the repo is made public.

### Enable comments

Comments are handled with Giscus.

Fill out the instructions here: https://giscus.app/

Edit the comments section in `_quarto.yml` with your repo name:

```yaml
comments:
  giscus:
    repo: Arcadia-Science/notebook-pub-template
    input-position: top
```

### Final run through

```bash
make execute
```

Commit and push all changes made.

```bash
make preview
```

### Final

Merge your pull request. The pub will be made public at <URL>

## Publishing revisions

See [CONTRIBUTING.md](CONTRIBUTING.md).
