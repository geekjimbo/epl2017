# load dataset
import pandas as pd 
import yaml
import re

CONFIG_PATH='./config/config.yml'
_config = yaml.load( open( CONFIG_PATH ))
dataset = _config['dev']['file_path_name']
df = pd.read_csv(dataset)

# transform home/away as pivot fields
# introducing pandas's «melt»
df_melted = df.melt(id_vars=['Round Number', 'Result', 'Date', 'Location'])

# sort the melted df
columns = ['Round Number', 'Date', 'Location', 'variable', 'value', 'Result']
df_sorted = df_melted[columns].sort_values(by=['Round Number', 'Date'])

# reset index
df_sorted = df_sorted.reset_index(drop=True)