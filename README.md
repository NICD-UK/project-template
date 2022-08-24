# Project Template

## Usage

To use the project template:

```
pip install cookiecutter
cookiecutter https://github.com/NICD-UK/project-template
```

You will be promted for nine inputs:

1. Project Name
2. Project Slug
3. Project Manager Name
4. Project Manager Email
5. Project Sponsor Name
6. Project Sponsor Email
7. Project Description
8. Raw data Directory
9. Python `venv` 

## Organization

```
README.md
config.yml
data/
├─ clean/
├─ model/
├─ raw/
├─ wrangle/
notebooks/
reports/
├─ describe/
├─ explore/
├─ final/
src/
├─ clean/
├─ model/
├─ wrangle/
```