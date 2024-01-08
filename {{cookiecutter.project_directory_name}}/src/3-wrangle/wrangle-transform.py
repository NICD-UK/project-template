#%% Load Libraries
import pandas
from pathlib import Path

#%% Setup
root_path = Path(__file__).parent.parent.parent
data_name = "<data-name>"

#%% Read Data
clean_data = pandas.read_pickle(root_path / f"data/clean/{data_name}.pkl")

#%% Wrangle Data
wrangle_data = clean_data

#%% Write Data
wrangle_data.to_pickle(root_path / f"data/wrangle/{data_name}.pkl")
