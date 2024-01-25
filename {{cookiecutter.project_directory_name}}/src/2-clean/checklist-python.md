# Cleaning Checklist

Data cleaning transfomrations and tests are independent of the data product. There are three transformations and three tests that are required data cleaning:

- [ ] Format Column Names
- [ ] Format Column Types
- [ ] Format Missing Values
- [ ] Test for Uniquness 
- [ ] Test for Validity
- [ ] Test for Consistency

## Format Column Names

Make sure column names are consistently formatted e.g., `snake_case`, `PascalCase`

```python
raw_data = raw_data.rename(columns={
    'column1:': 'name1',
    'column2:': 'name2',
})
```

## Format Column Types

Make sure column types are apporopriately formatted e.g., `float`, `category`

```python
raw_data = raw_data.astype({
    'column1': 'float',
    'column2': 'category',
})
```

## Format Missing Values

Make sure missing values are correctly formatted e.g., `NA`s that are zeros

```python
raw_data = raw_data.fillna({
    'column1': 0,
    'column2': 0,
})
```

## Test for Uniqueness

Test for unique rows and correct for or remove duplicates

```python
n_duplicates = raw_data.duplicated().sum()
print(f'There are {n_duplicates} duplicates.')
raw_data = raw_data.drop_duplicates()
```

## Test for Validity

Test for valid values and correct for or remove outliers

```python
n_outliers = raw_data[raw_data['column1'] < 0].sum()
print(f'There are {n_outliers} outliers.')
raw_data = raw_data.drop(raw_data[raw_data['column1'] < 0].index)
```

## Test for Consistency

Test for consistent values and correct for or remove errors

```python
n_errors = raw_data[raw_data['column1'] == raw_data['column2']].sum()
print(f"There are {n_errors} errors.")
raw_data = raw_data.drop(raw_data[raw_data['column1'] == raw_data['column2']].index)
```
