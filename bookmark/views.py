# bookmark/views.py
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Bookmark
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



class BookmarkListView(ListView):
    model = Bookmark


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url']
    success_url = reverse_lazy('list')  # 글쓰기를 완료했을 때 이동할 페이지
    template_name_suffix = '_create'


class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'  # 따라서 bookmark_update.html이어야 함


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')


class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 5  # 페이징 기능