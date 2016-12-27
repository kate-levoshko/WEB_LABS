"""block2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from simple import views, api_views
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/programmers/all/', api_views.all_programmers_api),
    url(r'^api/add/', api_views.post_prog_api),
    url(r'^api/delete/', api_views.prog_del_api),
    url(r'^api/filter/(\d+)/$', api_views.filter_salary_api),
    url(r'^auth/register/', views.register),
    url(r'^auth/login', views.login),
    url(r'^auth/logout/', views.logout),
    url(r'^info/show/', views.progs_view),
    url(r'^auth/logout/', views.logout),
    url(r'^prog/get/(\d+)/$', views.prog_by_id),
    url(r'^prog/delete/(\d+)/$', views.prog_del),
    url(r'^search/', views.search),
    url(r'^users/', views.view_users),
    url(r'^$', views.home),

] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
