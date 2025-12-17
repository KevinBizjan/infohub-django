from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Post, Category
from .forms import PostForm, RegisterForm, ContactForm


def home(request):
    posts = Post.objects.filter(is_active=True).order_by('-created_at')
    categories = Category.objects.all()
    return render(request, 'core/home.html', {
        'posts': posts,
        'categories': categories
    })


def posts_by_category(request, category_id):
    order = request.GET.get('order', 'desc')

    if order == 'asc':
        posts = Post.objects.filter(
            category_id=category_id,
            is_active=True
        ).order_by('created_at')
    else:
        posts = Post.objects.filter(
            category_id=category_id,
            is_active=True
        ).order_by('-created_at')

    categories = Category.objects.all()
    category = get_object_or_404(Category, id=category_id)

    return render(
        request,
        'core/posts_by_category.html',
        {
            'posts': posts,
            'categories': categories,
            'category': category,
            'order': order
        }
    )

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'core/create_post.html', {
        'form': form
    })

@login_required
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user != post.author and not request.user.is_staff:
        return redirect('home')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)

    return render(request, 'core/edit_post.html', {
        'form': form
    })

@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    post.delete()
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'registration/register.html', {'form': form})

from .forms import ContactForm
from django.shortcuts import redirect
from django.contrib import messages

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.success(
                request,
                "Gracias por contactarnos. Te responderemos a la brevedad."
            )
            form = ContactForm()
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {
        'form': form
    })

def contact_success(request):
    return render(request, 'core/contact_success.html')

def about(request):
    return render(request, 'core/about.html')

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, is_active=True)
    return render(request, 'core/post_detail.html', {'post': post})


from .forms import ContactForm
