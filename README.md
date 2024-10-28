<img src="https://github.com/datasciencecampus/awesome-campus/blob/master/ons_dsc_logo.png">

<img src="https://img.shields.io/badge/repo%20purpose-demonstration%20only%20(all contents)-red" alt="All contents of this repository is for demonstration purposes only."/>

# `r5py-example`

A repository demonstrating how to use the [`r5py`] python package for travel
time estimation. It is intended for **demonstration and educational purposes only**
and should not be used for any other purpose.

## Overview

The aim of this example explores travel time estimation, by different modalities,
to a subset of supermarkets across the Newport, Wales area.

The example uses `r5py` to calculate travel times from a set of origins (Output
Area Population weight centroids) to a set of destinations (supermarkets). The
example demonstrates how to use the `r5py` package to calculate travel times
using different modes of transport (public transit, walking, cycling, driving)
and how to visualise the results.

The `data/` directory contains the input data required to run this example. It
is a small, limited subset of the publicly available data covering only the
example area of interest. For more information on these data, please see the
[data/README.md](data/README.md).


## Installation

To run this example, you will need to:

1. Have Java installed on your system (required by `r5py`, see the
[r5py Java installation] documentation).
2. Install the required packages. You can do this by running the commands
below (uses `venv` and `pip` to create a virtual environment and install the
required packages).:

> **Note:** It is also possible to use `conda` to create the virtual
> environment and install the packages. In this case, use `conda` to install
> `r5py` v0.1.0 before installing the `requirements.txt,` since this will
> install a suitable OpenJDK version into the conda environment too.

Clone the repository:

```bash
git clone https://github.com/datasciencecampus/r5py-example.git
```

Create the virtual environment:
```bash
python3 -m venv .venv
```

Activate the virtual environment:
```bash
source .venv/bin/activate
```

> **Note:** On Windows, you should use `.\.venv\Scripts\activate` to activate
> the virtual environment.

Upgrade `pip`:
```bash
pip install --upgrade pip
```

Install the required packages:
```bash
pip install -r requirements.txt
```

_Optional:_ Install the pre-commit hooks:
```bash
pre-commit install
```

## Example File

The example is all self-contained within the notebook `r5py_example.ipynb`.

To run the notebook, make sure you have followed the installation instructions
above and have selected the correct kernel in the notebook to match the virtual
environment created.

You should then be able to follow the notebook from start to finish to see how
to use `r5py` to calculate travel times and visualise the results.

## Data Science Campus
At the [Data Science Campus](https://datasciencecampus.ons.gov.uk/about-us/) we
apply data science, and build skills, for public good across the UK and
internationally. Get in touch with the Campus at
[datasciencecampus@ons.gov.uk](datasciencecampus@ons.gov.uk).

## Licence

The code, unless otherwise stated, is released under [the MIT Licence][mit].

The documentation for this work is subject to [© Crown copyright][copyright]
and is available under the terms of the [Open Government 3.0][ogl] licence.

**TO BE UPDATE**

[`r5py`]: https://r5py.readthedocs.io/en/stable/index.html
[r5py Java installation]: https://r5py.readthedocs.io/en/stable/user-guide/installation/installation.html#java-development-kit
[mit]: LICENCE
[copyright]: http://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/
[ogl]: http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/
