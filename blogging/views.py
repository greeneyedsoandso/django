from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.shortcuts import redirect
from django import forms
from django.utils import timezone
from blogging.forms import MyCommentForm
from blogging.models import Comment
from django.views.generic.edit import CreateView


class PostListView(ListView):
    template_name = "blogging/list.html"
    queryset = Post.objects.exclude(published_date__exact=None).order_by(
        "-published_date"
    )


class PostDetailView(DetailView):
    model = Post
    template_name = "blogging/detail.html"
    queryset = Post.objects.exclude(published_date__exact=None)


class CommentCreateView(CreateView):
    model = Comment
    template_name = "blogging/add.html"
    fields = []

    def add_model(self, request):

        if request.method == "POST":
            form = MyCommentForm(request.POST)
            if form.is_valid():
                model_instance = form.save(commit=False)
                model_instance.timestamp = timezone.now()
                model_instance.save()
                return redirect("/")

        else:

            form = MyCommentForm()

            return render(request, "blogging/add.html", {"object": form})
