from django.shortcuts import render
from googleapiclient.discovery import build
from urllib.parse import urlparse
from collections import Counter

keyword_counter = Counter()

def search_google(request):
    results = []
    competitor_count = 0
    best_keywords = set()  # Use a set to avoid duplicate keywords
    query = ""
    
    if request.method == "POST":
        query = request.POST.get("query")
        api_key = "AIzaSyB9oLSWryW7NbsxL86hi5Q3dcGdU6X24wg"
        cse_id = "30d50d0ba989c41c4"
        
        # Build the Google Custom Search API client
        service = build("customsearch", "v1", developerKey=api_key)
        res = service.cse().list(q=query, cx=cse_id).execute()
        
        if "items" in res:
            import urllib.parse  # To parse URLs and extract domain names
            
            results = [
                {
                    "name": urllib.parse.urlparse(item["link"]).netloc,  # Extracts domain name
                    "link": item["link"]
                }
                for item in res["items"][:5]
            ]
            
            # Extract keywords from snippets
            for item in res["items"]:
                snippet = item.get("snippet", "")  # Get the snippet text
                if snippet:
                    words = snippet.split()  # Split the snippet into words
                    # Filter and clean the words
                    cleaned_keywords = [
                        word.strip(".,!?:;").lower() for word in words if len(word) > 3
                    ]
                    keyword_counter.update(cleaned_keywords)
                    best_keywords.update(cleaned_keywords)
            best_keywords = [keyword for keyword, count in keyword_counter.most_common(10)]
            competitor_count = len(results)  # Number of competitors found
    
    return render(request, "scraper/results.html", {
        "query": query,
        "results": results,
        "competitor_count": competitor_count,
        "best_keywords": ", ".join(best_keywords),  # Join keywords into a single string
    })
