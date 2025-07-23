from django.shortcuts import render
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

def home(request):
    return render(request, "main/home.html")

def about(request):
    return render(request, "main/about.html")

def contact(request):
    return render(request, "main/contact.html")

def scraping(request):
    context = {
        'url': '',
        'html_scrape': None,
        'form_count': 0,
        'form_id':[]
    }

    if request.method == 'POST':
        url = request.POST.get('url')
        try:
            page = urlopen(url)
            html_bytes = page.read()
            html_scrape = html_bytes.decode("utf-8")

            soup = BeautifulSoup(html_scrape, 'html.parser')
            forms = soup.find_all('form')

            form_id = []
            for form in forms:
                if form.get('id'):
                    form_id.append(f"id: {form.get('id')}")
                elif form.get('action'):
                    form_id.append(f"action: {form.get('action')}")
                else:
                    form_id.append("brak id i action")
                

            context['url'] = url
            context['html_scrape'] = html_scrape
            context['form_count'] = len(forms)
            context['form_id'] = form_id


        except (HTTPError, URLError) as e:
            context['html_scrape'] = f"Błąd: {e}"

    return render(request, "main/scraping.html", context)

