#%% Load Libraries
import pandas
import os
from pyprojroot import here
from ydata_profiling import ProfileReport

#%% Setup
data_name = "<data-name>"

#%% Read Data
clean_data = pandas.read_pickle(os.path.join(here(), "data", "clean", f"{data_name}.pkl"))

#%% Describe Datadata 
profile = ProfileReport(clean_data, title="Description Report")
profile.to_notebook_iframe()
