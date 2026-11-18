
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

### Loading all research questions modules

import data_modelling as dm 
import rq1 as vis_rq1
import rq2 as vis_rq2
import rq3 as vis_rq3
import rq4 as vis_rq4
import rq5 as vis_rq5

#load dataset
nobel_dataset = pd.read_csv("nobel_dataset.csv")

#clean dataset 
nobel_dataset = dm.clean_data(nobel_dataset)

nationality_data = vis_rq1.analyze_nationalities_over_time(nobel_dataset)
women_count = vis_rq3.count_women_winners_per_decade(nobel_dataset)
gender_percentages = vis_rq3.gender_counts_per_decade(nobel_dataset)
university_counts = vis_rq5.get_university_counts(nobel_dataset)



# call visualizations
# Default values

title_rq1 = "RQ1: Which nationalities have shown an increase in Nobel Prize winners over time?"
text_rq1 = "This analysis explores the frequency of different nationalities among Nobel Prize winners over time."
fig_rq1 = vis_rq1.plot_nationalities_over_time(nationality_data,top_n=10)
rq1_plot_id = "Nationalities-plot"

title_rq2 = "RQ2: In what ways has the typical age of Nobel Prize recipients changed throughout the decades in each category?"
text_rq2 = "This analysis examines how the age of Nobel Prize winner has evolved over the decades per category"
fig_rq2 = vis_rq2.analyze_age_trends(nobel_dataset)
rq2_plot_id = "Age per category-plot"

title_rq3 = "RQ3: How has the number of women Nobel Prize winners changed across the decades?"
text_rq3 = "The analysis focuses on the trends in the number of women Nobel Prize winners and, furthermore, compare the percentages of male and female Nobel Prize winners over decades"
fig_r3 = vis_rq3.plot_women_per_decade(women_count)
rq3_plot_id = "Women-plot"
fig_r3i = vis_rq3.plot_men_vs_women(gender_percentages)
rq3i_plot_id = "Gender-plot-per-percentages"

title_rq4 = "RQ4 : What is the gender distribution of the Nobel Prize winners across the different prize categories?"
text_rq4 = "The analysis examines how each category varies in terms of gender distribution "
fig_r4 = vis_rq4.gender_distribution(nobel_dataset)
rq4_plot_id = "Gender-plot"

title_rq5 = "RQ5 : Which universities or institutions are affiliated with most winners?"
text_rq5 = "This analysis explores which universities or institutions provided the most Nobel Prize winners"
fig_r5 = vis_rq5.plot_top_universities(university_counts)
rq5_plot_id = "University-plot"


# Initialize Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    [
        # Dashboard Title
        html.H1(
            "The insights of Nobel Prize Data",
            className="text-center my-4",
        ),

        # Research Question 1
        dbc.Row(
            dbc.Col(
                html.H3(title_rq1, className="text-center text-primary"),
                width=12,
            ),
            className="mb-3",
        ),
        dbc.Row(
            dbc.Col(
                html.P(text_rq1, className="text-center lead"),
                width=12,
            ),
            className="mb-4",
        ),
        dbc.Row(
            dbc.Col(
                dcc.Graph(id=rq1_plot_id, figure=fig_rq1),
                width=12,
            ),
            className="mb-5",
        ),

        # Research Question 2
        dbc.Row(
            dbc.Col(
                html.H3(title_rq2, className="text-center text-primary"),
                width=12,
            ),
            className="mb-3",
        ),
        dbc.Row(
            dbc.Col(
                html.P(text_rq2, className="text-center lead"),
                width=12,
            ),
            className="mb-4",
        ),
        dbc.Row(
            dbc.Col(
                dcc.Graph(id=rq2_plot_id, figure=fig_rq2),
                width=9,
            ),
            className="mb-5",
        ),

        # Research Question 3
        dbc.Row(
            dbc.Col(
                html.H3(title_rq3, className="text-center text-primary"),
                width=12,
            ),
            className="mb-3",
        ),
        dbc.Row(
            dbc.Col(
                html.P(text_rq3, className="text-center lead"),
                width=12,
            ),
            className="mb-4",
        ),
        dbc.Row(
            dbc.Col(
            html.Div(
                [
                    html.Span(
                    "View mode:",
                    className="me-2 fw-semibold"
                ),
                dcc.RadioItems(
                    id="rq3-women_gender_switch",
                    options=[
                        {"label": "Women count per decade", "value": "count"},
                        {"label": "Men vs Women (%)", "value": "percent"},
                    ],
                    value="count",
                    inline=True,
                    labelStyle={"margin-right":"25px"},
                ),
            ],
            className="d-flex justify-content-end align-items-center"
        ),
        width=12,
    ),
    className="mb-3",
),
        dbc.Row(
            dbc.Col(
                dcc.Graph(id= "rq3-graph"),
                width=12,
            ),
            className="mb-5",
            ),

        # Research Question 4
        dbc.Row(
            dbc.Col(
                html.H3(title_rq4, className="text-center text-primary"),
                width=12,
            ),
            className="mb-3",
        ),
        dbc.Row(
            dbc.Col(
                html.P(text_rq4, className="text-center lead"),
                width=12,
            ),
            className="mb-4",
        ),
        dbc.Row(
            dbc.Col(
                dcc.Graph(id=rq4_plot_id, figure=fig_r4),
                width=12,
            ),
            className="mb-5",
        ),

        # Research Question 5
        dbc.Row(
            dbc.Col(
                html.H3(title_rq5, className="text-center text-primary"),
                width=12,
            ),
            className="mb-3",
        ),
        dbc.Row(
            dbc.Col(
                html.P(text_rq5, className="text-center lead"),
                width=12,
            ),
            className="mb-4",
        ),
        dbc.Row(
            dbc.Col(
                dcc.Graph(id=rq5_plot_id, figure=fig_r5),
                width=12,
            ),
            className="mb-5",
        ),
    ],
    fluid=True,
)

# Create callbacks for Interactivity RQ3
from dash import Input, Output


@app.callback(
    Output(component_id="rq3-graph", component_property="figure"),
    [Input(component_id="rq3-women_gender_switch",component_property= "value")],
)
def update_rq3(view):
    if view == "count":
        return fig_r3 # women count per decade
    else: 
        return fig_r3i    # men vs women percentages


if __name__ == "__main__":
    app.run(debug=True)





