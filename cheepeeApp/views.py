from django.shortcuts import render, redirect, get_object_or_404
from .models import Cheepee

# Create your views here.

def get_allCheepees(request):
    # return render(request, "allCheepees.html")
    results = Cheepee.objects.all()
    return render(request,"allCheepees.html",{'cheepees': results})
