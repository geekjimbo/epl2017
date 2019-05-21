# load dataset
import pandas as pd 
import yaml

CONFIG_PATH='./config/config.yml'
_config = yaml.load( open( CONFIG_PATH ))
dataset = _config['dev']['file_path_name']
df = pd.read_csv(dataset)

print("succeeded !")