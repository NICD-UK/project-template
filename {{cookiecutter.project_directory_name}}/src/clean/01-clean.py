#%% Load Libraries
import pandas
from pathlib import Path

#%% Setup
root_path = Path(__file__).parent.parent.parent
data_name = "<data-name>"

#%% Read Data
raw_data = pandas.read_csv(root_path / f"data/raw/{data_name}.csv")

#%% Clean Data
clean_data = raw_data

#%% Write Data
clean_data.to_pickle(root_path / f"data/clean/{data_name}.pkl")
