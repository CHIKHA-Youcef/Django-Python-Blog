from datetime import date
from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "slug":"hike-mont",
        "image":"sand.jpg",
        "author":"Youcef",
        "date":date(2022, 2, 21),
        "title":"Mount hiki",
        "excerpt":"Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences",
        "content":"""
            Paragraphs are the building blocks of papers.
            Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences,
            a paragraph is half a page long, etc. In reality, though, 
            the unity and coherence of ideas among sentences is what constitutes a paragraph. A paragraph is defined as “a group
            of sentences or a single sentence that forms a unit” (Lunsford and Connors 116). Length and appearance do not determine
            whether a section in a paper is a paragraph. For instance, in some styles of writing, particularly journalistic styles,
            a paragraph can be just one sentence long. Ultimately, a paragraph is a sentence or group of sentences that support one main
            idea. In this handout, we will refer to this as the “controlling idea,”
            because it controls what happens in the rest of the paragraph.
        """
    },
    {
        "slug":"django",
        "image":"city.jpg",
        "author":"Youcef",
        "date":date(2021, 7, 12),
        "title":"Django",
        "excerpt":"Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences",
        "content":"""
            Paragraphs are the building blocks of papers.
            Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences,
            a paragraph is half a page long, etc. In reality, though, 
            the unity and coherence of ideas among sentences is what constitutes a paragraph. A paragraph is defined as “a group
            of sentences or a single sentence that forms a unit” (Lunsford and Connors 116). Length and appearance do not determine
            whether a section in a paper is a paragraph. For instance, in some styles of writing, particularly journalistic styles,
            a paragraph can be just one sentence long. Ultimately, a paragraph is a sentence or group of sentences that support one main
            idea. In this handout, we will refer to this as the “controlling idea,”
            because it controls what happens in the rest of the paragraph.
        """
    },
    {
        "slug":"python",
        "image":"my.jpg",
        "author":"Youcef",
        "date":date(2022, 4, 6),
        "title":"Python",
        "excerpt":"Paragraphs are the building blocks of papers. Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences",
        "content":"""
            Paragraphs are the building blocks of papers.
            Many students define paragraphs in terms of length: a paragraph is a group of at least five sentences,
            a paragraph is half a page long, etc. In reality, though, 
            the unity and coherence of ideas among sentences is what constitutes a paragraph. A paragraph is defined as “a group
            of sentences or a single sentence that forms a unit” (Lunsford and Connors 116). Length and appearance do not determine
            whether a section in a paper is a paragraph. For instance, in some styles of writing, particularly journalistic styles,
            a paragraph can be just one sentence long. Ultimately, a paragraph is a sentence or group of sentences that support one main
            idea. In this handout, we will refer to this as the “controlling idea,”
            because it controls what happens in the rest of the paragraph.
        """
    },
]


def get_date(post):
    return post["date"]

def index(req):
    stored_list = sorted(posts, key=get_date)
    return render(req, 'blog/index.html', {
        "posts":stored_list[-3:]
    })

def all_posts(req):
    return render(req, 'blog/all-posts.html',{
        'posts':posts,
    })

def post_detail(req, slug):
    thepost = next(post for post in posts if post["slug"] == slug)
    return render(req, 'blog/post-detail.html', {
        "post":thepost
    })




