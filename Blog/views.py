from django.contrib.auth.models import User
from Blog import models
from .models import Post
from .forms import PostForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages  
from .models import UserProfile  
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .forms import UserUpdateForm, UserProfileUpdateForm
from django.shortcuts import render, get_object_or_404, redirect


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')

        # Check if the username already exists
        if User.objects.filter(username=name).exists():
            messages.error(request, "Username already taken. Please choose another.")
            return render(request, 'Blog/signup.html')

        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered. Please use a different email or login.")
            return render(request, 'Blog/signup.html')

        newUser = User.objects.create_user(username=name, email=email, password=password)
        newUser.save()

        messages.success(request, "Account created successfully! Please log in.")
        return redirect('/loginn')

    return render(request, 'Blog/signup.html')



def loginn(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        profile_pic = request.FILES.get('profile_pic')  
        
        userr = authenticate(request, username=name, password=password)
        if userr is not None:
            login(request, userr)
            
            profile, created = UserProfile.objects.get_or_create(user=userr)
            if profile_pic:
                profile.profile_picture = profile_pic
                profile.save()
            
            return redirect('/home')
        else:
            return redirect('/login')

    return render(request, 'Blog/login.html')



def home(request):
    # Order the posts list by 'date_posted' in descending order (most recent posts first)
    posts_list = Post.objects.all().order_by('-date_posted')
    paginator = Paginator(posts_list, 5)  # Show 5 posts per page

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    context = {
        'posts': posts
    }
    return render(request, 'Blog/home.html', context)


def newPost(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        npost = models.Post(title=title, content=content, author=request.user)
        npost.save()
        return redirect('/home')
    
    return render(request, 'Blog/newpost.html')


def myPost(request):
    context = {
        'posts': Post.objects.filter(author= request.user)
    }
    return render(request, 'Blog/mypost.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  
    context = {
        'post': post
    }
    return render(request, 'Blog/post_detail.html', context)

@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Only the author can edit the post
    if post.author != request.user:
        return redirect('home')

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=post.pk)  # redirect to post-detail
    else:
        form = PostForm(instance=post)

    return render(request, 'Blog/postforms.html', {'form': form, 'post': post})




@login_required
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Only the author can delete the post
    if post.author != request.user:
        messages.error(request, "You are not authorized to delete this post.")
        return redirect('home')

    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post has been deleted successfully.")
        return redirect('home')

    return render(request, 'Blog/postdelete.html', {'post': post})



def myProfile(request):
    return render(request, 'Blog/myprofile.html')


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('my-profile')  
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileUpdateForm(instance=request.user.userprofile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'Blog/update_profile.html', context)


@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Your profile has been successfully deleted.')
        return redirect('home')

    return render(request, 'Blog/delete_profile_confirm.html')


def signout(request):
    logout(request)
    return redirect('/loginn')