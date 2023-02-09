#%% Load Libraries
import pandas
from pyprojroot import here
import os

#%% Setup
data_name = "<data-name>"

#%% Read Data
wrangle_data = pandas.read_pickle(os.path.join(here(), "data", "wrangle", f"{data_name}.pkl"))
