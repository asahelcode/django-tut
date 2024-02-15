from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
  all_post = Post.objects.all()

  context = {
    "allpost": all_post
  }

  return render(request, "base.html", context)