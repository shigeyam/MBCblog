from django.shortcuts import render, redirect
from .models import Post, Meeting
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .forms import Commentform, ImageUploadForm, MeetingForm

def frontpage(request):
    return render(request, "blog/frontpage.html")

def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts": posts})

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == "POST":
        form = Commentform(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("post_detail", slug=post.slug)
    else:
        form = Commentform()
    
    return render(request, "blog/post_detail.html", {"post": post, "form": form})

def mba_class(request):
    return render(request, "blog/mba_class.html")

def excel_class(request):
    return render(request, "blog/excel_class.html")

def commentpage(request):
    return render(request, "blog/commentpage.html")

class ImageUploadView(CreateView):
    template_name = "blog/image-upload.html"
    form_class = ImageUploadForm
    success_url = "/"

def commentpage(request):
    post = Meeting.objects.all()
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            meeting = form.save(commit=False)
            meeting.post = post
            meeting.save()
            return redirect("/commentpage")
    else:
        form = MeetingForm()
    
    return render(request, "blog/commentpage.html", {"post": post, "form": form})



