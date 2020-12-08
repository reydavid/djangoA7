from django.shortcuts import render,redirect,HttpResponse
from .models import User

# Create your views here.

def index(request):
    context = {
        "allusers": User.objects.all()
    }
    return render(request,'form_app/index.html',context)

def addUser(request):
    #if request.method == 'POST':
    name = request.POST['name']
    height = request.POST['height']
    weight = request.POST['weight']
    diet = request.POST['diet']

    user = User.objects.create(name = name, height = height, weight= weight, diet = diet)
    
    print('\n\n',request.User,'\n\n')

    return redirect('/')