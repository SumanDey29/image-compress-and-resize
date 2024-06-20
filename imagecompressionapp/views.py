from django.shortcuts import render, redirect

def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')