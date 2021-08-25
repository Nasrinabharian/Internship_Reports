import django_tables2 as tables
from .models import internship_report
from django.utils.html import format_html

class reportTable(tables.Table):
    class Meta:
        model = internship_report
        template_name = "django_tables2/bootstrap.html"
        fields = ("title", "receiver_name",
        #"description",
        "file", "created_at",
        #"updated_at",
         "status")

    #     class FileColumn(tables.column):
        #     def render(self, value):
            #     return format_html('<')
