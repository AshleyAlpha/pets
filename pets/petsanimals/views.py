
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
    image = Pet.objects.filter(id = pet_id).all()

    
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

def Bookform(request,id):
        current_user = request.user
        post = Image.objects.get(id=id)
        clients = Client.objects.filter(image=post)
        if request.method == 'POST':
                form = BookingForm(request.POST,request.FILES)
                if form.is_valid():
                        client = form.cleaned_data['client']
                        new_client = Client(client = client,user =current_user,image=post)
                        new_client.save()
                    
                
        else:
                    form = BookingForm()
        return render(request, 'index.html', {"form":form})

