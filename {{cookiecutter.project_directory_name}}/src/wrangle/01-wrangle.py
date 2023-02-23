#%% Load Libraries
import pandas
import os
from pyprojroot import here

#%% Setup
data_name = "<data-name>"

#%% Read Data
clean_data = pandas.read_pickle(os.path.join(here(), "data", "clean", f"{data_name}.pkl"))

#%% Clean Data
wrangle_data = clean_data

#%% Write Data
wrangle_data.to_pickle(os.path.join(here(), "data", "wrangle", f"{data_name}.pkl"))
