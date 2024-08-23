from django.shortcuts import render

def home(request):
    return render(request,'django4gitactions/index.html')
