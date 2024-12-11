from django.shortcuts import render
from .forms import SearchForm
from .models import search_do

def search_view(request):
    if request.method == 'GET':
        search_query = request.POST.get('query')
        print(search_query)
    form = SearchForm()
    return render(request, 'search/search_page.html', {'form': form})

def search_results(request):
    market_size_data = [150, 120, 80]
    market_trends_data = [5, 10, 15, 25]
    query = request.GET.get('query', '')
    results = search_do.objects.filter(name__icontains=query)
    chart_data = {
        'labels' : [item.name for item in results],
        'data' : [item.score for item in results]
    }
    return render(request, 'search_results.html', {
        'query': query,
        'results': results,
        'chart_data' : chart_data,
        'market_size_data': market_size_data,
        'market_trends_data': market_trends_data
        })
