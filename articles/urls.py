from django.urls import path , re_path
from . import views


urlpatterns = [
    re_path(r'^$',views.articles_list),
    re_path(r'^(?P<slug>[\w-]+)/$', views.articles_details),
]