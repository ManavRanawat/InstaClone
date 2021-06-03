from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import pickle



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            
            form.save()
            username = form.cleaned_data.get('username')
            
            user = User.objects.filter(username=username)
            Profile.objects.create(user=user.first())

            messages.success(request,f'Account created for {username}')
            return redirect('login')
        
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})



@login_required
def profile(request):
    
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES ,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request,f'Profile Updated for {username}')
            return redirect('profile')
        
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request, 'users/profile.html', context)