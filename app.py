# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, dcc, html, Output, Input, callback
import plotly.express as px
import pandas as pd

import plotly.express as px

import pandas as pd
import json

# Read in data
data_folder = "assets/data/"

# Reading the data for the age category, case states and sex graphs
df_age_cat_yrs = pd.read_csv(data_folder + "df_age_cat_yrs.csv")
df_case_state = pd.read_csv(data_folder + "df_case_status.csv")
df_sex = pd.read_csv(data_folder + "df_sex.csv")
# To make sure all graphs have the same scaling, determine the maximum frequency. It does not matter which total column
# is used, the all have the same maximum total
max_frequency = df_case_state['Total'].max()
# Needed for plotting the data in the counties
with open('geojson-counties-fips.json') as jsondata:
    counties = json.load(jsondata)

# Initalizing the app
app = Dash()

# Setting the inital values
year = 2008
status_selection = 'Confirmed'
sex_selection = 'Female'
age_cat_selection = 'Total'

df_age_selection = df_age_cat_yrs.loc[df_age_cat_yrs['Year'] == year, ['Year', 'FIPS', age_cat_selection]]
df_sex_selection = df_sex.loc[df_sex['Year'] == year, ['Year',  'FIPS', sex_selection]]
df_status_selection = df_case_state.loc[df_case_state['Year'] == year, ['Year', 'FIPS', status_selection]]

# Generating dropdownlist for year selection
year_list = [x for x in range(2008, 2022)]

# Generating the USA maps

fig_age = px.choropleth(
    df_age_selection, 
    geojson=counties, 
    locations='FIPS', 
    color=age_cat_selection, 
    scope='usa',
    range_color=[0, max_frequency],
    )

fig_status = px.choropleth(
    df_status_selection, 
    geojson=counties, 
    locations='FIPS', 
    color=status_selection, 
    scope='usa',
    range_color=[0, max_frequency],
    )

fig_sex = px.choropleth(
    df_sex_selection, 
    geojson=counties, 
    locations='FIPS', 
    color=sex_selection, 
    scope='usa',
    range_color=[0, max_frequency],
    )


app.layout = html.Div([
    html.H3("Select year to check"),
    dcc.Dropdown(year_list, '2008', id='year-dropdown'),
    # Radio item for age group
    html.H4("Select age group"),
    dcc.RadioItems(['0-19', '20+','Suppressed', 'Unknown', 'Total'],
                   'Total',
                   id='age_selection',
                   inline=True
                   ),
    dcc.Graph(
        id='age_graph',
        figure=fig_age
    ),
    # Radio items for case status
    html.H4("Select case status group"),    
    dcc.RadioItems(['Confirmed', 'Probable', 'Total'],
                   'Total',
                   id='status_selection',
                   inline=True
                   ),    
    dcc.Graph(
        id='status_graph',
        figure=fig_status
    ),
    # Radio items for sex status
    html.H4("Select gender group"),    
    dcc.RadioItems(['Female', 'Male', 'Total'],
                   'Total',
                   id='sex_selection',
                   inline=True
                   ),      
    dcc.Graph(
        id='sex_graph',
        figure=fig_sex
    ) 
])

# Callback for age category graph
@callback(
    Output('age_graph', 'figure'),
    Input('year-dropdown', 'value'),
    Input('age_selection', 'value')
    )
def set_display_age(selected_year, selected_age):
    df_age_selection = df_age_cat_yrs.loc[df_age_cat_yrs['Year'] == selected_year, ['Year', 'FIPS', selected_age]]
    fig_age = px.choropleth(
    df_age_selection, 
    geojson=counties, 
    locations='FIPS', 
    color=selected_age, 
    scope='usa',
    range_color=[0, max_frequency],
    )
    return fig_age

# Callback for case status graph
@callback(
    Output('status_graph', 'figure'),
    Input('year-dropdown', 'value'),
    Input('status_selection', 'value')
    )
def set_display_status(selected_year, selected_status):
    df_status_selection = df_case_state.loc[df_case_state['Year'] == selected_year, ['Year', 'FIPS', selected_status]]
    fig_status = px.choropleth(
    df_status_selection, 
    geojson=counties, 
    locations='FIPS', 
    color=selected_status, 
    scope='usa',
    range_color=[0, max_frequency],
    )
    return fig_status

# Callback for gender graph
@callback(
    Output('sex_graph', 'figure'),
    Input('year-dropdown', 'value'),
    Input('sex_selection', 'value')
    )
def set_display_sex(selected_year, selected_sex):
    df_sex_selection = df_sex.loc[df_sex['Year'] == selected_year, ['Year', 'FIPS', selected_sex]]
    fig_sex = px.choropleth(
    df_sex_selection, 
    geojson=counties, 
    locations='FIPS', 
    color=selected_sex, 
    scope='usa',
    range_color=[0, max_frequency],
    )
    return fig_sex

if __name__ == '__main__':
    app.run(debug=True)