import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash_table import DataTable
from dash_table.Format import Format, Group, Scheme

from components import header
from app import app
import pandas as pd
import os
from sys import platform

incident_demand_card1 = [
    dbc.CardHeader("Demand",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='created1', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

incident_resolved_card1 = [
    dbc.CardHeader("Resolved",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='resolved1', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

incident_reopened_card1 = [
    dbc.CardHeader("Reopened",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='reopened1', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

incident_reassigned_card1 = [
    dbc.CardHeader("Reassigned",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='reassigned1', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

incident_escalated_card1 = [
    dbc.CardHeader("Escalated",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='escalated1', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

incident_demand_card2 = [
    dbc.CardHeader("Demand",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='created11', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

incident_resolved_card2 = [
    dbc.CardHeader("Resolved",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='resolved11', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

incident_reassigned_card2 = [
    dbc.CardHeader("Reassigned",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='reassigned11', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

incident_reopened_card2 = [
    dbc.CardHeader("Reopened",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='reopened11', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

incident_escalated_card2 = [
    dbc.CardHeader("Escalated",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='escalated11', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

sr_demand_card1 = [
    dbc.CardHeader("Demand",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='created2', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

sr_resolved_card1 = [
    dbc.CardHeader("Resolved",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='resolved2', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

sr_reassigned_card1 = [
    dbc.CardHeader("Reassigned",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='reassigned2', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

sr_reopened_card1 = [
    dbc.CardHeader("Reopened",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='reopened2', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

sr_escalated_card1 = [
    dbc.CardHeader("Escalated",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='escalated2', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

sr_demand_card2 = [
    dbc.CardHeader("Demand",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='created22', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

sr_resolved_card2 = [
    dbc.CardHeader("Resolved",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='resolved22', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

sr_reassigned_card2 = [
    dbc.CardHeader("Reassigned",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='reassigned22', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

sr_reopened_card2 = [
    dbc.CardHeader("Reopened",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='reopened22', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

sr_escalated_card2 = [
    dbc.CardHeader("Escalated",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='escalated22', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

incident_ibm_backlog_card1 = [
    dbc.CardHeader("Backlog with IBM",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='withibm1', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

incident_wpp_backlog_card1 = [
    dbc.CardHeader("Backlog with WPP",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='withwpp1', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

incident_total_backlog_card1 = [
    dbc.CardHeader("Total Backlog",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='total1', className='card-text',
                   style={'text-align':'center', 'height':'20px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

sr_ibm_backlog_card1 = [
    dbc.CardHeader("Backlog with IBM",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='withibm2', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

sr_wpp_backlog_card1 = [
    dbc.CardHeader("Backlog with WPP",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='withwpp2', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

sr_total_backlog_card1 = [
    dbc.CardHeader("Total Backlog",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='total2', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]
#incident_ibm_backlogage_card1

incident_ibm_backlogage_card1 = [
    dbc.CardHeader("Age of Backlog with IBM",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='ageibm1', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

incident_wpp_backlogage_card1 = [
    dbc.CardHeader("Age of Backlog with WPP",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='agewpp1', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

incident_total_backlogage_card1 = [
    dbc.CardHeader("Age of Total Backlog",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='totalage1', className='card-text',
                   style={'text-align':'center', 'height':'20px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

sr_ibm_backlogage_card1 = [
    dbc.CardHeader("Age of Backlog with IBM",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='ageibm2', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

sr_wpp_backlogage_card1 = [
    dbc.CardHeader("Age Backlog with WPP",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='agewpp2', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]

sr_total_backlogage_card1 = [
    dbc.CardHeader("Age Total Backlog",
            style={'text-align':'center','height':'30px',
                   'fontSize':14,'font-weight':'bold','margin-top':'-15px',}),
    dbc.CardBody([
            html.P(id='totalage2', className='card-text',
                   style={'text-align':'center', 'height':'1px',
                         'fontSize':30,'font-weight':'bold','margin-top':'-20px',})
        ]),
]



incidentpivot=pd.DataFrame(columns=['Backlog','00-30','31-60','61-90','91-120',\
                                    '121-180','181-365','365+'])
srpivot=pd.DataFrame(columns=[['Backlog','00-30','31-60','61-90','91-120',\
                                    '121-180','181-365','365+']])

    
    
    
# Get the logo to be displayed in the Navigation Bar
src = app.get_asset_url('IBM Logo.png')

regions = ['All Regions', 'APAC','EMEA','Global - EMEA','LATAM','NA.','Global - NA']
keyapps = ['Adept','Dynamics AX - NA','HR.net (Talent Tree)','JD Edwards','Maconomy - EMEA',\
           'Maconomy - NA','PeopleSoft','SAP','Tango & Condor']

legacyregions = ['All Regions', 'APAC','EMEA','Global - EMEA','LATAM','NA.','Global - NA']

resources = ['All', 'Local','GD',]
report_type = ['Throughput', 'Backlog']

# Dropdown for the menu in the Navigation Bar
dropdown = dbc.DropdownMenu(color="success",direction="left", right=False,
        children=[
            dbc.DropdownMenuItem("Regions", id = "regionmenu", href = '/ServiceNowDashboard/regions'),
            dbc.DropdownMenuItem("Key Applications", id = "keyappsmenu", href = '/ServiceNowDashboard/keyapps'),
            dbc.DropdownMenuItem("Legacy Report", href = '/ServiceNowDashboard/legacy'),
            dbc.DropdownMenuItem("SLA's", disabled=True, href = '/ServiceNowDashboard/sla'),
            dbc.DropdownMenuItem("Compare", href = '/ServiceNowDashboard/compare'),
            dbc.DropdownMenuItem(divider=True),
            dbc.DropdownMenuItem("Themes", disabled=True, href = '/ServiceNowDashboard/themes'),
            ],
        nav=True,
        in_navbar=True,
        label="Menu",
        )

path = os.path.dirname(os.path.abspath(__file__))
if (platform.upper().find('LINUX',0,-1) > 0):
    path += "//data//"
else:
    path += "\\data\\"

#path =  "C:\\Dashboard Apps\\ServiceNowDashboard\\data\\"
reportweeks = path + 'Weeks.csv'
weeksfile = pd.read_csv(reportweeks)
weeksfile.sort_values(['Year','Week'], ascending = [False, False], inplace=True)
currentyear = weeksfile['Year'].max()
years = weeksfile['Year'].unique()
weeks = weeksfile[weeksfile['Year'] == currentyear]
week1 = weeks['Week'].unique()
currentweek = weeks['Week'].unique().max()
markers = {1:'1',4:'4',8:'8',13:'13',17:'17',21:'21',26:'26',
           30:'30',34:'34',39:'39',43:'43',47:'47',53:'53'}

#cummulativethroughtputdata = path + 'Cummulative Weekly Incident Data.csv'

regions = html.Div([
    header.get_header(),

# start of Dropdown row
    html.Div(children = [

        html.Div([dbc.Label("Region",color="primary")],
                 style = {'padding-top':'0.5%','padding-left':'1.5%','font-weight':'bold'}),
        html.Div([dcc.Dropdown(id='region-dropdown', 
            options=[{'label': i, 'value': i} for i in regions
                    ], multi=False, clearable=False, value = 'All Regions',optionHeight=25,), 
                 ], style={'padding-top':'0.1%','padding-left':'1%','width':'20%','fontSize':14,},className = 'dbc_dark'),

        html.Div([dbc.Label("Year : ",color="primary")],
                 style = {'padding-top':'0.5%','padding-left':'5%','font-weight':'bold'}),
                
        html.Div([dcc.Dropdown(id='year-dropdown', 
            options=[{'label': i, 'value': i} for i in years
                    ], multi=False, clearable=False, value = currentyear,optionHeight=25,), 
                 ], style={'padding-top':'0.1%','padding-left':'1%','width': '10%','fontSize':14,},className = 'dbc_dark'),
                        
        html.Div([dbc.Label("Report Week : ",color="primary")],
                 style = {'padding-top':'0.5%','padding-left':'5%','font-weight':'bold'}),
            
        html.Div([dcc.Dropdown(id='week-dropdown', 
            options=[{'label': i, 'value': i} for i in week1
                    ], multi=False, clearable=False, value = currentweek,optionHeight=25,), 
                 ], style={'padding-top':'0.1%','padding-left':'1%','width':'10%','fontSize':14,},className = 'dbc_dark'),
            
        html.Div([dbc.Label("Team : ",color="primary")],
                 style = {'padding-top':'0.5%','padding-left':'5%','font-weight':'bold'}),

        html.Div([dcc.Dropdown(id='resource-dropdown', 
            options=[{'label': i, 'value': i} for i in resources
                    ], multi=False, clearable=False, value = 'All',optionHeight=25,), 
                 ], style={'padding-top':'0.1%','padding-left':'1%','width':'10%','fontSize':14},className = 'dbc_dark'),

        html.Div([dbc.Label("Review : ",color="primary")],
                 style = {'padding-top':'0.5%','padding-left':'4.5%','font-weight':'bold'}),

        html.Div([dcc.Dropdown(id='report-dropdown', 
            options=[{'label': i, 'value': i} for i in report_type
                    ], multi=False, clearable=False, value = 'Throughput',optionHeight=25,), 
                 ], style={'padding-top':'0.1%','padding-left':'1%','width':'10%','fontSize':14,},className = 'dbc_dark'),            
    ],className='row',style = {'padding-top': '35px'},),

# End of Dropdown row

# Start of throughput Containter    

# Start incident section
    html.Div([
    html.Div([
        dbc.Row([
        dbc.Col([
            dbc.Card(html.P(id = 'header1'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':20,'font-weight':'bold',\
                       'margin-left':'1.1%','margin-bottom':'2px','height':'25px','line-height':'25px',}),
            dbc.Row([
                dbc.Col(
                    [dbc.Card(incident_demand_card1, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_resolved_card1, inverse= True, color = 'success',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_reassigned_card1, inverse= True, color = 'primary',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_reopened_card1, inverse= True, color = 'warning',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_escalated_card1, inverse= True, color = 'danger',),],), 
            ],no_gutters=True, style={'margin-left':'1.3%','margin-bottom':'2px'}),
        
            dbc.Card(html.P(id = 'header3'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':20,'font-weight':'bold',\
                      'margin-left':'1.1%','height':'25px','line-height':'25px','margin-bottom':'2px'}),
            dbc.Row([
                dbc.Col(
                    [dbc.Card(incident_demand_card2, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_resolved_card2, inverse= True, color = 'success',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_reassigned_card2, inverse= True, color = 'primary',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_reopened_card2, inverse= True, color = 'warning',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_escalated_card2, inverse= True, color = 'danger',),],), 
            ],no_gutters=True, style={'margin-left':'1.3%','margin-bottom':'2px'}),
        ],style={'margin-right':'.5%'}),

# Service Request Section
        dbc.Col([
            dbc.Card(html.P(id = 'header2'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':20,'font-weight':'bold',\
                       'margin-right':'1.5%','margin-bottom':'2px','height':'25px','line-height':'25px',}),

            dbc.Row([
                dbc.Col(
                    [dbc.Card(sr_demand_card1, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_resolved_card1, inverse= True, color = 'success',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_reassigned_card1, inverse= True, color = 'primary',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_reopened_card1, inverse= True, color = 'warning',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_escalated_card1, inverse= True, color = 'danger',),],), 
            ],no_gutters=True, style={'margin-bottom':'2px','margin-right':'1.5%'}),
        
            dbc.Card(html.P(id = 'header4'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':20,'font-weight':'bold',\
                      'margin-right':'1.5%','height':'25px','line-height':'25px','margin-bottom':'2px'}),

            dbc.Row([
                dbc.Col(
                    [dbc.Card(sr_demand_card2, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_resolved_card2, inverse= True, color = 'success',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_reassigned_card2, inverse= True, color = 'primary',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_reopened_card2, inverse= True, color = 'warning',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_escalated_card2, inverse= True, color = 'danger',),],), 
            ],no_gutters=True, style={'margin-bottom':'2px','margin-right':'1.5%'}),
        ],),
        ],no_gutters=True),
    ],style={'margin-top':'2px'}),

# Start of demand vs throughput graphs
    dbc.Row(
        [
            html.Div([dcc.Loading(dcc.Graph(id='incident_demand_vs_throughput', 
                    config= {"scrollZoom": True,"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'49.7%','margin-right':'0.6%'},className='border 1px white'),
            html.Div([dcc.Loading(dcc.Graph(id='sr_demand_vs_throughput', 
                    config= {"scrollZoom": True,"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'49.7%'},className='border 1px white'),
    ],no_gutters=True, style={'margin-top':'1px','margin-left':'.6%', 'margin-right':'.7%'},
    ), 
# End of demand vs throughput graphs
        
# Start of MTTR graphs
    html.Div(children = [
        dbc.Row(children = [
            html.Div([dcc.Loading(dcc.Graph(id='incident_1_mttr', 
                    config= {"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'24.7%','margin-right':'.25%'},className='border 1px white'),
            
            html.Div([dcc.Loading(dcc.Graph(id='incident_x_mttr', 
                    config= {"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'24.7%','margin-right':'.6%'},className='border 1px white'),
        
            html.Div([dcc.Loading(dcc.Graph(id='sr_1_mttr', 
                    config= {"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'24.7%','margin-right':'.3%'},className='border 1px white'),
            
            html.Div([dcc.Loading(dcc.Graph(id='sr_x_mttr', 
                    config= {"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'24.7%'},className='border 1px white'),  
        ]),  
    ],style={'margin-top': '2px','margin-left':'1.6%','margin-right':'1.6%'}),
# End of MTTR graphs

# Start of weekly demand status graphs
    html.Div(children = [
        dbc.Row(children = [
            html.Div([dcc.Loading(dcc.Graph(id='incident_1_week', 
                    config= {"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'24.7%','margin-right':'.25%'},className='border 1px white'),
            
            html.Div([dcc.Loading(dcc.Graph(id='incident_x_week', 
                    config= {"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'24.7%','margin-right':'.6%'},className='border 1px white'),
        
            html.Div([dcc.Loading(dcc.Graph(id='sr_1_week', 
                    config= {"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'24.7%','margin-right':'.3%'},className='border 1px white'),
            
            html.Div([dcc.Loading(dcc.Graph(id='sr_x_week', 
                    config= {"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'24.7%'},className='border 1px white'),  
        ]),  
    ],style={'margin-top': '2px','margin-left':'1.6%','margin-right':'1.6%'}),# End of weekly demand status graphs
    
    ],id='throughput-container', style= {'display': 'block'}),
# End of throughput containter

# Start of Backlog Containter    
    html.Div([
    html.Div([
        dbc.Row([
        dbc.Col([
            dbc.Card(html.P(id = 'header5'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':20,'font-weight':'bold',\
                       'margin-left':'1.1%','margin-bottom':'2px','height':'25px','line-height':'25px',}),
            dbc.Row([
                dbc.Col(
                    [dbc.Card(incident_ibm_backlog_card1, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_wpp_backlog_card1, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_total_backlog_card1, inverse= True, color = 'info',),],), 
            ],no_gutters=True, style={'margin-left':'1.3%','margin-bottom':'2px'}),

            dbc.Card(html.P(id = 'header7'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':20,'font-weight':'bold',\
                       'margin-left':'1.1%','margin-bottom':'2px','height':'25px','line-height':'25px',}),
            dbc.Row([
                dbc.Col(
                    [dbc.Card(incident_ibm_backlogage_card1, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_wpp_backlogage_card1, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_total_backlogage_card1, inverse= True, color = 'info',),],), 
            ],no_gutters=True, style={'margin-left':'1.3%','margin-bottom':'2px'}),
        
        ],style={'margin-right':'.5%'}),

# Service Request Section
        dbc.Col([
            dbc.Card(html.P(id = 'header6'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':20,'font-weight':'bold',\
                       'margin-right':'1.5%','margin-bottom':'2px','height':'25px','line-height':'25px',}),
            dbc.Row([
                dbc.Col(
                    [dbc.Card(sr_ibm_backlog_card1, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_wpp_backlog_card1, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_total_backlog_card1, inverse= True, color = 'info',),],), 
            ],no_gutters=True, style={'margin-bottom':'2px','margin-right':'1.5%'}),

            dbc.Card(html.P(id = 'header8'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':20,'font-weight':'bold',\
                       'margin-right':'1.5%','margin-bottom':'2px','height':'25px','line-height':'25px',}),
            dbc.Row([
                dbc.Col(
                    [dbc.Card(sr_ibm_backlogage_card1, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_wpp_backlogage_card1, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_total_backlogage_card1, inverse= True, color = 'info',),],), 
            ],no_gutters=True, style={'margin-bottom':'2px','margin-right':'1.5%'}),
        
        ],),
        ],no_gutters=True),
    ],style={'margin-top':'2px'}),
# =============================================================================
    dbc.Row(
        [
            html.Div([dcc.Loading(dcc.Graph(id='incident_backlog_trend', 
                    config= {"scrollZoom": True,"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'49.7%','margin-right':'0.4%'},className='border 1px white'),

            html.Div([dcc.Loading(dcc.Graph(id='sr_backlog_trend', 
                    config= {"scrollZoom": True,"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'49.7%'},className='border 1px white'),
    ],style={'margin-top':'1px','margin-left':'.5%', 'margin-right':'.5%'},
    ), 
# End of Backlog Trend graphs
        
# Start of Backlog Agr Graphs
    dbc.Row(
        [
            html.Div([dcc.Loading(dcc.Graph(id='incident_backlog_age', 
                    config= {"scrollZoom": True,"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'49.7%','margin-right':'0.4%'},className='border 1px white'),

            html.Div([dcc.Loading(dcc.Graph(id='sr_backlog_age', 
                    config= {"scrollZoom": True,"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'49.7%'},className='border 1px white'),
    ],style={'margin-top':'1px','margin-left':'.5%', 'margin-right':'.5%'},
    ), 
# End of Backlog Age Graphs

    dbc.Row([        
        dbc.Col(
            [
            dbc.Card(html.P('Incident Backlog Age Buckets in Days'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':18,'font-weight':'bold', \
                    'margin-bottom':'2px','height':'22px','line-height':'22px',}),

            html.Div([dcc.RadioItems(id='incident_radio',inputStyle={"margin-right": "15px","margin-left": "10px",},
                options=[
                    {'label': 'By Team', 'value': 1},
                    {'label': 'By Reason', 'value': 2},
                ],
                value=1,
                labelStyle={'display': 'inline-block'}),
            ],className = 'dbc_dark'),
                        
            html.Div([DataTable(id='incident_age',
                columns=[
                {'name': 'Backlog', 'id': 'Backlog', 'type': 'text'}, 
                {'name': '0 to 30', 'id': '00-30', 'type': 'text'},
                {'name': '31 to 60', 'id': '31-60', 'type': 'text'},
                {'name': '61 to 90', 'id': '61-90', 'type': 'text'},
                {'name': '91 to 120', 'id': '91-120', 'type': 'text'},
                {'name': '121 to 180', 'id': '121-180', 'type': 'text'},
                {'name': '181 to 365', 'id': '181-365', 'type': 'text'},
                {'name': '365+', 'id': '365+', 'type': 'text'},],
                page_current= 0,
                page_action="native",
                page_size= 3,
                row_deletable=False, 
                selected_columns=[],
                selected_rows=[],
                style_data_conditional=([
                    {"if": {"state": "selected"},"backgroundColor": "inherit !important","border": "inherit !important",},
                    {'if': {'row_index': 'odd'}, 'backgroundColor': 'PeachPuff'},
                    {'if': {'row_index': 'even'}, 'backgroundColor': 'LemonChiffon'},]),
                style_header={'border': '1px solid black','fontSize':14, 'font-family':'Calibri', 'backgroundColor': 'red', 'fontWeight': 'bold',
                              'whiteSpace': 'normal', 'height': 'auto', 'color':'white','text-align':'center'},
                style_data ={'border': '1px solid black','lineHeight': '15px','color':'black','text-align':'center','font-weight':'bold','fontSize':14},
                style_cell={'padding': '5px','fontSize':14, 'font-family':'Calibri',},),
            ],style={'margin-top':'-7px'}), 
            
            
            ],style={'margin-right':'0.6%',}
        ),
                            
        dbc.Col(
            [
            dbc.Card(html.P('Service Request Backlog Age Buckets in Days'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':18,'font-weight':'bold', \
                    'margin-bottom':'2px','margin-left':'-.3%','height':'22px','line-height':'22px',}),

            html.Div([dcc.RadioItems(id='sr_radio',inputStyle={"margin-right": "15px","margin-left": "10px",},
                options=[
                    {'label': 'By Team', 'value': 1},
                    {'label': 'By Reason', 'value': 2},
                ],
                value=1,
                labelStyle={'display': 'inline-block'}),
            ],className = 'dbc_dark'),
            
            html.Div([DataTable(id='sr_age',
                columns=[
                {'name': 'Backlog', 'id': 'Backlog', 'type': 'text'}, 
                {'name': '0 to 30', 'id': '00-30', 'type': 'text'},
                {'name': '31 to 60', 'id': '31-60', 'type': 'text'},
                {'name': '61 to 90', 'id': '61-90', 'type': 'text'},
                {'name': '91 to 120', 'id': '91-120', 'type': 'text'},
                {'name': '121 to 180', 'id': '121-180', 'type': 'text'},
                {'name': '181 to 365', 'id': '181-365', 'type': 'text'},
                {'name': '365+', 'id': '365+', 'type': 'text'},],
                page_current= 0,
                page_action="native",
                page_size= 3,
                row_deletable=False, 
                selected_columns=[],
                selected_rows=[],
                style_data_conditional=([
                    {"if": {"state": "selected"},"backgroundColor": "inherit !important","border": "inherit !important",},
                    {'if': {'row_index': 'odd'}, 'backgroundColor': 'PeachPuff'},
                    {'if': {'row_index': 'even'}, 'backgroundColor': 'LemonChiffon'},]),
                style_header={'border': '1px solid black','fontSize':14, 'font-family':'Calibri', 'backgroundColor': 'red', 'fontWeight': 'bold',
                              'whiteSpace': 'normal', 'height': 'auto', 'color':'white','text-align':'center'},
                style_data ={'border': '1px solid black','lineHeight': '15px','color':'black','text-align':'center','font-weight':'bold','fontSize':14},
                style_cell={'padding': '5px','fontSize':14, 'font-family':'Calibri',},),
            ],style={'margin-top':'-7px'}), 
            ],style={'margin-left':'-.1%'}
        ),
        ],no_gutters=True, style={'margin-top':'3px','margin-bottom':'3px','margin-left':'0.5%','margin-right':'0.5%',},),

#    dbc.Row([        
        
      
#        ]),   
        

        ],id='backlog-container', style= {'display': 'block'}),
# End of backlog containter

    dcc.Store(id='intermediate-value'),
    dcc.Store(id='startyearweek'),
    dcc.Store(id='endyearweek'),

# Start of slider
        html.Div(children = [
        html.Div([dbc.Label("Week Slider:",color="primary")],
                 style = {'padding-top': '0.1%','padding-left': '1.5%', 'width':'8%','font-weight': 'bold',}),
        html.Div([dcc.Slider(id='week-slider', 
                min = 1, max = 53, marks=markers, value = 13), 
            ],style={'padding-left': '.1%', 'padding-top':'.3%','width':'85%'},className = 'dbc_dark'),
        ],className =' row'),
# End of slider


]),
# End of region wise dashboard

# Start of key application wise dashboard
keyapps = html.Div(children = [
    header.get_header(),

# start of Dropdown row
    html.Div(children = [

        html.Div([dbc.Label("Key App",color="primary")],
                 style = {'padding-top':'0.5%','padding-left':'1.5%','font-weight':'bold'}),
        html.Div([dcc.Dropdown(id='region-dropdown', 
            options=[{'label': i, 'value': i} for i in keyapps
                    ], multi=False, clearable=False, value = 'Adept', optionHeight=25,)
                 ], style={'padding-top':'0.1%','padding-left':'1%','width':'20%','fontSize':14,},className = 'dbc_dark'),

        html.Div([dbc.Label("Year : ",color="primary")],
                 style = {'padding-top':'0.5%','padding-left':'5%','font-weight':'bold'}),
                
        html.Div([dcc.Dropdown(id='year-dropdown', 
            options=[{'label': i, 'value': i} for i in years
                    ], multi=False, clearable=False, value = currentyear, optionHeight=25,), 
                 ], style={'padding-top':'0.1%','padding-left':'1%','width': '10%','fontSize':14,},className = 'dbc_dark'),
                        
        html.Div([dbc.Label("Report Week : ",color="primary")],
                 style = {'padding-top':'0.5%','padding-left':'5%','font-weight':'bold'}),
            
        html.Div([dcc.Dropdown(id='week-dropdown', 
            options=[{'label': i, 'value': i} for i in week1
                    ], multi=False, clearable=False, value = currentweek, optionHeight=25,), 
                 ], style={'padding-top':'0.1%','padding-left':'1%','width':'10%','fontSize':14,},className = 'dbc_dark'),
            
        html.Div([dbc.Label("Team : ",color="primary")],
                 style = {'padding-top':'0.5%','padding-left':'5%','font-weight':'bold'}),

        html.Div([dcc.Dropdown(id='resource-dropdown', 
            options=[{'label': i, 'value': i} for i in resources
                    ], multi=False, clearable=False, value = 'All', optionHeight=25,), 
                 ], style={'padding-top':'0.1%','padding-left':'1%','width':'10%','fontSize':14},className = 'dbc_dark'),

        html.Div([dbc.Label("Review : ",color="primary")],
                 style = {'padding-top':'0.5%','padding-left':'4.5%','font-weight':'bold'}),

        html.Div([dcc.Dropdown(id='report-dropdown', 
            options=[{'label': i, 'value': i} for i in report_type
                    ], multi=False, clearable=False, value = 'Throughput', optionHeight=25,), 
                 ], style={'padding-top':'0.1%','padding-left':'1%','width':'10%','fontSize':14,},className = 'dbc_dark'),            
    ],className='row',style = {'padding-top': '35px'},),

# End of Dropdown row

# Start of throughput Containter    

# Start incident section
    html.Div([
    html.Div([
        dbc.Row([
        dbc.Col([
            dbc.Card(html.P(id = 'header1'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':20,'font-weight':'bold',\
                       'margin-left':'1.1%','margin-bottom':'2px','height':'25px','line-height':'25px',}),
            dbc.Row([
                dbc.Col(
                    [dbc.Card(incident_demand_card1, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_resolved_card1, inverse= True, color = 'success',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_reassigned_card1, inverse= True, color = 'primary',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_reopened_card1, inverse= True, color = 'warning',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_escalated_card1, inverse= True, color = 'danger',),],), 
            ],no_gutters=True, style={'margin-left':'1.3%','margin-bottom':'2px'}),
        
            dbc.Card(html.P(id = 'header3'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':20,'font-weight':'bold',\
                      'margin-left':'1.1%','height':'25px','line-height':'25px','margin-bottom':'2px'}),
            dbc.Row([
                dbc.Col(
                    [dbc.Card(incident_demand_card2, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_resolved_card2, inverse= True, color = 'success',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_reassigned_card2, inverse= True, color = 'primary',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_reopened_card2, inverse= True, color = 'warning',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_escalated_card2, inverse= True, color = 'danger',),],), 
            ],no_gutters=True, style={'margin-left':'1.3%','margin-bottom':'2px'}),
        ],style={'margin-right':'.5%'}),

# Service Request Section
        dbc.Col([
            dbc.Card(html.P(id = 'header2'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':20,'font-weight':'bold',\
                       'margin-right':'1.5%','margin-bottom':'2px','height':'25px','line-height':'25px',}),

            dbc.Row([
                dbc.Col(
                    [dbc.Card(sr_demand_card1, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_resolved_card1, inverse= True, color = 'success',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_reassigned_card1, inverse= True, color = 'primary',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_reopened_card1, inverse= True, color = 'warning',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_escalated_card1, inverse= True, color = 'danger',),],), 
            ],no_gutters=True, style={'margin-bottom':'2px','margin-right':'1.5%'}),
        
            dbc.Card(html.P(id = 'header4'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':20,'font-weight':'bold',\
                      'margin-right':'1.5%','height':'25px','line-height':'25px','margin-bottom':'2px'}),

            dbc.Row([
                dbc.Col(
                    [dbc.Card(sr_demand_card2, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_resolved_card2, inverse= True, color = 'success',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_reassigned_card2, inverse= True, color = 'primary',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_reopened_card2, inverse= True, color = 'warning',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_escalated_card2, inverse= True, color = 'danger',),],), 
            ],no_gutters=True, style={'margin-bottom':'2px','margin-right':'1.5%'}),
        ],),
        ],no_gutters=True),
    ],style={'margin-top':'2px'}),

# Start of demand vs throughput graphs
    dbc.Row(
        [
            html.Div([dcc.Loading(dcc.Graph(id='incident_demand_vs_throughput', 
                    config= {"scrollZoom": True,"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'49.7%','margin-right':'0.6%'},className='border 1px white'),
            html.Div([dcc.Loading(dcc.Graph(id='sr_demand_vs_throughput', 
                    config= {"scrollZoom": True,"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'49.7%'},className='border 1px white'),
    ],no_gutters=True, style={'margin-top':'1px','margin-left':'.6%', 'margin-right':'.7%'},
    ), 
# End of demand vs throughput graphs
        
# Start of MTTR graphs
    html.Div(children = [
        dbc.Row(children = [
            html.Div([dcc.Loading(dcc.Graph(id='incident_1_mttr', 
                    config= {"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'24.7%','margin-right':'.25%'},className='border 1px white'),
            
            html.Div([dcc.Loading(dcc.Graph(id='incident_x_mttr', 
                    config= {"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'24.7%','margin-right':'.6%'},className='border 1px white'),
        
            html.Div([dcc.Loading(dcc.Graph(id='sr_1_mttr', 
                    config= {"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'24.7%','margin-right':'.3%'},className='border 1px white'),
            
            html.Div([dcc.Loading(dcc.Graph(id='sr_x_mttr', 
                    config= {"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'24.7%'},className='border 1px white'),  
        ]),  
    ],style={'margin-top': '2px','margin-left':'1.6%','margin-right':'1.6%'}),
# End of MTTR graphs

# Start of weekly demand status graphs
    html.Div(children = [
        dbc.Row(children = [
            html.Div([dcc.Loading(dcc.Graph(id='incident_1_week', 
                    config= {"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'24.7%','margin-right':'.25%'},className='border 1px white'),
            
            html.Div([dcc.Loading(dcc.Graph(id='incident_x_week', 
                    config= {"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'24.7%','margin-right':'.6%'},className='border 1px white'),
        
            html.Div([dcc.Loading(dcc.Graph(id='sr_1_week', 
                    config= {"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'24.7%','margin-right':'.3%'},className='border 1px white'),
            
            html.Div([dcc.Loading(dcc.Graph(id='sr_x_week', 
                    config= {"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'24.7%'},className='border 1px white'),  
        ]),  
    ],style={'margin-top': '2px','margin-left':'1.6%','margin-right':'1.6%'}),# End of weekly demand status graphs
    
    ],id='throughput-container', style= {'display': 'block'}),
# End of throughput containter

# Start of Backlog Containter    
    html.Div([
    html.Div([
        dbc.Row([
        dbc.Col([
            dbc.Card(html.P(id = 'header5'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':20,'font-weight':'bold',\
                       'margin-left':'1.1%','margin-bottom':'2px','height':'25px','line-height':'25px',}),
            dbc.Row([
                dbc.Col(
                    [dbc.Card(incident_ibm_backlog_card1, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_wpp_backlog_card1, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_total_backlog_card1, inverse= True, color = 'info',),],), 
            ],no_gutters=True, style={'margin-left':'1.3%','margin-bottom':'2px'}),

            dbc.Card(html.P(id = 'header7'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':20,'font-weight':'bold',\
                       'margin-left':'1.1%','margin-bottom':'2px','height':'25px','line-height':'25px',}),
            dbc.Row([
                dbc.Col(
                    [dbc.Card(incident_ibm_backlogage_card1, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_wpp_backlogage_card1, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(incident_total_backlogage_card1, inverse= True, color = 'info',),],), 
            ],no_gutters=True, style={'margin-left':'1.3%','margin-bottom':'2px'}),
        
        ],style={'margin-right':'.5%'}),

# Service Request Section
        dbc.Col([
            dbc.Card(html.P(id = 'header6'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':20,'font-weight':'bold',\
                       'margin-right':'1.5%','margin-bottom':'2px','height':'25px','line-height':'25px',}),
            dbc.Row([
                dbc.Col(
                    [dbc.Card(sr_ibm_backlog_card1, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_wpp_backlog_card1, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_total_backlog_card1, inverse= True, color = 'info',),],), 
            ],no_gutters=True, style={'margin-bottom':'2px','margin-right':'1.5%'}),

            dbc.Card(html.P(id = 'header8'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':20,'font-weight':'bold',\
                       'margin-right':'1.5%','margin-bottom':'2px','height':'25px','line-height':'25px',}),
            dbc.Row([
                dbc.Col(
                    [dbc.Card(sr_ibm_backlogage_card1, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_wpp_backlogage_card1, inverse= True, color = 'info',),],style={'margin-right':'1.5%',}), 
                dbc.Col(
                    [dbc.Card(sr_total_backlogage_card1, inverse= True, color = 'info',),],), 
            ],no_gutters=True, style={'margin-bottom':'2px','margin-right':'1.5%'}),
        
        ],),
        ],no_gutters=True),
    ],style={'margin-top':'2px'}),
# =============================================================================
    dbc.Row(
        [
            html.Div([dcc.Loading(dcc.Graph(id='incident_backlog_trend', 
                    config= {"scrollZoom": True,"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'49.7%','margin-right':'0.4%'},className='border 1px white'),

            html.Div([dcc.Loading(dcc.Graph(id='sr_backlog_trend', 
                    config= {"scrollZoom": True,"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'49.7%'},className='border 1px white'),
    ],style={'margin-top':'1px','margin-left':'.5%', 'margin-right':'.5%'},
    ), 
# End of Backlog Trend graphs
        
# Start of Backlog Agr Graphs
    dbc.Row(
        [
            html.Div([dcc.Loading(dcc.Graph(id='incident_backlog_age', 
                    config= {"scrollZoom": True,"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'49.7%','margin-right':'0.4%'},className='border 1px white'),

            html.Div([dcc.Loading(dcc.Graph(id='sr_backlog_age', 
                    config= {"scrollZoom": True,"displayModeBar": False, "showTips": False,'displaylogo': False}),
            )],style={'width':'49.7%'},className='border 1px white'),
    ],style={'margin-top':'1px','margin-left':'.5%', 'margin-right':'.5%'},
    ), 
# End of Backlog Age Graphs

    dbc.Row([        
        dbc.Col(
            [
            dbc.Card(html.P('Incident Backlog Age Buckets in Days'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':15,'font-weight':'bold',\
                       'height':'25px','line-hieght':'25px','margin-bottom':'2px'}),

            html.Div([dcc.RadioItems(id='incident_radio',inputStyle={"margin-right": "15px","margin-left": "10px",},
                options=[
                    {'label': 'By Team', 'value': 1},
                    {'label': 'By Reason', 'value': 2},
                ],
                value=1,
                labelStyle={'display': 'inline-block'}),
            ],className = 'dbc_dark'),
                        
            html.Div([DataTable(id='incident_age',
                columns=[
                {'name': 'Backlog', 'id': 'Backlog', 'type': 'text'}, 
                {'name': '0 to 30', 'id': '00-30', 'type': 'text'},
                {'name': '31 to 60', 'id': '31-60', 'type': 'text'},
                {'name': '61 to 90', 'id': '61-90', 'type': 'text'},
                {'name': '91 to 120', 'id': '91-120', 'type': 'text'},
                {'name': '121 to 180', 'id': '121-180', 'type': 'text'},
                {'name': '181 to 365', 'id': '181-365', 'type': 'text'},
                {'name': '365+', 'id': '365+', 'type': 'text'},],
                page_current= 0,
                page_action="native",
                page_size= 3,
                row_deletable=False, 
                selected_columns=[],
                selected_rows=[],
                style_data_conditional=([
                    {"if": {"state": "selected"},"backgroundColor": "inherit !important","border": "inherit !important",},
                    {'if': {'row_index': 'odd'}, 'backgroundColor': 'PeachPuff'},
                    {'if': {'row_index': 'even'}, 'backgroundColor': 'LemonChiffon'},]),
                style_header={'border': '1px solid black','fontSize':14, 'font-family':'Calibri', 'backgroundColor': 'red', 'fontWeight': 'bold',
                              'whiteSpace': 'normal', 'height': 'auto', 'color':'white','text-align':'center'},
                style_data ={'border': '1px solid black','lineHeight': '15px','color':'black','text-align':'center','font-weight':'bold','fontSize':14},
                style_cell={'padding': '5px','fontSize':14, 'font-family':'Calibri',},),
            ],style={'margin-top':'-7px'}), 
            
            
            ],style={'margin-right':'0.6%',}
        ),
                            
        dbc.Col(
            [
            dbc.Card(html.P('Service Request Backlog Age Buckets in Days'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':15,'font-weight':'bold',\
                       'height':'20px','line-hieght':'20px','margin-left':'-.3%','margin-bottom':'2px'}),

            html.Div([dcc.RadioItems(id='sr_radio',inputStyle={"margin-right": "15px","margin-left": "10px",},
                options=[
                    {'label': 'By Team', 'value': 1},
                    {'label': 'By Reason', 'value': 2},
                ],
                value=1,
                labelStyle={'display': 'inline-block'}),
            ],className = 'dbc_dark'),
            
            html.Div([DataTable(id='sr_age',
                columns=[
                {'name': 'Backlog', 'id': 'Backlog', 'type': 'text'}, 
                {'name': '0 to 30', 'id': '00-30', 'type': 'text'},
                {'name': '31 to 60', 'id': '31-60', 'type': 'text'},
                {'name': '61 to 90', 'id': '61-90', 'type': 'text'},
                {'name': '91 to 120', 'id': '91-120', 'type': 'text'},
                {'name': '121 to 180', 'id': '121-180', 'type': 'text'},
                {'name': '181 to 365', 'id': '181-365', 'type': 'text'},
                {'name': '365+', 'id': '365+', 'type': 'text'},],
                page_current= 0,
                page_action="native",
                page_size= 3,
                row_deletable=False, 
                selected_columns=[],
                selected_rows=[],
                style_data_conditional=([
                    {"if": {"state": "selected"},"backgroundColor": "inherit !important","border": "inherit !important",},
                    {'if': {'row_index': 'odd'}, 'backgroundColor': 'PeachPuff'},
                    {'if': {'row_index': 'even'}, 'backgroundColor': 'LemonChiffon'},]),
                style_header={'border': '1px solid black','fontSize':14, 'font-family':'Calibri', 'backgroundColor': 'red', 'fontWeight': 'bold',
                              'whiteSpace': 'normal', 'height': 'auto', 'color':'white','text-align':'center'},
                style_data ={'border': '1px solid black','lineHeight': '15px','color':'black','text-align':'center','font-weight':'bold','fontSize':14},
                style_cell={'padding': '5px','fontSize':14, 'font-family':'Calibri',},),
            ],style={'margin-top':'-7px'}), 
            ],style={'margin-left':'-.1%'}
        ),
        ],no_gutters=True, style={'margin-top':'3px','margin-bottom':'3px','margin-left':'0.5%','margin-right':'0.5%',},),

#    dbc.Row([        
        
      
#        ]),   
        

        ],id='backlog-container', style= {'display': 'block'}),
# End of backlog containter

    dcc.Store(id='intermediate-value'),
    dcc.Store(id='startyearweek'),
    dcc.Store(id='endyearweek'),

# Start of slider
        html.Div(children = [
        html.Div([dbc.Label("Week Slider:",color="primary")],
                 style = {'padding-top': '0.1%','padding-left': '1.5%', 'width':'8%','font-weight': 'bold',}),
        html.Div([dcc.Slider(id='week-slider', 
                min = 1, max = 53, marks=markers, value = 13), 
            ],style={'padding-left': '.1%', 'padding-top':'.3%','width':'85%'},className = 'dbc_dark'),
        ],className =' row'),
# End of slider


]),

# Start of key application wise dashboard

themes = html.Div(children = [
    header.get_header(),
    header.get_regions(),
    html.H3(['Themes Page is under Construction'],style={'textAlign' : 'center'})
])

sla = html.Div(children = [
    header.get_header(),
    header.get_regions(),
    html.H3(['Themes Page is under Construction'],style={'textAlign' : 'center'})

]),

compare = html.Div(children = [
    header.get_header(),
    html.Div(
        [
        dbc.Button("Add Chart", id="add-chart", color='warning', n_clicks=0) ],
            style = {'padding-top': '35px'},),
    html.Div(id='container', children=[])

]),

legacy = html.Div(children = [
    header.get_header(),

# start of Dropdown row
    html.Div(children = [

        html.Div([dbc.Label("Region",color="primary")],
                 style = {'padding-top':'0.5%','padding-left':'1.5%','font-weight':'bold'}),
        html.Div([dcc.Dropdown(id='legacyregion-dropdown', 
            options=[{'label': i, 'value': i} for i in legacyregions
                    ],  multi=False, clearable=False, value = 'All Regions', optionHeight=25,), 
                 ], style={'padding-top':'0.1%','padding-left':'1%','width':'20%','fontSize':14,},className = 'dbc_dark'),

        html.Div([dbc.Label("Year : ",color="primary")],
                 style = {'padding-top':'0.5%','padding-left':'10%','font-weight':'bold'}),
                
        html.Div([dcc.Dropdown(id='year-dropdown', 
            options=[{'label': i, 'value': i} for i in years
                    ], multi=False, clearable=False, value = currentyear, optionHeight=25,), 
                 ], style={'padding-top':'0.1%','padding-left':'1%','width': '10%','fontSize':14,},className = 'dbc_dark'),
                        
        html.Div([dbc.Label("Report Week : ",color="primary")],
                 style = {'padding-top':'0.5%','padding-left':'10%','font-weight':'bold'}),
            
        html.Div([dcc.Dropdown(id='week-dropdown', 
            options=[{'label': i, 'value': i} for i in week1
                    ], multi=False, clearable=False, value = currentweek, optionHeight=25,), 
                 ], style={'padding-top':'0.1%','padding-left':'1%','width':'10%','fontSize':14,},className = 'dbc_dark'),
            
        html.Div([dbc.Label("Team : ",color="primary")],
                 style = {'padding-top':'0.5%','padding-left':'10%','font-weight':'bold'}),

        html.Div([dcc.Dropdown(id='resource-dropdown', 
            options=[{'label': i, 'value': i} for i in resources
                    ], multi=False, clearable=False, value = 'All', optionHeight=25,), 
                 ], style={'padding-top':'0.1%','padding-left':'1%','width':'10%','fontSize':14},className = 'dbc_dark'),

    ],className='row',style = {'padding-top': '35px'},),

# End of Dropdown row

    dbc.Row([        
        dbc.Col(
            [
            dbc.Card(html.P('Throughput - Tickets Resolved (or Cancelled)'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':15,'font-weight':'bold',\
                       'height':'20px','line-hieght':'20px','margin-bottom':'0px'}),

           html.Div([DataTable(id='throughput',
                page_current= 0,
                page_action="native",
                page_size= 3,
                row_deletable=False, 
                selected_columns=[],
                selected_rows=[],
                style_data_conditional=([
                    {"if": {"state": "selected"},"backgroundColor": "inherit !important","border": "inherit !important",},
                    {'if': {'row_index': 'odd'}, 'backgroundColor': 'PeachPuff'},
                    {'if': {'row_index': 'even'}, 'backgroundColor': 'LemonChiffon'},]),
                style_header={'border': '1px solid black','fontSize':14, 'font-family':'Calibri', 'backgroundColor': 'red', 'fontWeight': 'bold',
                              'whiteSpace': 'normal', 'height': 'auto', 'color':'white','text-align':'center'},
                style_data ={'border': '1px solid black','lineHeight': '15px','color':'black','text-align':'center','font-weight':'bold','fontSize':14},
                style_cell={'padding': '5px','fontSize':14, 'font-family':'Calibri',},),
            ],style={'margin-bottom':'2px'}), 

            dbc.Card(html.P('Demand - Tickets Created'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':15,'font-weight':'bold',\
                       'height':'20px','line-hieght':'20px','margin-bottom':'0px'}),

           html.Div([DataTable(id='demand',
                page_current= 0,
                page_action="native",
                page_size= 3,
                row_deletable=False, 
                selected_columns=[],
                selected_rows=[],
                style_data_conditional=([
                    {"if": {"state": "selected"},"backgroundColor": "inherit !important","border": "inherit !important",},
                    {'if': {'row_index': 'odd'}, 'backgroundColor': 'PeachPuff'},
                    {'if': {'row_index': 'even'}, 'backgroundColor': 'LemonChiffon'},]),
                style_header={'border': '1px solid black','fontSize':14, 'font-family':'Calibri', 'backgroundColor': 'red', 'fontWeight': 'bold',
                              'whiteSpace': 'normal', 'height': 'auto', 'color':'white','text-align':'center'},
                style_data ={'border': '1px solid black','lineHeight': '15px','color':'black','text-align':'center','font-weight':'bold','fontSize':14},
                style_cell={'padding': '5px','fontSize':14, 'font-family':'Calibri',},),
            ],style={'margin-bottom':'2px'}), 

            dbc.Card(html.P('MTTR (Days): Osprey Resolver Group > Resolved'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':15,'font-weight':'bold',\
                       'height':'20px','line-hieght':'20px','margin-bottom':'0px'}),

           html.Div([DataTable(id='mttr',
                page_current= 0,
                page_action="native",
                page_size= 3,
                row_deletable=False, 
                selected_columns=[],
                selected_rows=[],
                style_data_conditional=([
                    {"if": {"state": "selected"},"backgroundColor": "inherit !important","border": "inherit !important",},
                    {'if': {'row_index': 'odd'}, 'backgroundColor': 'PeachPuff'},
                    {'if': {'row_index': 'even'}, 'backgroundColor': 'LemonChiffon'},]),
                style_header={'border': '1px solid black','fontSize':14, 'font-family':'Calibri', 'backgroundColor': 'red', 'fontWeight': 'bold',
                              'whiteSpace': 'normal', 'height': 'auto', 'color':'white','text-align':'center'},
                style_data ={'border': '1px solid black','lineHeight': '15px','color':'black','text-align':'center','font-weight':'bold','fontSize':14},
                style_cell={'padding': '5px','fontSize':14, 'font-family':'Calibri',},),
            ],style={'margin-bottom':'2px'}), 

            dbc.Card(html.P('Health Check: New INC, SR tickets (last week)'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':15,'font-weight':'bold',\
                       'height':'20px','line-hieght':'20px','margin-bottom':'0px'}),

           html.Div([DataTable(id='healthcheck',
                page_current= 0,
                page_action="native",
                page_size= 3,
                row_deletable=False, 
                selected_columns=[],
                selected_rows=[],
                style_data_conditional=([
                    {"if": {"state": "selected"},"backgroundColor": "inherit !important","border": "inherit !important",},
                    {'if': {'row_index': 'odd'}, 'backgroundColor': 'PeachPuff'},
                    {'if': {'row_index': 'even'}, 'backgroundColor': 'LemonChiffon'},]),
                style_header={'border': '1px solid black','fontSize':14, 'font-family':'Calibri', 'backgroundColor': 'red', 'fontWeight': 'bold',
                              'whiteSpace': 'normal', 'height': 'auto', 'color':'white','text-align':'center'},
                style_data ={'border': '1px solid black','lineHeight': '15px','color':'black','text-align':'center','font-weight':'bold','fontSize':14},
                style_cell={'padding': '5px','fontSize':14, 'font-family':'Calibri',},),
            ],style={'margin-top':'0px'}), 

        ],style={'margin-left':'.5%','margin-right':'5px'}),
            
        dbc.Col(
            [
            dbc.Card(html.P('Backlog: Average age in days (IBM tickets / WPP tickets)'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':15,'font-weight':'bold',\
                       'height':'20px','line-hieght':'20px','margin-bottom':'0px'}),

           html.Div([DataTable(id='backlogage',
                page_current= 0,
                page_action="native",
                page_size= 4,
                row_deletable=False, 
                selected_columns=[],
                selected_rows=[],
                style_data_conditional=([
                    {"if": {"state": "selected"},"backgroundColor": "inherit !important","border": "inherit !important",},
                    {'if': {'row_index': 'odd'}, 'backgroundColor': 'PeachPuff'},
                    {'if': {'row_index': 'even'}, 'backgroundColor': 'LemonChiffon'},]),
                style_header={'border': '1px solid black','fontSize':14, 'font-family':'Calibri', 'backgroundColor': 'red', 'fontWeight': 'bold',
                              'whiteSpace': 'normal', 'height': 'auto', 'color':'white','text-align':'center'},
                style_data ={'border': '1px solid black','lineHeight': '33px','color':'black','text-align':'center','font-weight':'bold','fontSize':14},
                style_cell={'padding': '5px','fontSize':14, 'font-family':'Calibri',},),
            ],style={'margin-bottom':'2px'}), 

            dbc.Card(html.P('Backlog: Number of Tickets (IBM tickets / WPP tickets)'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':15,'font-weight':'bold',\
                       'height':'20px','line-hieght':'20px','margin-bottom':'0px'}),

           html.Div([DataTable(id='backlog',
                page_current= 0,
                page_action="native",
                page_size= 3,
                row_deletable=False, 
                selected_columns=[],
                selected_rows=[],
                style_data_conditional=([
                    {"if": {"state": "selected"},"backgroundColor": "inherit !important","border": "inherit !important",},
                    {'if': {'row_index': 'odd'}, 'backgroundColor': 'PeachPuff'},
                    {'if': {'row_index': 'even'}, 'backgroundColor': 'LemonChiffon'},]),
                style_header={'border': '1px solid black','fontSize':14, 'font-family':'Calibri', 'backgroundColor': 'red', 'fontWeight': 'bold',
                              'whiteSpace': 'normal', 'height': 'auto', 'color':'white','text-align':'center'},
                style_data ={'border': '1px solid black','lineHeight': '33px','color':'black','text-align':'center','font-weight':'bold','fontSize':14},
                style_cell={'padding': '5px','fontSize':14, 'font-family':'Calibri',},),
            ],style={'margin-bottom':'2px'}), 

            dbc.Card(html.P('Backlog: Aged Tickets ((IBM tickets / WPP tickets))'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':15,'font-weight':'bold',\
                       'height':'20px','line-hieght':'20px','margin-bottom':'0px'}),

           html.Div([DataTable(id='backlogagebucket',
                page_current= 0,
                page_action="native",
                page_size= 3,
                row_deletable=False, 
                selected_columns=[],
                selected_rows=[],
                style_data_conditional=([
                    {"if": {"state": "selected"},"backgroundColor": "inherit !important","border": "inherit !important",},
                    {'if': {'row_index': 'odd'}, 'backgroundColor': 'PeachPuff'},
                    {'if': {'row_index': 'even'}, 'backgroundColor': 'LemonChiffon'},]),
                style_header={'border': '1px solid black','fontSize':14, 'font-family':'Calibri', 'backgroundColor': 'red', 'fontWeight': 'bold',
                              'whiteSpace': 'normal', 'height': 'auto', 'color':'white','text-align':'center'},
                style_data ={'border': '1px solid black','lineHeight': '33px','color':'black','text-align':'center','font-weight':'bold','fontSize':14},
                style_cell={'padding': '5px','fontSize':14, 'font-family':'Calibri',},),
            ],style={'margin-bottom':'2px'}), 

            dbc.Card(html.P('Backlog: Aged Tickets On-Hold resons (INC, SR)'), color="primary", inverse=True,
                style={'text-align':'center','fontSize':15,'font-weight':'bold',\
                       'height':'20px','line-hieght':'20px','margin-bottom':'0px'}),

           html.Div([DataTable(id='wppbacklogage',
                sort_action="native",
                sort_mode="single",
                column_selectable="single",
                page_current= 0,
                page_action="native",
                page_size= 4,
                row_deletable=False, 
                selected_columns=[],
                selected_rows=[],
                style_data_conditional=([
                    {"if": {"state": "selected"},"backgroundColor": "inherit !important","border": "inherit !important",},
                    {'if': {'row_index': 'odd'}, 'backgroundColor': 'PeachPuff'},
                    {'if': {'row_index': 'even'}, 'backgroundColor': 'LemonChiffon'},]),
                style_header={'border': '1px solid black','fontSize':14, 'font-family':'Calibri', 'backgroundColor': 'red', 'fontWeight': 'bold',
                              'whiteSpace': 'normal', 'height': 'auto', 'color':'white','text-align':'center'},
                style_data ={'border': '1px solid black','lineHeight': '15px','color':'black','text-align':'center','font-weight':'bold','fontSize':14},
                style_cell={'padding': '5px','fontSize':14, 'font-family':'Calibri',},),
            ],style={'margin-top':'0px'}), 

        ],style={'margin-right':'.5%'}),

    ],no_gutters= True,style={'margin-top':'3px'}),
])