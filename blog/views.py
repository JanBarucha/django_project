from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author' : 'J_junior',
        'title' : 'Blog post 1',
        'content' : 'First post content',
        'date_posted' : ' August 25, 2022'
    },
    {
        'author': 'J_junior_second_post',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': ' August 27, 2022'
    }
]


# Create your views here.
def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)



def about(request):
    return render(request, 'blog/about.html', { 'title' : 'About' })
