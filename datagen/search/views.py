from django.shortcuts import render
from .forms import SearchForm
from .models import search_do
import openai
print(openai.__version__)
import os
#from django.http import JsonResponse
#from django.conf import settings

def search_view(request):
    if request.method == 'GET':
        search_query = request.POST.get('query')
        print(search_query)
    form = SearchForm()
    return render(request, 'search/search_page.html', {'form': form})

def get_results(request):
    if request.method == "POST":
        # Get the prompt from the form
        user_prompt = request.POST.get("prompt")

        # Query the ChatGPT API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_prompt}
            ]
        )

        # Process the API response
        related_data = extract_data(response.choices[0].message['content'])

        # Render the result page with the data
        return render(request, "search_results.html", {"related_data": related_data})

def extract_data(chat_response):
    """
    Custom function to parse ChatGPT's response and extract relevant data
    for the chart.
    """
    # For demonstration, assume chat_response is JSON-like
    # Replace with your actual parsing logic
    return [
        {"label": "Category A", "value": 35},
        {"label": "Category B", "value": 25},
        {"label": "Category C", "value": 20},
        {"label": "Category D", "value": 20}
    ]

openai.api_key = os.getenv("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")