from django.views.generic import ListView, DetailView  # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView  # new
from django.urls import reverse_lazy  # new
from .models import thingstodo
from django.views.generic import TemplateView

class ThingstodoHomeView(TemplateView):
    template_name = "thingstodo/home.html"

class ThingstodoListView(ListView):
    model = thingstodo
    template_name = "thingstodo_list.html"


class ThingstodoDetailView(DetailView):  # new
    model = thingstodo
    template_name = "thingstodo_detail.html"


class ThingstodoUpdateView(UpdateView):  # new
    model = thingstodo
    fields = (
        "title",
        "body",
    )
    template_name = "thingstodo_edit.html"


class ThingstodoDeleteView(DeleteView):  # new
    model = thingstodo
    template_name = "thingstodo_delete.html"
    success_url = reverse_lazy("thingstodo_list")


class ThingstodoCreateView(CreateView):  # new
    model = thingstodo
    template_name = "thingstodo_new.html"
    fields = (
        "title",
        "body",
        "author",
    )
    success_url = '/'