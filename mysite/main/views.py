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
        'form_count': 0,
        'form_identifiers': [],
        'selected_form_html': None,
    }

    if request.method == 'POST':
        url = request.POST.get('url')
        selected_form_index = request.POST.get('selected_form_index')

        try:
            page = urlopen(url)
            html_bytes = page.read()
            html_scrape = html_bytes.decode("utf-8")

            soup = BeautifulSoup(html_scrape, 'html.parser')
            forms = soup.find_all('form')

            form_identifiers = []
            for i, form in enumerate(forms):
                if form.get('id'):
                    form_identifiers.append((i, f"id: {form.get('id')}"))
                elif form.get('action'):
                    form_identifiers.append((i, f"action: {form.get('action')}"))
                else:
                    form_identifiers.append((i, "brak id i action"))

            context['url'] = url
            context['form_count'] = len(forms)
            context['form_identifiers'] = form_identifiers

            if selected_form_index is not None:
                try:
                    index = int(selected_form_index)
                    context['selected_form_html'] = forms[index].prettify()
                except (IndexError, ValueError):
                    context['selected_form_html'] = "Nieprawidłowy formularz."

        except (HTTPError, URLError) as e:
            context['selected_form_html'] = f"Błąd: {e}"

    return render(request, "main/scraping.html", context)
