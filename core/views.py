from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import internship_report
from django_tables2 import SingleTableView
from .tables import reportTable
def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
    'count': count
    })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
    'form': form
    })


#@login_required
#def list_page(request):
#    return render(request, 'reports_page.html')

#def reports_page(request):
#    return render(request, 'reports_page.html')

class secret_page(LoginRequiredMixin, CreateView):
    model = internship_report
    #if request.method == 'POST':
    #    model = internship_report(request.POST)
    #    if model.is_valid():
        #    model.save()
        #    return redirect('/')
    fields = ["title", "receiver_name", "description", "file", "status"]
    template_name = 'secret_page.html'

class reportupdate(LoginRequiredMixin, UpdateView):
    model = internship_report
    fields = ["title", "receiver_name", "description", "file", "status"]
    template_name = 'secret_page.html'
#class list_page(ListView):
    #model = internship_report
    #template_name = 'reports_page.html'

class list_page(SingleTableView):
    model = internship_report
    table_class = reportTable
    template_name = 'reports_page.html'



#class SecretPage(LoginRequiredMixin, TemplateView):
#    template_name = 'secret_page.html'
