# Create your views here.
from django.shortcuts import get_object_or_404, render, HttpResponse

from myapp.form import ReviewForm
from .models import Post, Review
# Create your views here.


def index(request):
    posts = Post.objects.all()
    reviews = Review.objects.all().order_by('-date')
    return render(request, 'html/index.html', {'posts': posts, 'reviews': reviews})


def submit_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ReviewForm()
    return render(request, 'html/submit_review.html', {'form': form})


def about(request):
    return render(request, './html/about.html')


def contact(request):
    return render(request, './html/form.html')


def gallery(request):
    return render(request, './html/gallery.html')


def footer(request):
    return render(request, './html/footer.html')


def header(request):
    return render(request, './html/header.html')


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, './html/post_detail.html', {'post': post})
