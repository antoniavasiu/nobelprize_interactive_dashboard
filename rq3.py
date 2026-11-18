import pandas as pd
import plotly.express as px
import data_modelling as dm

nobel_dataset = pd.read_csv("nobel_dataset.csv")
nobel_dataset = dm.clean_data(nobel_dataset)

#Q3:How has the number of women Nobel Prize winners changed across the decades?
def count_women_winners_per_decade(data: pd.DataFrame) -> pd.DataFrame:
    """
    Count the number of women Nobel Prize winners per decade.
    Filter the dataset to include only women (using the 'gender' column),
    Compute the decade from the 'awardyear' column
    Returns counts in '1910s' format.
    """
    
    # keep only gender and award year
    data = data[["gender", "awardyear"]].copy()
    # doesnt count unknown 
    data = data[data["gender"]!= "unknown"]
    # filter only women
    women = data[data["gender"] == "female"].copy() #make a copy of this slice to avoid SettingWithCopyWarning
    # create new column decade and calculate it as integer
    women["decade"] = (women["awardyear"] // 10) * 10 
    # convert dacade to string format like "1910s"
    women["decade"] = women["decade"].astype(str) + "s"
    # initialize an empty dictionary to store counts
    decade_counts_dict = {}
    # loop through each decade value in the women DataFrame 
    # count occurrences per decade
    for decade in women["decade"]:
        if decade in decade_counts_dict:
            decade_counts_dict[decade] += 1
        else:
            decade_counts_dict[decade] = 1
    # convert to DataFrame
    decade_counts = pd.DataFrame(
     list(decade_counts_dict.items()),
     columns=["decade", "count"]
    ).sort_values(by="decade")

    return decade_counts

def gender_counts_per_decade(data: pd.DataFrame) -> pd.DataFrame:
    """
    Count Nobel Prize winners by gender for each decade and compute gender percentages.
    Filters the dataset to include only male and female winners.
    Groups winners by decade.
    Computes absolute numbers and percentages for each gender per decade.
    Return a dataframe cotaining absolute counts and the percentage shares by gender and decade.
    """
    data = data.copy()
    data = data[["gender", "awardyear"]]
    data["gender"] = data["gender"].str.lower().str.strip()
    data = data[data["gender"].isin(["male", "female"])] 
    data["decade"] = (data["awardyear"] // 10 * 10).astype(str) + "s"

    # build counts dataframe 
    gender_percentages = (
        data.groupby(["decade", "gender"])
        .size() 
        .unstack(fill_value=0) 
        .reset_index()
        .sort_values("decade")
        .rename(columns={"male": "men_count", "female":"women_count"})
    )

    # then compute percentage
    gender_percentages["total"] = gender_percentages["men_count"] + gender_percentages["women_count"]
    
    gender_percentages["Male"] = gender_percentages["men_count"] / gender_percentages["total"] * 100
    gender_percentages["Female"] = gender_percentages["women_count"] / gender_percentages["total"] * 100

    return gender_percentages

### Research Question 3:
### How has the number of women Nobel Prize winners changed across the decades?
### We will define a function to plot the counts of women Nobel Prize winners per decade
### The function will take as input a pandas DataFrame "df_decade_counts"

### It will return a px.plotly figure object
### The function will use plotly to visualize the progression of women Nobel Prize winners across decades
### The function will set appropriate titles and labels for the plot and use markers to highlight data points

def plot_women_per_decade(df_decade_counts: pd.DataFrame) -> px:
    """
    Plots the number of female Nobel Prize winners per decade.
    Returns a Plotly graph line figure.
    """
    # Line chart fo women winners by decade
    fig = px.line(
        df_decade_counts,
        x="decade",
        y="count",
        labels={"decade": "Decade", "count": "Number of Women Winners"},
        title="Progression of Women Nobel Prize Winners per Decade(excluding unknowns)",
        markers= True, 
    )
    # Customize the line and the markers for readability
    fig.update_traces(
        line= dict(dash= "solid",width=3, color="red"),
        marker=dict(symbol="diamond", size=8,color="black" )
    )
    # Apply a clean white theme and adjust figure dimesions
    fig.update_layout(
        template= "plotly_white", 
        xaxis=dict(type="category"), 
        height=600,
        width=900,
        margin=dict(l=20, r=20, t=50, b=20),
        showlegend=False,
    )
    return fig

### We will define a function to plot the percentages between men and women Nobel Prize winners per decade
### The function will take as input a pandas DataFrame "gender_percentages"

### It will return a px.plotly figure object
### The function will use plotly to visualize the comparison between men and women Nobel Prize winner across decades counted on percentages
### The function will set appropriate titles and labels for the plot and use markers to highlight data points

def plot_men_vs_women(gender_percentages: pd.DataFrame) -> px:
    """
    Plots men vs women Nobel Prize winners per decade on percentages.
    Return a Plotly graph line figure
    """
    # Create a line chart with seperate lines for men and women
    fig2 = px.line(
        gender_percentages,
        x="decade",
        y=["Male", "Female"],
        markers=True,
        title="Men vs Women Nobel Prize Winners per Decade (%) (excluding unknowns)",
        labels={
            "decade": "Decade",
            "value": "Percentage of Winners",
            "variable": "Gender",
        },
    )
    # Increase line and marker size for better readability
    fig2.update_traces(line=dict(width=3), marker=dict(size=9))
    # Apply a clean white theme and adjust figure dimesions
    fig2.update_layout(
        template="plotly_white",
        width=900,
        height=550,
        legend_title_text="Gender",
    )

    return fig2


   