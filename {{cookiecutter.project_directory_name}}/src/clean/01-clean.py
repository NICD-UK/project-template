#%% Load Libraries
import pandas
from pyprojroot import here
import os

#%% Setup
data_name = "<data-name>"

#%% Read Data
raw_data = pandas.read_csv(os.path.join(here(), "data", "raw", f"{data_name}.csv"))

#%% Clean Data
clean_data = raw_data

#%% Write Data
clean_data.to_pickle(os.path.join(here(), "data", "clean", f"{data_name}.pkl"))
