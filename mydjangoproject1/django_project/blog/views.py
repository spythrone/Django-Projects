from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'book' : 'Sapiens',
        'author' : 'Yuval Noah Harari',
        'price'  :   '200'
    },
    {
        'book' : 'One Up On The Wall Street',
        'author' : 'Peter Lynch',
        'price'  :   '150',
    },
]


def home(request):
    context = {
        'posts' : posts,
    }
    return render(request, template_name='blog/home.html', context=context)

def about(request):
    context = {
        'title' : 'About',
    }
    return render(request, template_name='blog/about.html', context=context)