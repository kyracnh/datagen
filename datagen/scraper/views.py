from django.shortcuts import render
from googleapiclient.discovery import build

def search_google(request):
    results = []
    query = ""
    if request.method == "POST":
        query = request.POST.get("query")
        api_key = "AIzaSyB9oLSWryW7NbsxL86hi5Q3dcGdU6X24wg"
        cse_id = "30d50d0ba989c41c4"
        
        # Build the Google Custom Search API client
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=query, cx=cse_id).execute()
        
        if "items" in res:
            results = res["items"]
    
    return render(request, "scraper/results.html", {"query": query, "results": results})
