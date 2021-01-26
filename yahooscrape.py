import re
import json
import csv
from io import StringIO
from bs4 import BeautifulSoup
import requests
import pandas as pd

# Company Tag lets the program know which company to scrape the following data from
company_tag = 'GME'

stats= 'https://finance.yahoo.com/quote/{}/key-statistics?p={}'.format(company_tag, company_tag)
profile= 'https://finance.yahoo.com/quote/{}/profile?p={}'.format(company_tag, company_tag)
financials= 'https://finance.yahoo.com/quote/{}/financials?p={}'.format(company_tag, company_tag)


# Getting Financial Data

response = requests.get(financials)
soup = BeautifulSoup(response.text, 'html.parser')
pattern = re.compile(r'\s--\sData\s--\s')
script_data = soup.find('script', text= pattern).contents[0]
start= script_data.find('context')-2
json_data = json.loads(script_data[start:-12])

income_statement_annual= json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['incomeStatementHistory']['incomeStatementHistory']
income_statement_quarterly= json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['incomeStatementHistoryQuarterly']['incomeStatementHistory']

cash_flow_annual= json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['cashflowStatementHistory']['cashflowStatements']
cash_flow_quarterly= json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['cashflowStatementHistoryQuarterly']['cashflowStatements']

balance_sheet_annual= json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['balanceSheetHistory']['balanceSheetStatements']
balance_sheet_quarterly= json_data['context']['dispatcher']['stores']['QuoteSummaryStore']['balanceSheetHistoryQuarterly']['balanceSheetStatements']

#Annual Income Statement
income_statement_annual_reduced = []
for i in income_statement_annual:
    statement= {}
    for key, val in i.items():
        try:
            statement[key] = val['raw']
        except TypeError:
            continue
        except KeyError:
            continue
    income_statement_annual_reduced.append(statement)
    
#Quarterly Income Statement
income_statement_quarterly_reduced = []
for i in income_statement_quarterly:
    statement= {}
    for key, val in i.items():
        try:
            statement[key] = val['raw']
        except TypeError:
            continue
        except KeyError:
            continue
    income_statement_quarterly_reduced.append(statement)

#Annual Cash Flow Statement
cash_flow_annual_reduced = []
for i in cash_flow_annual:
    statement= {}
    for key, val in i.items():
        try:
            statement[key] = val['raw']
        except TypeError:
            continue
        except KeyError:
            continue
    cash_flow_annual_reduced.append(statement)
    
#Quarterly Cash Flow Statement
cash_flow_quarterly_reduced = []
for i in cash_flow_quarterly:
    statement= {}
    for key, val in i.items():
        try:
            statement[key] = val['raw']
        except TypeError:
            continue
        except KeyError:
            continue
    cash_flow_quarterly_reduced.append(statement)

#Annual Balance Sheet Statement
balance_sheet_annual_reduced = []
for i in balance_sheet_annual:
    statement= {}
    for key, val in i.items():
        try:
            statement[key] = val['raw']
        except TypeError:
            continue
        except KeyError:
            continue
    balance_sheet_annual_reduced.append(statement)
    
#Quarterly Balance Sheet Statement
balance_sheet_quarterly_reduced = []
for i in balance_sheet_quarterly:
    statement= {}
    for key, val in i.items():
        try:
            statement[key] = val['raw']
        except TypeError:
            continue
        except KeyError:
            continue
    balance_sheet_quarterly_reduced.append(statement)

a_is = pd.DataFrame(income_statement_annual_reduced)
q_is = pd.DataFrame(income_statement_quarterly_reduced)
a_cf = pd.DataFrame(cash_flow_annual_reduced)
q_cf = pd.DataFrame(cash_flow_quarterly_reduced)
a_bs = pd.DataFrame(balance_sheet_annual_reduced)
q_bs = pd.DataFrame(balance_sheet_quarterly_reduced)


# Getting Profile Data

response = requests.get(profile)
soup = BeautifulSoup(response.text, 'html.parser')
pattern = re.compile(r'\s--\sData\s--\s')
script_data = soup.find('script', text= pattern).contents[0]
start= script_data.find('context')-2
json_data = json.loads(script_data[start:-12])


# Getting Statistics

response = requests.get(stats)
soup = BeautifulSoup(response.text, 'html.parser')
pattern = re.compile(r'\s--\sData\s--\s')
script_data = soup.find('script', text= pattern).contents[0]
start= script_data.find('context')-2
json_data = json.loads(script_data[start:-12])

