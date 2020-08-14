from django.shortcuts import render


posts = [
    {
        'author' : 'Paramveer',
        'title' : 'Blog Post 1',
        'content' : 'First Post Content',
        'date_posted' : 'August 14, 2020',
    },
    {
        'author' : 'Mukul',
        'title' : 'Blog Post 2',
        'content' : 'Second Post Content',
        'date_posted' : 'August 14, 2020',
    }

]


# Create your views here.

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title' : 'About'})      # No need to create context. we can pass dictionary directly