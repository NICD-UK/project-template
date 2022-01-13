# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Project Organization

```
README.md
config.yml
data/
├─ clean/
├─ model/
├─ raw/
├─ wrangle/
notebooks/
├─ describe/
├─ explore/
├─ final/
notes.md
reports/
src/
├─ clean/
├─ model/
├─ wrangle/
```

## Data Science Workflow

Task sections in the [CRISP-DM Guide](https://www.the-modeling-agency.com/crisp-dm.pdf) are provided.

### Business Understanding

1. **Determine Business Objectives** [1.1]
    - *background* (`notes.md`)
    - *business objectives* (`notes.md`)
    - *business success criteria* (`notes.md`)
2. **Assess Situation** [1.2]
    - *inventory of resources* (`notes.md`)
    - *requirements, assumptions and constraints* (`notes.md`)
    - *risks and contingencies* (`notes.md`)
    - *terminology* (`notes.md`)
    - *costs and benefits* (`notes.md`)
3. **Determine Data Science Questions** [1.3]
    - *data science questions* (`notes.md`)
    - *data science success criteria* (`notes.md`)
4. **Plan Project** [1.4]
    - *project plan* (`notes.md`)
    - *initial assessment of tools and techniques* (`notes.md`)

### Data Understanding

1. **Collect Raw Data** [2.1]
    - *raw data* (`data/raw/`)
    - *initial cleaning scripts* (`src/clean/`)
    - *initial clean data* (`data/clean`)
2. **Describle Data** [2.2]
    - *description report* (`reports/describe/`)
3. **Explore Data** [2.3]
    - *exploration report* (`reports/explore/`)

## Data Preparation

1. **Clean Data** [3.2]
    - *cleaning scripts* (e.g. `src/clean/`)
    - *clean data* (`data/clean/`)
2. **Wrangle Data** [3.1, 3.3, 3.4]
    - *wrangling scripts* (`src/wrangle/`)
    - *wrangle data* (`data/wrangle/`)

### Modelling

1. **Select Modelling Techniques** [4.1]
    - *modelling techniques* (`notes.md`)
    - *modelling assumptions* (`notes.md`)
2. **Generate Test Design** [4.2]
    - *test design* (`notes.md`)
3. **Build Model** [4.3]
    - *modelling scripts* (`src/model/`)
    - *models* (`data/models/`)
    - *model descriptions* (`notes.md`)
4. **Assess Model** [4.4]
    - *model assessment (`notes.md`)

### Evaluation

1. **Evaluate Results** [5.1]
    - *evaluation of data science results with respect to business success criteria* (`notes.md`)
    - *approved models* (`notes.md`)
2. **Review Process** [5.2]
    - *process review* (`notes.md`)
3. **Determine Next Steps** [5.3]
    - *possible actions* (`notes.md`)
    - *decision* (`notes.md`)

### Deployment

1. **Plan Deployment** [6.1]
    - *deployment plan* (`notes.md`)
2. **Plan Monitoring and Maintenance** [6.2]
    - *monitoring and maintenance plan* (`notes.md`)
3. **Produce Final Report** [6.3]
    - *final report*  (`reports/final/`)
    - *final presentation* (`reports/final/`)
4. **Review Project** [6.4]
    - *project review* (`notes.md`)