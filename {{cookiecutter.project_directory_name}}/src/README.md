# Transformation Checklist

## Motivation

## Cleaning Checklist

For each data source:

*rows x columns*

- [ ] read data from `/data/raw/`
- [ ] ...
- [ ] check quality
    - uniqueness
    - consistency
    - validity
- [ ] write data to `/data/clean/`

## Wrangling Checklist

*observations x variables*

For each data product:

- [ ] read data from `/data/clean/`
- [ ] ...
- [ ] check quality
    - completeness
    - timeliness
    - accuracy
- [ ] write data to `/data/wrangle/`

## Modelling checklist

For each model:

- [ ] read data from `/data/wrangle/`
- [ ] preproces data
    - remove zero-variance variables
    - encode categorical variables
    - impute missing values
    - transformation skewed variables
    - centre and scale variables
    - decorrelate variables
- [ ] write model to `/data/model/`
