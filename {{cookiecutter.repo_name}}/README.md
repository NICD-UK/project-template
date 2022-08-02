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
notes.md
reports/
├─ describe/
├─ explore/
├─ final/
src/
├─ clean/
├─ model/
├─ wrangle/
```

## Data Science Workflow

Task sections in the [CRISP-DM Guide](https://www.the-modeling-agency.com/crisp-dm.pdf) are provided.

### Project Understanding

1. **Determine Project Objectives** [Section 1.1]
    - *background* (`notes.md`)
    - *project objectives* (`notes.md`)
    - *project success criteria* (`notes.md`)
2. **Assess Situation** [Section 1.2]
    - *inventory of resources* (`notes.md`)
    - *requirements, assumptions and constraints* (`notes.md`)
    - *risks and contingencies* (`notes.md`)
    - *terminology* (`notes.md`)
    - *costs and benefits* (`notes.md`)
3. **Determine Data Science Questions** [Section 1.3]
    - *data science questions* (`notes.md`)
    - *data science success criteria* (`notes.md`)
4. **Plan Project** [Section 1.4]
    - *project plan* (`notes.md`)
    - *initial assessment of tools and techniques* (`notes.md`)

### Data Understanding

1. **Collect Raw Data** [Section 2.1]
    - *raw data* (`data/raw/`)
    - *initial cleaning scripts* (`src/clean/`)
    - *initial clean data* (`data/clean`)
2. **Describe Data** [Section 2.2]
    - *description report* (`reports/describe/`)
3. **Explore Data** [Section 2.3]
    - *exploration report* (`reports/explore/`)

### Data Preparation

1. **Clean Data** [Section 3.2]
    - *cleaning scripts* (e.g. `src/clean/`)
    - *clean data* (`data/clean/`)
2. **Wrangle Data** [Section 3.1-4]
    - *wrangling scripts* (`src/wrangle/`)
    - *wrangle data* (`data/wrangle/`)

### Modelling

1. **Select Modelling Techniques** [Section 4.1]
    - *modelling techniques* (`notes.md`)
    - *modelling assumptions* (`notes.md`)
2. **Select Experimental Design** [Section 4.2]
    - *experimental design* (`notes.md`)
3. **Build Model** [Section 4.3]
    - *modelling scripts* (`src/model/`)
    - *models* (`data/model/`)
    - *model descriptions* (`notes.md`)
4. **Assess Model** [Section 4.4]
    - *model assessment* (`notes.md`)

### Evaluation

1. **Evaluate Results** [Section 5.1]
    - *evaluation of data science results with respect to project success criteria* (`notes.md`)
    - *approved models* (`notes.md`)
2. **Review Process** [Section 5.2]
    - *process review* (`notes.md`)
3. **Determine Next Steps** [Section 5.3]
    - *possible actions* (`notes.md`)
    - *decision* (`notes.md`)

### Deployment

1. **Plan Deployment** [Section 6.1]
    - *deployment plan* (`notes.md`)
2. **Plan Monitoring and Maintenance** [Section 6.2]
    - *monitoring and maintenance plan* (`notes.md`)
3. **Produce Final Report** [Section 6.3]
    - *final report*  (`reports/final/`)
    - *final presentation* (`reports/final/`)
4. **Review Project** [Section 6.4]
    - *project review* (`notes.md`)
