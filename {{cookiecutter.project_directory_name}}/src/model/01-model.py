#%% Load Libraries
import pandas
from pathlib import Path
from sklearn.model_selection import train_test_split
import yaml

#%% Setup
root_path = Path(__file__).parent.parent.parent
with open(root_path / "params.yaml") as f:
    params = yaml.safe_load(f)["default"]
data_name = "<data-name>"

#%% Read Data
wrangle_data = pandas.read_pickle(root_path / f"data/wrangle/{data_name}.pkl")

#%% Split Data
X_data = wrangle_data.drop(columns=params["target"])
y_data = wrangle_data[params["target"]]
X_train, X_test, y_train, y_test = train_test_split(X_data, y_data,
    train_size=params["split"]["train"], 
    random_state=params["seed"],
)
