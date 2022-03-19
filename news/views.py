from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView
from django.core.paginator import Paginator

from .models import *
from .forms import NewsForm


def news_list(request):
    news = News.objects.all().order_by('-date_published')
    size = 20
    if request.GET.get('num'):
        size = request.GET.get('num')
    paginator = Paginator(news, size)

    count_pages = None
    is_paginated = False
    if paginator.num_pages > 1:
        is_paginated = True
        count_pages = [i for i in range(1, paginator.count + 1)]

    page = request.GET.get('page') 
    page_obj = paginator.get_page(page)
    context = {
        'page_obj':page_obj,
        'is_paginated': is_paginated,
        'count_pages': count_pages,
    }
    return render(request, 'index.html', context=context)

def create(request):
    error = ''
    if request.method == 'POST' and request.FILES:
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = "Форма была некорректной"

    form = NewsForm()
    return render(request, 'news/news_form.html', {'form':form, 'error':error})


class NewsDetailView(generic.DetailView):
    model = News


class NewsDelete(DeleteView):
    model = News
    success_url = reverse_lazy('index')
