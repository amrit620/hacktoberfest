from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from .forms import Register
from django.contrib import messages

def home(request):
	post = Post.objects.all()
	context = {
		'post':post
	}
	return render(request,'home.html',context)

def user_reg(request):
	form = Register()
	if request.method == 'POST':
		form = Register(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request,'Account was successfully created for '+user)
			return redirect('home')
	        
	context = {'form':form,}
	return render(request,'signup.html',context)


def user_login(request):
	return render(request,'login.html')