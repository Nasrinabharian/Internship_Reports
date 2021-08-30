from django.db import models
from django.urls import reverse
from django.utils import timezone
s_CHOICES = (
    ('New', 'New'),
    ('Completed','Completed'),
)
class internship_report(models.Model):
    title = models.CharField(max_length = 200)
    receiver_name = models.CharField(max_length = 200)
    description = models.TextField()
    file = models.FileField(null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices=s_CHOICES, default='New')
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("home")
    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)
