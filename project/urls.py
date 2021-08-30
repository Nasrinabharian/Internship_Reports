from django.contrib import admin
from django.urls import path, include
from core import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('addreport/', views.secret_page, name='secret'),
    path('list/', views.list_page.as_view(), name='list'),
    path('list/delete_report/<int:pk>/', views.delete_report, name='delete_report'),
    path('list/<int:pk>/', views.update_report, name='update_report'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
