from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html");

def plan(request):
    return render(request, "plan.html");

def improvement(request):
    return render(request, "improvement.html");

def book(request):
    return render(request, "book.html");