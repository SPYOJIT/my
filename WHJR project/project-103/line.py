import pandas as pd

import plotly.express as px

df = pd.read_csv("F:C:\Users\PC World\OneDrive\Desktop\WHJR project\project-103\data.csv")

fig = px.line(df, x="date", y="cases", color="country", title='Corona cases')

fig.show()
#made by saanvi