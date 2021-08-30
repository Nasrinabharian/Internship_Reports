from django import forms


from django.forms import ModelForm
from .models import internship_report
from django.utils.html import format_html
#from django_tables2.utils import A

class reportTable(forms.ModelForm):
    class Meta:
        model = internship_report
        template_name = "django_tables2/bootstrap.html"
        fields = ("title",
        "receiver_name",
        "description",
        "file", "status")
    
