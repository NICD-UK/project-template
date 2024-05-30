<img src="figures/logo.png" width=400 align="right">

# Project Template

![](https://img.shields.io/github/v/release/NICD-UK/project-template?color=4ce48c&include_prereleases)
![](https://img.shields.io/github/license/NICD-UK/project-template)

The `project-template` package can create a [project sturcture](#project-structure) and [template scripts](#templates-scripts) for a data science project. The package also provides tools to automate common data science tasks. The package has been developed to be used with [Visual Studio Code](https://code.visualstudio.com) for Python projects and [RStudio](https://posit.co/products/open-source/rstudio/) for R projects.

## Install

In the command line run:

```bash
pip3 install cookiecutter
```

## Create

In the command line move to where you want to create the project directory and run:

```bash
python3 -m cookiecutter https://github.com/NICD-UK/project-template
```

You will be prompted for the:

1. Project Name
2. Project Directory Name
3. Project Manager Name
4. Project Manager Email
5. Project Sponsor Name
6. Project Sponsor Email
7. Project Summary
8. <a name="language">Project Language</a>

In the command line run:

```bash
make
```

This command will:

1. Initialise a virtual environment:
    - `venv` for Python
    - `renv` for R
2. Install the packages required for the template scripts
3. Save the packages to a dependencies file:
    - `requirements.txt` for Python
    - `renv.lock` for R
4. Initialise a git repository

## Usage

To install a package in Python run:

```
venv/bin/pip install <package>
```

To install a package in R use the Packages tab in RStudio.

<img src="figures/rstudio-packages.png" height=80>

To save packages to the dependencies file run:

```
make save
```

To load packages from the dependencies file run:

```
make load
```

## Project Structure

The project has the following structure:

```
Makefile
README.md
data/
├─ clean/
├─ raw/
├─ wrangle/
models/
notebooks/
presentations/
reports/
src/
├─ 1-import/
├─ 2-clean/
├─ 3-wrangle/
├─ 4-model/
```

## Template Scripts

There are template scripts for:

1. transforming raw data into cleaned data in `src/2-clean/`,
2. visualising cleaned data in `src/2-clean/`,
3. transforming cleaned data into wrangled data in `src/3-wrangle/`,
4. visualising wrangled data in `src/3-wrangle`

available in [Python](https://www.python.org) or [R](https://www.r-project.org). Answer **Python** or **R** to the [Language](#language) prompt during setup for the corresponding template scripts. All template transformation scripts include code to read data from and write data to the appropriate data directories. All template visualisation scripts include code to read data from the appropriate data directory and to generate a data report. There is also a template script for presenting data in `presentations/` available in [Quarto](https://quarto.org).
