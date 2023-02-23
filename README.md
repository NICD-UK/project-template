# Project Template

## Setup

To use the project template:

```
pip install cookiecutter
cookiecutter https://github.com/NICD-UK/project-template
```

You will be prompted for eleven answers:

1. Project Name
2. Project Directory Name
3. Project Manager Name
4. Project Manager Email
5. Project Sponsor Name
6. Project Sponsor Email
7. Project Summary
8. <a name="raw-data-directory">Raw Data Directory</a>
9. <a name="language">Language</a> (**Python** / **R**)
10. <a name="venv">`venv` Project</a> (**No** / **Yes**)
11. <a name="git">`git` Project</a> (**No** / **Yes**)

## Project Structure

The project has the following structure:

```
README.md
config.yml
data/
├─ clean/
├─ model/
├─ raw/
├─ wrangle/
presentations/
reports/
├─ clean/
├─ final/
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

## Raw Data

Raw data files can be stored either:

1. inside the project directry in `data/raw/` or 
2. outside the project directory.

If the raw data files are stored outside the project directory answer the [Raw Data Directory](#raw-data-directory) prompt during setup with the absolute path to them. This absolute path is included in the `config.yml` file. The `config.yml` file can be different for each project collaborator.

## Script Templates

There are template scripts for:

1. cleaning data in `src/clean/`,
2. describing data in `reports/clean/`,
3. wrangling data in `src/wrangle/`,
4. exploring data in `reports/wrangle`

available in [Python](https://www.python.org) or [R](https://www.r-project.org). Answer **Python** or **R** to the [Language](#language) prompt during setup for the relevant scripts. All template scripts include code to read from and write to the appropriate data directories. The template scripts for describing and exploring data generate reports for the cleaned and wrangled data, respectively. There is also a template script for presenting data in `presentations/` available in [Quarto](https://quarto.org).

## Virtual Evironment and Git

Answer **Yes** to the [`venv` Project](#venv) prompt during setup for a Python virtual environment. This is recommended for Python projects. Answer **Yes** to the [`git` Project](#git) prompt during setup for a git repository. This is recommended for *all* projects.

## Recommendations

For the best experience it is recommended to use the project template with [Virtual Studio Code](https://code.visualstudio.com) for Python projects and [RStudio](https://posit.co/products/open-source/rstudio/) for R projects. 