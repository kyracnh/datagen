from django.shortcuts import render
from .forms import SearchForm
from .models import search_do
from .forms import BusinessPromptForm
from .utils import fetch_competitors, analyze_data, create_line_chart
from django.shortcuts import render, redirect
from django.contrib import messages
import json

def search_results(request):
    query = request.GET.get('query', '')  # Get the search query from the GET parameters
    results = search_do.objects.filter(name__icontains=query)  # Filter based on query

    print("result:", results )

    # Prepare data for the chart
    chart_data = {
        'labels': [item.name for item in results],
        'data': [item.score for item in results],
    }

    # Sample market data
    market_size_data = [150, 120, 80]
    market_trends_data = [5, 10, 15, 25]

    return render(request, 'search_results.html', {
        'query': query,
        'results': results,
        'chart_data': chart_data,
        'market_size_data': market_size_data,
        'market_trends_data': market_trends_data,
    })


def generate_data(request):
    if request.method == 'POST':
        print(request.POST)
        form = BusinessPromptForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']
            
            # Debugging the sample data
            data = [
                {"Competitor Name": "Competitor A", "Popularity (Score)": 85},
                {"Competitor Name": "Competitor B", "Popularity (Score)": 75},
                {"Competitor Name": "Competitor C", "Popularity (Score)": 90},
                {"Competitor Name": "Competitor D", "Popularity (Score)": 65},
                {"Competitor Name": "Competitor E", "Popularity (Score)": 80},
            ]
            print("Chart Data:", data)
            
            chart = create_line_chart(data)  # Generate chart JSON
            request.session['chart'] = chart  # Store chart in session
            
            return redirect('search_results.html')
        else:
            print("Form validation failed.")
    else:
        form = BusinessPromptForm()
    return render(request, 'search_results.html', {'form': form})

def search_view(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['query']
            return redirect('search_results')  # Redirect to results page with the search query
    else:
        form = SearchForm()

    return render(request, 'search/search_page.html', {'form': form})

def result_view(request):
    chart = request.session.get('chart', None)
    if not chart:
        print("Chart not found in session. Redirecting to form.")
        return redirect('/')
    
    # Ensure chart JSON is passed to the template
    return render(request, 'search_results.html', {'chart_data': chart})

from django.http import HttpResponseRedirect
from django.urls import reverse

def search(request):
    if request.method == "POST":
        prompt = request.POST.get("prompt")  # Get the query from the form
        api_key = "18855a38c90993e458ee153ab366b7fcd27d0b23"
        url = "https://api.serper.dev/search"

        # Define the payload
        payload = {
            "q": prompt,
            "gl": "us",  # Geolocation
            "hl": "en",  # Language
        }

        # Make the API call
        headers = {
            "X-API-KEY": api_key,
            "Content-Type": "application/json",
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            data = response.json()
            # Extract relevant data for the chart
            results = [
                {"title": item["title"], "link": item["link"]}
                for item in data.get("organic", [])
            ]
            # After handling the POST, redirect to prevent resubmission
            return HttpResponseRedirect(reverse('search_results', kwargs={'prompt': prompt, 'results': results}))

        else:
            # Handle error gracefully
            return render(request, "search_results.html", {"error": "Failed to fetch results."})

    return render(request, "search.html")