from django.shortcuts import render
from userapp.models import User
# Create your views here.

def index(request):
    return render(request,'index.html')


def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request,'users.html',context=user_dict)
