# Project Template

## Setup

To use the project template:

```
pip install cookiecutter
cookiecutter https://github.com/NICD-UK/project-template
```

You will be prompted for the following answers:

1. Project Name
2. Project Directory Name
3. Project Manager Name
4. Project Manager Email
5. Project Sponsor Name
6. Project Sponsor Email
7. Project Summary
8. <a name="language">Language</a>: **Python** or **R**

Then run:

```
make
```

This command will:

1. Initialise a virtual environment
    - `venv` for Python
    - `renv` for R
2. Install the packages required for the template scipts
3. Save the packages to a dependencies file
    - `requirements.txt` for Python
    - `renv.lock` for R
4. Initialise a git repository

## Package Management

To install a package in Python run:

```
venv/bin/pip install <package>
```

To install a package in R use the Packages tab in RStudio.

To save the installed packages to the dependencies file run:

```
make save
```

To load the packages from the dependencies file run:

```
make load
```

## Project Structure

The project has the following structure:

```
README.md
data/
├─ clean/
├─ raw/
├─ wrangle/
models/
presentations/
reports/
├─ clean/
├─ wrangle/
src/
├─ clean/
├─ model/
├─ wrangle/
```

## Project Charter

The `README.md` file is the [Project Charter](https://en.wikipedia.org/wiki/Project_charter). The head of the project charter includes: the project name; the name and email of the project manager; and the name and email of the project sponsor. This is filled out with the answers to the corresponding prompts during setup. The body of the project charter includes:

- Summary
- Objectives
- Deliverables
- Resources
- Scope
- Costs and Benefits
- Risks and Contingencies

The body of the project charter is filled out during the project scoping phase.

## Script Templates

There are template scripts for:

1. cleaning data in `src/clean/`,
2. describing data in `reports/clean/`,
3. wrangling data in `src/wrangle/`,
4. exploring data in `reports/wrangle`

available in [Python](https://www.python.org) or [R](https://www.r-project.org). Answer **Python** or **R** to the [Language](#language) prompt during setup for the relevant template scripts. All template scripts include code to read from and write to the appropriate data directories. The template scripts for describing and exploring data generate reports for the cleaned and wrangled data, respectively. There is also a template script for presenting data in `presentations/` available in [Quarto](https://quarto.org).

## Recommendations

For the best experience it is recommended to use the project template with [Visual Studio Code](https://code.visualstudio.com) for Python projects and [RStudio](https://posit.co/products/open-source/rstudio/) for R projects. 
