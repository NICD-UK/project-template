#%% Load Libraries
import pandas
from pathlib import Path

#%% Setup
root_path = Path(__file__).parent.parent.parent
data_name = "<data-name>"

#%% Read Data
wrangle_data = pandas.read_pickle(root_path / f"data/wrangle/{data_name}.pkl")
