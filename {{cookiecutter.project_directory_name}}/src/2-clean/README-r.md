# Data Cleaning

Data cleaning transformations and tests are independent of the data product. There are three transformations and three tests that are required for data cleaning:

- [ ] Format Column Names
- [ ] Format Column Types
- [ ] Format Missing Values
- [ ] Test for Uniquness 
- [ ] Test for Validity
- [ ] Test for Consistency

## Format Column Names

Make sure column names are consistently formatted e.g., `snake_case`, `PascalCase`

```r
raw_data <- raw_data %>%
  rename(
    name1 = column1,
    name2 = column2
  )
```

## Format Column Types

Make sure column types are appropriately formatted e.g., `numeric`, `factor`

```r
raw_data <- raw_data %>%
  mutate(
    column1 = as.numeric(column1),
    column2 = as.factor(column2),
  )
```

## Format Missing Values

Make sure missing values are correctly formatted e.g., `NA`s that should be zeros

```r
raw_data <- raw_data %>%
  mutate(
    column1 = ifelse(is.na(column1), 0, column1),
    column2 = ifelse(is.na(column2), 0, column2),
  )
```

## Test for Uniqueness

Test for unique rows and correct for or remove duplicates

```r
n_duplicates <- sum(duplicated(raw_data)) 
print(paste0('There are ', n_duplicates, ' duplicates.'))
raw_data <- raw_data %>%
  distinct()
```

## Test for Validity

Test for valid values and correct for or remove outliers

```r
n_outliers <- sum(pull(raw_data, column1) < 0)
print(paste0('There are ', n_outliers, ' outliers.'))
raw_data <- raw_data %>%
  filter(column1 >= 0)
```

## Test for Consistency

Test for consistent values and correct for or remove errors

```r
n_errors <- sum(pull(raw_data, column1) == pull(raw_data, column2))
print(paste0('There are ', n_errors, ' errors.'))
raw_data <- raw_data %>%
  filter(column1 != column2)
```
