from django.shortcuts import get_object_or_404, redirect, render
from.models import Post
from.forms import CommentForm

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('Post_detail', slug = slug)
    else:
        form = CommentForm()
    return render(request, 'alaye_blog/detail.html', {'post':post, 'form':form})
