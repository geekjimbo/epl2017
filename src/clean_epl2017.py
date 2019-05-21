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


# Extract «goals» from «Result» field, both: «home» goals and «away» goals:
# calc home goals
df_sorted['home_goals'] = df_sorted.apply(lambda x: extract_goals( "Home Team", x['result']  ), axis=1)

# calc away goals
df_sorted['away_goals'] = df_sorted.apply(lambda x: extract_goals( "Away Team", x['result']  ), axis=1)


# Step 3. Calculate the «points» won by each «Round Number, Team»

