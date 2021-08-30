from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from core.models import internship_report
from django_tables2 import SingleTableView
from .forms import reportTable
from django.core.files.storage import FileSystemStorage
from django import forms
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.forms import ModelForm
from .models import internship_report
from django.utils.html import format_html
class ReportForm(forms.ModelForm):
    class Meta:
        model = internship_report
        fields = [
            "title",
            "receiver_name",
            "description",
            "file",
            "status"
            ]


def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {'count': count})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def secret_page(request):
    if request.method == "GET":
        form = reportTable()
        return render(request, 'secret_page.html', {'form': form})
    else:
        form = reportTable(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        print(form.errors)
        return redirect('list')
class list_page(ListView):
    model = internship_report
    table_class = reportTable
    template_name = 'reports_page.html'
    context_object_name = 'reports'

@login_required
def delete_report(request, pk):
    if request.method =='POST':
        report = internship_report.objects.get(pk=pk)
        report.delete()
    return redirect('list')


@login_required
def update_report(request, pk):
    if request.method == "GET":
        report = internship_report.objects.get(pk=pk)
        form = reportTable(instance=report)
        return render(request, 'secret_page.html', {'form': form})
    else:
        report = internship_report.objects.get(pk=pk)
        form = reportTable(request.POST, request.FILES, instance= report)
        if form.is_valid():
            form.save()
        print(form.errors)
        return redirect('list')
