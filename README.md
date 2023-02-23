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
8. Raw Data Directory
9. Language (Python / R)
10. `venv` Project (No / Yes)
11. `git` Project (No / Yes)

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
notebooks/
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

Raw data files inside the project directory are in `data/raw/`. If the raw data files are outside the project directory: answer with the appropriate absoute path to the Raw Data Directory prompt during setup. This absolute path is in the `config.yml` file. The `config.yml` file can be different for each project collaborator.

## Script Templates

There are template scripts for cleaning data (`src/clean/`), describing data (`reports/clean/`), wrangling data (`src/wrangle/`) and exploring data (`reports/wrangle`) available in Python and R. The project template provides Python or R temmplate scripts depending on answer to the Language prompt during setup. All template scripts include code to read from and write to the appropriate data directories. The included code uses best practice to ensure reproducability. The template scripts for describing and exploring data generate reports for the cleaned and wrangled data, respectively. There is also a template script for presenting data (`presentations/`) available in Quarto.

## Virtual Evironment and Git

Answer Yes to the `venv` Project prompt during setup for a Python 3 virtual environment. This is recommended for Python projects. Answer Yes to the `git` Project prompt during setup for a git repository. This is recommended for *all* projects.

## Recommendations

For the best experience it is recommended to use the project template with [Virtual Studio Code](https://code.visualstudio.com) for Python projects and [RStudio](https://posit.co/products/open-source/rstudio/) for R projects. 