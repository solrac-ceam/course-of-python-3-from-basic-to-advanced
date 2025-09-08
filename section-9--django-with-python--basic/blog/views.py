from django.http import Http404
from django.shortcuts import render

from blog.data import posts


# Create your views here.
def index(request):
    context = {
        "head_title": "Blog - ",
        "text": "Blog",
        "posts": posts,
    }
    return render(request, "blog/index.html", context)


def example_view(request):
    context = {
        "head_title": "Example - ",
        "text": "Example page",
    }
    return render(request, "blog/example.html", context)


def post(request, post_id):
    found_post = None

    for post in posts:
        if post["id"] == post_id:
            found_post = post
            break
    
    if not found_post:
        raise Http404("Post not found")
    
    context = {
        "head_title": f"{found_post['title']} - ",
        "post": found_post,
    }
    return render(request, "blog/post.html", context)
