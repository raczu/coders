from django.shortcuts import render, redirect


# Create your views here.
def challengesView(request):
    return render(request, 'challenges/challenges.html')