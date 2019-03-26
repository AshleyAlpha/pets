from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from .forms import ProfileForm, PicForm
from .models import Profile, Image, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required(login_url='/accounts/login/')
def cheznous(request):
    images = Image.objects.all()
    return render(request,'index.html',{"images":images})

@login_required(login_url='/accounts/login/')
def images(request,image_id):
    image = Image.objects.get(id = image_id)
    return render(request,"info.html", {"image":image})

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