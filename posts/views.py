"""Posts views."""

# Django
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

# Model 
from posts.models import Post

# Forms
from posts.forms import CommentForm


def list_posts(request):
    """List existing posts."""

    query = request.GET.get('q')
    paginate_by = 6

    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(labels__icontains=query) 
        ).distinct()
    else:
        posts = Post.objects.all().order_by('-created')

    paginator = Paginator(posts, paginate_by)

    page_number = request.GET.get('page')
    page_objects = paginator.get_page(page_number)

    return render(request, 'posts/list_posts.html', {'page_objects': page_objects})


def detail_post(request, pk):
    """Detail Post."""

    post = Post.objects.get(pk=pk)

    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.save()
        comment_form = CommentForm()
        
    return render(
        request, 
        'posts/detail_post.html', 
        {
            'post': post,
            'form': comment_form
        }
    )


