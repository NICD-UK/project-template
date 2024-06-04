#%% Load Packages
import pandas
from pathlib import Path
from ydata_profiling import ProfileReport

#%% Setup
root_path = Path(__file__).parent.parent.parent
data_name = "income"

#%% Read Data
clean_data = pandas.read_pickle(root_path / f"data/clean/{data_name}.pkl")

#%% Describe Data 
profile = ProfileReport(clean_data, title="Description Report")
profile.to_file(root_path / f"reports/clean/{data_name}.html")
