# Research question 2: 

# In what ways has the typical age of Nobel Prize recipients changed throughout the decades in each category?





#import necessary libraries

import pandas as pd

import plotly.express as px



#import data cleaning module

import data_modelling as dm



# Display all rows in output

pd.set_option('display.max_rows', None)



# Load in the dataset

df = pd.read_csv("nobel_dataset.csv")

df = dm.clean_data(df)





def analyze_age_trends(df: pd.DataFrame) -> pd.DataFrame:

    """

    Analyzes average age of Nobel Prize winners over time by category.

    Returns a summary showing average age by decade and category.

    Also creates and displays line chart visualization.

    """

    # Calculate age at time of winning prize

    df['age_at_prize'] = df['awardyear'] - df['birth_year']

    

    # Create decade column for time-based analysis

    df['decade'] = (df['awardyear'] // 10) * 10

    

    # Group by decade and category, then calculate average age

    age_summary = df.groupby(['decade', 'category'])['age_at_prize'].mean()

    

    # Round to 1 decimal place for readability

    age_summary = age_summary.round(1)

    

    # Convert to DataFrame for better display

    age_summary = age_summary.reset_index()

    age_summary.columns = ['Decade', 'Category', 'Average_Age']

    

    # Create line chart visualization

    fig = px.line(age_summary, x='Decade', y='Average_Age', color='Category',

                  title='Average Age of Nobel Prize Winners Over Time by Category',

                  labels={'Average_Age': 'Average Age', 'Decade': 'Decade'})

    fig.update_layout(template='plotly_white', xaxis=dict(dtick=10))

    fig.update_traces(mode='lines+markers+text', textposition='top center')

    

    return fig











