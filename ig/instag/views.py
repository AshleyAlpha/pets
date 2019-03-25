from django.shortcuts import render
from django.http  import HttpResponse
# from .forms import ProfileForm, ImageForm, CommentsForm
from django.contrib.auth.decorators import login_required
from .models import Profile, Image, Comment

def cheznous(request):
    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

        return redirect('welcome')

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})
