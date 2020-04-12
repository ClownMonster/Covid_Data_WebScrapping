import pandas as pd
import plotly.express as px

df = pd.read_excel('./CovidData.xlsx')

fig = px.bar(df.head(100), x = 'Country Name', y = 'Total Cases', color = 'Total Cases' )
fig.update_layout(title_text = 'Clown Monsters Visualization')
fig.show()