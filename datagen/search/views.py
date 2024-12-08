from django.shortcuts import render

def search_view(request):
    if request.method == 'POST':
        search_query = request.POST.get('query')
        print(search_query)
    return render(request, 'search/search_page.html')
