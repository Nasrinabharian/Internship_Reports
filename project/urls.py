from django.contrib import admin
from django.urls import path, include
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('addreport/', views.secret_page.as_view(), name='secret'),
    path('list/', views.list_page.as_view(), name='list'),
    path('list/edit/<int:pk>', views.reportupdate.as_view(), name="reportupdate")


]
