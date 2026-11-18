# rq1.py 
import pandas as pd
import plotly.express as px

def analyze_nationalities_over_time(df):
    """
    Analyze which nationalities have shown an increase in Nobel Prize winners over time.
    """
    # Keep only needed columns
    data = df[['birth_countrynow', 'awardyear']].copy()
    
    # Convert awardyear to numeric
    data['awardyear'] = pd.to_numeric(data['awardyear'], errors='coerce')
    data = data.dropna()
    
    # Create decade column
    data['decade'] = (data['awardyear'] // 10) * 10
    data['decade_str'] = data['decade'].astype(str) + 's'
    
    # Count winners per nationality per decade
    nationality_counts = data.groupby(['birth_countrynow', 'decade_str']).size().reset_index()
    nationality_counts.columns = ['nationality', 'decade', 'count']
    
    return nationality_counts

def plot_nationalities_over_time(df, top_n=10):
    """
    Create a bar chart showing nationalities with Nobel Prize winners over time.
    """
    # Find total winners per nationality
    total_counts = df.groupby('nationality')['count'].sum().reset_index()
    
    # Get top N nationalities
    top_nationalities = total_counts.nlargest(top_n, 'count')['nationality'].tolist()
    
    # Filter for only top nationalities
    filtered_df = df[df['nationality'].isin(top_nationalities)]
    filtered_df = filtered_df.sort_values('decade')
    
    # Create bar chart
    fig = px.bar(
        filtered_df,
        x='decade',
        y='count',
        color='nationality',
        title=f'Top {top_n} Nationalities of Nobel Prize Winners Over Time',
        labels={'decade': 'Decade', 'count': 'Number of Winners', 'nationality': 'Nationality'},
        barmode='group'
    )
    
    # Update layout
    fig.update_layout(
        template='plotly_white',
        xaxis_tickangle=0,
        height=550,
        width=900,
        legend_title='Nationality',
        margin=dict(l=20, r=20, t=50, b=20)
    )
    
    return fig