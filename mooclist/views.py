from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, DetailView

from .models import *
from django.views.generic.list import ListView


class CoursesList(ListView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context



class CoursesCreateView(CreateView):
    model = Course
    template_name = 'users/create.html'
    fields = ['name', 'discipline', 'platform', 'price', 'available', 'link', 'weeks', 'hours']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CoursesDetailsView(DetailView):
    pass


