import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc

from app import app

src = app.get_asset_url('IBM Logo.png')

def get_header():

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

    header = html.Div(children = [
       dbc.Row(children = [
            dbc.Col(dbc.NavbarSimple(children = 
                [dropdown,dbc.Col(html.Img(src=src, height="30px"))],
                brand="ServiceNow Dashboard",
                brand_style = {'textAlign' : 'center','fontSize':25, 'color': 'white','fontWeight': 'bold'},
                brand_href="#",
                fixed = 'top',
                color='primary',
                style = {'textAlign' : 'center', 'padding-left': '37%','fontSize':18, 'height': '35px',
                     'padding-bottom' : '.5%','padding-top' : '0.5%','margin-bottom' : '0%'}
                )
                )
            ]
            ),
       ]
    )
    return header

def get_regions():   
    region_nav = html.Div(children = [
        dbc.Row(children = [
            dbc.Col(dcc.Link(html.H6('All Regions'), href='/ServiceNowDashboard/regions/allregions', id = 'allregions',),
                        style={'background-color':'springgreen', 'text-align':'center'}),
            dbc.Col(dcc.Link(html.H6('APAC'), href ='/ServiceNowDashboard/regions/apac', id = 'apac'),
                        style={'background-color':'springgreen', 'text-align':'center'}),
            dbc.Col(dcc.Link(html.H6('EMEA'), href ='/ServiceNowDashboard/regions/emea', id = 'emea'), 
                        style={'background-color':'springgreen', 'text-align':'center'}),
            dbc.Col(dcc.Link(html.H6('Global - EMEA'), href ='/ServiceNowDashboard/regions/globalemea', id = 'globalemea'), 
                        style={'background-color':'springgreen', 'text-align':'center'}),
            dbc.Col(dcc.Link(html.H6('LATAM'), href ='/ServiceNowDashboard/regions/latam', id = 'latam'),
                        style={'background-color':'springgreen', 'text-align':'center'}),
            dbc.Col(dcc.Link(html.H6('NA'), href ='/ServiceNowDashboard/regions/na', id = 'na'),
                        style={'background-color':'springgreen', 'text-align':'center'}),
            dbc.Col(dcc.Link(html.H6('Global - NA'), href ='/ServiceNowDashboard/regions/globalna', id = 'globalna'),
                        style={'background-color':'springgreen', 'text-align':'center'}),
            dbc.Col(dcc.Link(html.H6('GD'), href ='/ServiceNowDashboard/regions/gd', id = 'gd'),
                        style={'background-color':'springgreen', 'text-align':'center',}),
            ] , justify="center", style = {'padding-top': '35px'}
        )        
        ]
    )
    return region_nav

def get_keyapps():
    keyapps_nav = html.Div(children = [
        dbc.Row(children = [
            dbc.Col(dcc.Link(html.H6("ADEPT"), href ='/ServiceNowDashboard/keyapps/adept'),
                        style={'background-color':'sprintgreen', 'text-align':'center'}),
            dbc.Col(dcc.Link(html.H6("Dynamics AX - NA") ,href ='/ServiceNowDashboard/keyapps/dynamicsna'),
                        style={'background-color':'sprintgreen', 'text-align':'center'}),
            dbc.Col(dcc.Link(html.H6("HR.net (Talent Tree)"), href ='/ServiceNowDashboard/keyapps/hrnet'),
                        style={'background-color':'sprintgreen', 'text-align':'center'}),
            dbc.Col(dcc.Link(html.H6("JD Edwards"), href ='/ServiceNowDashboard/keyapps/jde'),
                        style={'background-color':'sprintgreen', 'text-align':'center'}),
            dbc.Col(dcc.Link(html.H6("Maconomy - EMEA"), href ='/ServiceNowDashboard/keyapps/maconomyemea'),
                        style={'background-color':'sprintgreen', 'text-align':'center'}),
            dbc.Col(dcc.Link(html.H6("Maconomy - NA"), href ='/ServiceNowDashboard/keyapps/maconomyna'),
                        style={'background-color':'sprintgreen', 'text-align':'center'}),
            dbc.Col(dcc.Link(html.H6("PeopleSoft"), href ='/ServiceNowDashboard/keyapps/ps'),
                        style={'background-color':'sprintgreen', 'text-align':'center'}),
            dbc.Col(dcc.Link(html.H6("SAP"), href ='/ServiceNowDashboard/keyapps/sap'),
                        style={'background-color':'sprintgreen', 'text-align':'center'}),
            dbc.Col(dcc.Link(html.H6("Tango & Condor"), href ='/ServiceNowDashboard/keyapps/tnc'),
                        style={'background-color':'springgreen', 'text-align':'center'}),
            ] , justify="center", style = {'padding-top': '35px','padding-botton':'20px'}
        )
        ]
    )
    return keyapps_nav
