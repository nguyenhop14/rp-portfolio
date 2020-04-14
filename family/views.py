from django.shortcuts import render, HttpResponseRedirect
from django.views import generic
from .models import Parent, Child
from django.urls import reverse_lazy
from .forms import ChildrenFormset
from django.db import transaction
# Create your views here.
class ParentList(generic.ListView):
    model = Parent
    template_name = 'parent_list.html'
    context_object_name = 'parent_list'

    def get_queryset(self):
        return Parent.objects.all()
  

class ParentDetail(generic.DetailView):
  model = Parent
  template_name = "parent_detail.html"

class ParentCreate(generic.CreateView):
    model = Parent
    fields = ['name']
    success_url = reverse_lazy('family:parent_detail')

    def get_context_data(self):
        context = super().get_context_data()
        if self.request.POST:
            context['children'] = ChildrenFormset(self.request.POST)
        else:
            context['children'] = ChildrenFormset()
        return context
    def form_valid(self, form):
        context = self.get_context_data()
        children = context['children']
        with transaction.atomic():
            self.object = form.save()
            if children.is_valid():
                children.instance = self.object
                children.save()
        return super().form_valid(form)

class ParentDelete(generic.DeleteView):
  model = Parent 
  success_url = reverse_lazy('family:parents_list')

class ParentUpdate(generic.UpdateView):
  model = Parent
  fields = ['name']
  template_name = "family/parent_update.html"
  def get_success_url(self):   
    return reverse_lazy('family:parent_detail', kwargs={'pk': self.object.id})

class FamilyUpdate(generic.UpdateView):
  model = Parent
  fields = ['name']
  template_name = "family/parent_form.html"
  def get_success_url(self):   
    return reverse_lazy('family:parent_detail', kwargs={'pk': self.object.id})
  
  def get_context_data(self):
        context = super().get_context_data()
        if self.request.POST:
            context['children'] = ChildrenFormset(self.request.POST)
        else:
            context['children'] = ChildrenFormset()
        return context
  def form_valid(self, form):
        context = self.get_context_data()
        children = context['children']
        with transaction.atomic():
            self.object = form.save()
            if children.is_valid():
                children.instance = self.object
                children.save()
        return super().form_valid(form)