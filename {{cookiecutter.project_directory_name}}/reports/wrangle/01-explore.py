#%% Load Libraries
import os
import pandas
from pyprojroot import here
from ydata_profiling import ProfileReport

#%% Setup
data_name = "<data-name>"

#%% Read Data
wrangle_data = pandas.read_pickle(os.path.join(here(), "data", "wrangle", f"{data_name}.pkl"))

#%% Explore Data
profile = ProfileReport(wrangle_data, title="Exploration Report")
profile.to_notebook_iframe()
