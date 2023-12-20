#%% Load Libraries
import pandas
from pathlib import Path
from ydata_profiling import ProfileReport

#%% Setup
root_path = Path(__file__).parent.parent.parent
data_name = "<data-name>"

#%% Read Data
wrangle_data = pandas.read_pickle(root_path / f"data/wrangle/{data_name}.pkl")

#%% Explore Data
profile = ProfileReport(wrangle_data, title="Exploration Report")
profile.to_file(root_path / f"reports/wrangle/{data_name}.html")
