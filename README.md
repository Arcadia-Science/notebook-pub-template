# If using as template

* Your repo must be public
* Go to settings -> actions -> workflow permissions, and check read and write permissions

Primary source is here: https://quarto.org/docs/publishing/github-pages.html#overview

This publishes uses gh-pages, but execution is done locally, not on CI. That means all computation is run locally. To do this, run `make pub` (`quarto render --execute`). The computational outputs are stored in `_freeze` directory and the results should be committed, since the CI will use these results to render the webpage.

In order to publish the website, you have to do the following *once*. Have a clean branch, then run `quarto publish gh-pages`.

Now, whenever you push to main, a github action should rebuild the website.

# Giscus

Fill out the instructions here: https://giscus.app/
