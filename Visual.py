import pandas as pd
import plotly.express as px
from plotly import graph_objects as go

df = pd.read_excel('./CovidData.xlsx')

#fig = px.bar(df.head(100), x = 'Country Name', y = 'Total Cases', color = 'Total Cases' )
#fig.update_layout(title_text = 'Clown Monsters Visualization')
#fig.show()


fig = go.Figure()
#df.sort_values(df['Total Deaths per 1M'], ascending = False, inplace = True)
df = df.head(150)

fig.add_trace( go.Bar(y = df['Total Deaths Cases'], x = df['Country Name'], marker = {'colorscale': 'Viridis', 'color': 'rebeccapurple' }))
fig.update_layout(title_text = 'Heat Map Visulation', barmode = 'stack')

fig.show()
