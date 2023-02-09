#%% Load Libraries
import pandas
from pyprojroot import here
import os

#%% Setup
data_name = "<data-name>"

#%% Read Data
clean_data = pandas.read_pickle(os.path.join(here(), "data", "clean", f"{data_name}.pkl"))
