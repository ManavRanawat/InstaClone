from django.http.response import Http404
from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import pickle
from django.views.generic import ListView,CreateView,DetailView
# Create your views here.

# class UserPostsListView(LoginRequiredMixin,ListView):
#     model = Post
#     context_object_name = 'posts'
#     def get_queryset(self):
#         user = User.objects.filter(username=self.kwargs['username'])
#         return Post.objects.filter(user=user)

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields = ['img','caption']
    template_name = 'posts/add_post.html'
    # redirect_url = 'profile'
    def form_valid(self,form):
        print("IN HERE")
        form.instance.user = self.request.user
        return super().form_valid(form)

# class PostDetailView(LoginRequiredMixin, DetailView):
#     model = Post
#     template_name = 'posts/view_post.html'
#     context_object_name = 'post'

#     def get_queryset(self):
#         post_id = self.kwargs['pk']
#         return Post.objects.filter(pk=post_id)

@login_required
def display_post(request,pk):
    post_id = pk
    post = get_object_or_404(Post,pk=post_id)
    context={"post":post}
    if request.method == "POST":
        #check if like or comment button is clicked
        print("LIKE:",request.POST.get('like_button'),"COMMENT:",request.POST.get('comment'))
        if request.POST.get('like_button')=="":
            #like is pressed 
            # liked = Like.objects.filter(post = post,like_by=request.user).first()
            # print("YAHA AAYA",liked)
            # if not liked:
            like = Like.objects.create(post=post,like_by=request.user)
            like.save()
        elif request.POST.get('comment')=="" and request.POST.get('comment_msg').strip()!="":
            # assert(request.POST.get('comment')!=None)
            cmt = Comment.objects.create(post=post,comment_user=request.user,comment=request.POST.get('comment_msg'))
            cmt.save()
        return redirect(display_post,pk=post_id)
    #checking if the image has been liked Already
    context["total_likes"]=Like.objects.filter(post = context["post"]).count()
    liked = Like.objects.filter(post = context["post"],like_by=request.user)
    # print("LIKES:",context["total_likes"])
    if liked:
        context["is_liked"]=True
    else:
        context["is_liked"]=False
    context["comments"] = Comment.objects.filter(post=context["post"])
    return render(request,'posts/view_post.html',context)

@login_required
def viewall(request):
    context ={"posts":Post.objects.filter(user=request.user)}
    return render(request,'posts/viewall.html',context)
