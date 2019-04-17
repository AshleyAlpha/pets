
from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from .forms import BookingForm
from .models import Pet, Client
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def cheznous(request):
    images = Pet.objects.all()
    return render(request,'index.html',{"images":images})


@login_required(login_url='/accounts/login/')
def images(request,pet_id):
    current_user = request.user
    image = Pet.objects.get(id = pet_id)
    post = Pet.objects.get(id=pet_id)
    # comment = Comment.objects.filter(id = image_id).all()
    # print(comment)
    # if request.method == 'POST':
    #     form = CommentForm(request.POST,request.FILES)
    #     if form.is_valid():
    #         comment = form.cleaned_data['comment']
    #         new_comment = Comment(comment = comment,user =current_user,image=post)
    #         new_comment.save()
                
            
    # else:
    #     form = CommentForm()
    return render(request,"picture.html", {"image":image})

def petpic(request):
    current_user = request.user
    if request.method == 'POST':
        form = PicForm(request.POST, request.FILES)
        if form.is_valid():
            picture = form.save(commit=False)
            picture.user = current_user
            picture.save()

    else:
        form = PicForm()
    return render(request, 'petpic.html', {"form": form})

