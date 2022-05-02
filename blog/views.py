from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
posts_list = {
    'post1':'post1',
    'post2':'post2',
    'post3':'post3',
}
def index(req):
    return render(req, 'blog/index.html')

def all_posts(req):
    return render(req, 'blog/all-posts.html',{
        'postsList':list(posts_list.keys()),
    })

def post_detail(req, post):
    return 




