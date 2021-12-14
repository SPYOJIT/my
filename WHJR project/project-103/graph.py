import pandas as pd
import plotly.express as px

df = pd.read_csv("F:C:\Users\PC World\OneDrive\Desktop\WHJR project\project-103\data.csv")
fig = px.scatter(df, x="date", y="cases",color="country",title='Corona Cases')
fig.show()
#made by saanvi