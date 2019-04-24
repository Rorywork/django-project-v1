from django.shortcuts import render

# Create your views here.

def get_allCheepees(request):
    return render(request, "allCheepees.html")
