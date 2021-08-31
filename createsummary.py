import pandas as pd
import os
from sys import platform

def get_Newstate(data):
    value = statedir[data]
    return value

statedir = {'Closed': 1,'Resolved':2,'Cancelled': 3,'Work In Progress': 4, 'On Hold': 5, 'Queued': 6}

path = os.path.dirname(os.path.abspath(__file__))
if (platform.upper().find('LINUX',0,-1) > 0):
    path += "//data//"
else:
    path += "\\data\\"

#path =  "C:\\Dashboard Apps\\ServiceNowDashboard\\data\\"
cummulativeincidentdata = path + 'Cummulative Weekly Incident Data.csv'
cummulativebacklogdata = path + 'Cummulative Weekly Backlog Data.csv'

region_summary = path + 'regionsummary.csv'
region_spread = path + 'regionspread.csv'
region_mttr = path + 'regionmttr.csv'

keyapp_summary = path + 'keyappsummary.csv'
keyapp_spread = path + 'keyappspread.csv'
keyapp_mttr = path + 'keyappmttr.csv'

tickettype = ['Incident','SR']
# Read Historical data in chunks

colnames = ['Assignment Group Region', 'Resource Type', 'TicketType', 'State_Type', 'State','Number',\
            'MTTR (FAORG > Resolved)', 'Year Created/Resolved','Wk Created/Resolved', 'Key Applications',]
    
chunksize = 100000
chunk_data = pd.read_csv(cummulativeincidentdata, iterator = True, chunksize=chunksize, \
                         infer_datetime_format= True, usecols = colnames)
tickets = pd.concat(chunk_data, ignore_index=True)

tickets.rename(columns={'Wk Created/Resolved':'Week','Year Created/Resolved':'Year',
                        'MTTR (FAORG > Resolved)':'MTTR','Assignment Group Region':'Region',
                        'Key Applications':'Key Apps','State_Type':'Status',
                        'Resource Type':'Type'}, inplace=True)

tickets = tickets[(tickets['TicketType'].isin(tickettype))]

tickets['Weekstr'] = tickets['Week'].apply(str).apply(lambda x: x.zfill(2))
tickets['Yearstr'] = tickets["Year"].apply(str) 
tickets['YearWeek'] = tickets['Yearstr'] + tickets['Weekstr']
tickets['YearWeek'] = tickets['YearWeek'].apply(int)
tickets['Newstate'] = tickets['State'].apply(get_Newstate)

tickets = tickets[['Region','Type','TicketType','State','Status','Year','Week','Number','MTTR',\
                       'YearWeek','Newstate','Key Apps']]

# Region Wise Summary of tickets
regionsummary = tickets.groupby(['Region','YearWeek','Year','Week','TicketType','Status','Type',\
                                 'State','Newstate'])['Number'].count().reset_index()

# Region Wise Spread of tickets created in a week
regionspread = tickets[(tickets['Status'] == 'Created')]
regionspread  = regionspread.groupby(['Region','YearWeek','Year','Week','TicketType','Status','Type',\
                                 'State','Newstate'])['Number'].count().reset_index()

# Region Wise MTTR
regionmttr = tickets[(tickets['Status'] == 'Resolved')]
regionmttr  = regionmttr.groupby(['Region','YearWeek','Year','Week','TicketType','Type'])\
                .agg({'Number':'count','MTTR':'mean'}).reset_index()

# Region Wise MTTR irrespective of Resource Type
regionmttrall = tickets[(tickets['Status'] == 'Resolved')]
regionmttrall  = regionmttrall.groupby(['Region','YearWeek','Year','Week','TicketType'])\
                .agg({'Number':'count','MTTR':'mean'}).reset_index()
regionmttrall['Type'] = 'All'
regionmttr = regionmttr.append(regionmttrall)

# Create Region Wise Summary Files
regionsummary.to_csv(region_summary, index = False)
regionspread.to_csv(region_spread, index = False)
regionmttr.to_csv(region_mttr, index = False)

# KeyApp Wise Summary of tickets
keyappsummary = tickets.groupby(['Key Apps','YearWeek','Year','Week','TicketType','Status','Type',\
                                 'State','Newstate'])['Number'].count().reset_index()

# KeyApp Wise Spread of tickets created in a week
keyappspread = tickets[(tickets['Status'] == 'Created')]
keyappspread  = keyappspread.groupby(['Key Apps','YearWeek','Year','Week','TicketType','Status','Type',\
                                 'State','Newstate'])['Number'].count().reset_index()

# KeyApp Wise MTTR
keyappmttr = tickets[(tickets['Status'] == 'Resolved')]
keyappmttr  = keyappmttr.groupby(['Key Apps','YearWeek','Year','Week','TicketType','Type'])\
                .agg({'Number':'count','MTTR':'mean'}).reset_index()

# KeyApp Wise MTTR irrespective of Resource Type
keyappmttrall = tickets[(tickets['Status'] == 'Resolved')]
keyappmttrall  = keyappmttrall.groupby(['Key Apps','YearWeek','Year','Week','TicketType'])\
                .agg({'Number':'count','MTTR':'mean'}).reset_index()
keyappmttrall['Type'] = 'All'
keyappmttr = keyappmttr.append(keyappmttrall)

# Create KeyApp Wise Summary Files
keyappsummary.to_csv(keyapp_summary, index = False)
keyappspread.to_csv(keyapp_spread, index = False)
keyappmttr.to_csv(keyapp_mttr, index = False)
