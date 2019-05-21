# load dataset
import pandas as pd 
import yaml
import re

def extract_goals(role, goals_str):
    expresion = "([0-9]*)(\s*-\s*)([0-9]*)"
    re_match = re.match(expresion, goals_str)
    if type(re_match) == type(None):
        return -1
    
    goals = int(re_match[1])
    if role == "Away Team":
        goals = int(re_match[3])
    return goals

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

# change data element names
# rename data elements
cols = ["round_number", "date", "location", "team_role", "team", "result"]
df_sorted.columns = cols