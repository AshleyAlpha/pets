from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from .forms import ProfileForm, PicForm,CommentForm,LikeForm
from .models import Profile, Image, Comment,Like
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='/accounts/login/')
def cheznous(request):
    images = Image.objects.all()
    return render(request,'index.html',{"images":images})

@login_required(login_url='/accounts/login/')
def images(request,image_id):
    image = Image.objects.get(id = image_id)
    comment = Comment.objects.filter(id = image_id).all()
    print(image.image.url)
    form = CommentForm()
    return render(request,"img.html", {"form": form,"image":image,"comment":comment})

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

        return redirect(cheznous)

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def theProfile(request,id):
    user = User.objects.get(id = id)
    profiles = Profile.objects.get(user = user)
   
    return render(request,'theProfile.html',{"profiles":profiles,"user":user})

def picture(request):
    current_user = request.user
    if request.method == 'POST':
        form = PicForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.user = current_user
            picture.save()

    else:
        form = PicForm()
    return render(request, 'picture.html', {"form": form})

def comments(request,id):
        current_user = request.user
        post = Image.objects.get(id=id)
        comments = Comment.objects.filter(image=post)
        if request.method == 'POST':
                form = CommentForm(request.POST,request.FILES)
                if form.is_valid():
                        comment = form.cleaned_data['comment']
                        new_comment = Comment(comment = comment,user =current_user,image=post)
                        new_comment.save()
                    
                
        else:
                    form = CommentForm()
        return render(request, 'img.html', {"form":form,'post':post,'user':current_user,'comments':comments})


def like(request):
    current_user = request.user
    if request.method == 'POST':
        form = LikeForm(request.POST, request.FILES)
        if form.is_valid():
            likes = form.save(commit=False)
            likes.user = current_user
            likes.save()

            return redirect(home)

    else:
        form = LikeForm()
    return render(request, 'like.html', {"form": form})
