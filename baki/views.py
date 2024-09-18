from django.shortcuts import render

# Create your views here.
def home(request): 
    return render(request, 'home.html', {'page_title': "Home"})

def about(request): 
    return render(request, 'about.html', {'page_title': "About Baki"})

def live(request): 
    return render(request, 'live.html', {'page_title': "Live Stream"})