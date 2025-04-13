from preswald import text, plotly, connect, get_df, table, query, slider
import pandas as pd
import plotly.express as px




# Load the CSV
connect()
df = get_df('videoGamesSales_csv')


#Manipulate data
sql = "SELECT * FROM videoGamesSales_csv WHERE Rank <= 50"
filtered_df = query(sql, "videoGamesSales_csv")


#UI
text("# Video Game Sales")
table(filtered_df, title="Filtered Data")


# Slider user control for sales thresholds
threshold = slider("Global Sales Threshold", min_val=0, max_val=100, default=50)


#Updated thresholds
filtered_sales_df = df[df["Global_Sales"] >= threshold]


#Creating visualization using scatters plots for Sales by Game
fig = px.scatter(filtered_sales_df, x="Name", y="Global_Sales", title="Sales by Game")
plotly(fig)





