from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.urls import reverse

from .forms import ArticleForm
from .models import Article
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    ListView
)

# Create your views here.







def article_list_view(request):
    queryset = Article.objects.all()
    context = {
        "article_list": queryset,
        'add_link': reverse("articles:articles_create")
    }
    return render(request, "articles/article_list.html", context)

def article_details_view(request,id):
    obj = get_object_or_404(Article, id=id)
    context = {
        "object": obj
    }
    return render(request, "articles/article_details.html", context)

def article_update_view(request,id):
    obj = get_object_or_404(Article, id=id)
    form_update = ArticleForm(request.POST or None, instance=obj)
    if form_update.is_valid():
        form_update.save()
        return redirect("../")
    context = {
        "form": form_update
    }
    return render(request, "articles/article_create.html", context)

def article_create_view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("../")
    

    context = {
        "form": form
    }
    return render(request, "articles/article_create.html", context)

def article_delete_view(request,id):
    obj = get_object_or_404(Article, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect("../../")
    context = {
        "obj": obj,
    }
    return render(request, "articles/article_delete.html", context)