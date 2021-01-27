import json
import csv
from io import StringIO
import requests
import pandas as pd

# Importing config.json to set company tag and history params
config = {}
with open('config.json') as config_json:
    config = json.load(config_json)

# Company Tag lets the program know which company to scrape the data from.
# Company Tag is set in the config.json
company_tag = config['company']

# Getting Historic Data from Yahoo Finance API

source = "https://query1.finance.yahoo.com/v7/finance/download/{}?".format(company_tag)

response = requests.get(source, params= config['params'])
file= StringIO(response.text)
reader= csv.reader(file)
data= list(reader)

# Converting list of lists into dataframe
df = pd.DataFrame(data= data[1:], columns= data[0])
df.set_index('Date', inplace= True)

# Saving Data
df.to_csv('{}_{}_{}_stock_data.csv'.format(config['company'], config['params']['range'], config['params']['interval']), index= True)

