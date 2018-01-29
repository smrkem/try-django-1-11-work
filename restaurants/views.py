from django.shortcuts import render
from django.views import View

# Create your views here.
def home(request):
    return render(request, 'home.html', {"myvar": "Slippery Pete"})

class ContactView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contact.html', {})
