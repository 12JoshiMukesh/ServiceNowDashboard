import dash
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.CYBORG]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets,title='ServiceNow Dashboard',
				update_title='Loading...', suppress_callback_exceptions=True, 
				url_base_pathname='/ServiceNowDashboard/',
			meta_tags=[{'name': 'viewport',
							'content': 'width=device-width, initial-scale=1.0'}]
				)
server = app.server

