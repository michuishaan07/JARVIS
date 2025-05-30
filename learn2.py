from googlesearch import search

import webbrowser
def google_search(query):
    for url in search(query, num_results=1):
        webbrowser.open(url)

google_search("Python programming")
