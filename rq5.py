import pandas as pd
import plotly.express as px


def get_university_counts(df, top_n=10):
    """
    This function identifies which universities are most frequently
    affiliated with Nobel Prize winners.

    The analysis is based on the primary affiliation field and counts
    how often each university appears in the dataset.
    """

    # Select the relevant column
    data = df[['affiliation_1']].copy()

    # Remove missing or unknown values
    data = data[data['affiliation_1'] != 'unknown']

    # Extract university name
    data['university'] = data['affiliation_1'].str.split(',').str[0]

    # Count number of winners per university
    university_counts = (
        data.groupby('university')
        .size()
        .reset_index(name='number_of_winners')
        .sort_values(by='number_of_winners', ascending=False)
        .head(top_n)
    )

    return university_counts


def plot_top_universities(top_df):
    """
    This function visualizes the universities with the highest
    number of Nobel Prize winners using a bar chart.
    """

    fig = px.bar(
        top_df,
        x='university',
        y='number_of_winners',
        title='Top Universities by Number of Nobel Prize Winners'
    )

    fig.update_layout(
        template='plotly_white',
        xaxis_tickangle=45,
        height=550,
        width=900
    )

    return fig
