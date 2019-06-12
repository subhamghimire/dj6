from django.shortcuts import render
# from userapp.models import User
from userapp.forms import NewUserForm
# Create your views here.

def index(request):
    return render(request,'index.html')


def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            #this take back to you index page
            return index(request)
        else:
            print('Error form is invalid')

    return render(request,'users.html',{'form':form})
