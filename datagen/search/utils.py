import requests
import pandas as pd
import plotly.express as px
import json

def fetch_competitors(prompt):
    api_url = "https://www.googleapis.com/customsearch/v1"  # Replace with the actual API URL
    params = {"query": prompt,
              "api_key": "AIzaSyB9oLSWryW7NbsxL86hi5Q3dcGdU6X24wg",
              "cx": "30d50d0ba989c41c4",
              }  # Add your API key here
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return response.json()  # Assuming the API returns JSON
    return []

def analyze_data(data):
    df = pd.DataFrame(data)  # Convert data to a DataFrame
    # Example: Group competitors by their rating
    grouped_data = df.groupby('rating').size().reset_index(name='count')
    return grouped_data

def create_line_chart(data):
    import plotly.express as px
    import json

    fig = px.line(
        data,
        x='Competitor Name', 
        y='Popularity (Score)',
        title='Competitor Popularity over Time',
        labels={'Popularity (Score)': 'Popularity Score'},
    )
    fig.update_layout(template='plotly_white')

    return json.dumps(fig, cls=px.utils.PlotlyJSONEncoder)