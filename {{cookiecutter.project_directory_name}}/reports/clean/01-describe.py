#%% Load Libraries
import pandas
from pathlib import Path
from ydata_profiling import ProfileReport

#%% Setup
root_path = Path(__file__).parent.parent.parent
data_name = "<data-name>"

#%% Read Data
clean_data = pandas.read_pickle(root_path / f"data/clean/{data_name}.pkl")

#%% Describe Datadata 
profile = ProfileReport(clean_data, title="Description Report")
profile.to_notebook_iframe()
