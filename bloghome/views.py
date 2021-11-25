from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import  postform
from django.urls import reverse_lazy


# Create your views here.
# def home(request):
# return render(request,'index.html')

class Home(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-id']


class postdetail(DetailView):
    model = Post
    template_name = 'post.html'


class Addpost(CreateView):
    model = Post
    form_class =  postform
    template_name = 'add_post.html'
    #fields = ('title', 'body')



class Addcomment(CreateView):
    model = Comment
    template_name = 'add_comment.html'
    fields = ('name', 'body')

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


class updatepost(UpdateView):
    model = Post
    template_name = 'update.html'
    fields = ['title', 'img', 'body']


class deletepost(DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = reverse_lazy('hm')



class deletecomment(DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    success_url = reverse_lazy('hm')




