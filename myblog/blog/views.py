from django.core.context_processors import csrf
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from blog.models import Post, Author, Comment
from django.forms import ModelForm
from django import http
from django.http import HttpResponseRedirect



class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]

def add_comment(request, pk):
    """Add a new comment."""
    p = request.POST

    if p.has_key("body") and p["body"]:
        author = "Anonymous"
        if p["author"]: author = p["author"]

        comment = Comment(post=Post.objects.get(pk=pk))
        cf = CommentForm(p, instance=comment)
        cf.fields["author"].required = False

        comment = cf.save(commit=False)
        comment.author = author
        comment.save()
    return HttpResponseRedirect(reverse("blog.views.post", args=[pk]))


def index(request):   
    posts = Post.objects.all().order_by('-date')
    paginator = Paginator(posts, 2)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage, EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response("index.html", dict(posts=posts, user=request.user))

def about(request):
    return render_to_response('about.html')

def resume(request):
    return render_to_response('resume.html')

def contactus(request):
    return render_to_response('contactus.html')

def home(request):
    return render_to_response('home.html')


def post(request, pk):
    post = Post.objects.get(pk=int(pk))
    comments = Comment.objects.filter(post=post)
    d = dict(post=post, user=request.user)
    d.update(csrf(request))
    return render_to_response("post.html", d)


  
