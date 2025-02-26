# -*- coding: utf-8 -*-
"""
SAMPLE TEST CASE

- INPUT: event log generated by a 6-station flow line
- OUTPUT:   1. generate a complete graph model of the line;
            2. generate a reduced model composed by 4 nodes;

Author: Giovanni Lugaresi
"""

# %% DEPENDENCIES

import pandas as pd 
import numpy as np
import json

# libraries developed in this work, here we only use these functions, but they are supported by several others in the modules
from msmlib import gen_model_init
from modelred import local_search
from msm_plots import plot_model

# %% SUPPORT FUNCTION

def convert(o):
    '''
    workaround to solve an issue saving numpy integers to json
    https://stackoverflow.com/questions/11942364/typeerror-integer-is-not-json-serializable-when-serializing-json-in-python
    '''
    if isinstance(o, np.generic): return o.item()  
    raise TypeError

# %% INPUT FILES READ

# Load config file: 
# the configuration file lists parameters of interest that set the model generation and tuning phases
with open('config.json', encoding='utf-8') as f:
    config = json.load(f)

# Load event log
data = pd.read_csv( 'eventlog.csv', sep=",", header='infer')

# %% SET PARAMETERS
# we set parameters for this particular test

# we are interested in a model of size 4 (4 nodes)
dim = 4

# we are interested in a model obtained by aggregation. We set the neighbourhood search
# so that it generates 2 neighbours by clustering, and none by nodes reduction
config['modelred']['n_aggregate'] = 2   
config['modelred']['n_reducing'] = 0


# %% MODEL GENERATION

model, unique_list, *args = gen_model_init(data, config, tag = True)

# graphical plot: COMMENT IT IF IT DOES NOT WORK
a = plot_model(model, 'original_model')

# simplified plot: list of arcs
print([a['arc'] for a in model['arcs']])

#save model json file
with open('original_model.json', 'w') as handle:
    json.dump(model,handle,default=convert)

# %%     MODEL TUNING

#set the target dimention (update request of model dimention in config file)
config["modelred"]["desired_size"] = dim

# model tuning
record = local_search(model, unique_list, config, 0)    

# take final model
final_model = record[-1]['solution']
#modelagg = neighbours_aggregate(model, 1)[0]

b = plot_model(final_model, 'tuned_model')

#save model json file
with open('tuned_model.json', 'w') as handle:
    json.dump(final_model, handle, default=convert)