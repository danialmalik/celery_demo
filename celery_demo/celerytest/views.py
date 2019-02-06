from django.shortcuts import render


def index(request):
    return render(request,'index.html' ,{'response_text': 'hello'})
