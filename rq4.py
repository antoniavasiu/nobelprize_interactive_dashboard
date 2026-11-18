import pandas as pd
import plotly.express as px

import data_modelling as dm

df_data = pd.read_csv("nobel_dataset.csv")

def gender_distribution(data):
    counts = data.groupby(["category", "gender"]).size()
    percentages = counts / counts.sum() * 100
    df_column = counts.reset_index()
    df_column.columns = ["category", "gender", "count"]
    visualization = px.bar(
    df_column,
    x="category",
    y="count",
    color="gender",
    barmode="group",
    title="Gender Distribution by Nobel Prize Category: "
    )


    return visualization


    #return counts
#gender_distribution(df_data)
#result = gender_distribution(df_data)



#print(result)

#print(type(result))

# Interesting fact: Each unknown value is the gender of the peace winners. 
# Otherwise, there is no other unknown data. Each entry has a category attributed to it
"""
result_df = result.reset_index()
result_df.columns = ["category", "gender", "count"]

fig = px.bar(
    result_df,
    x="category",
    y="count",
    color="gender",
    barmode="group",
    title="Gender Distribution by Nobel Prize Category"
)

fig.show()

"""