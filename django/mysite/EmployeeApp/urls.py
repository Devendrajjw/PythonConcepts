# from django.conf.urls import urls
from django.urls import re_path
from . import views
# import views
from django.urls import path


urlpatterns = [
    # re_path(r'^department$', views.departmentApi),
    # re_path(r'^department/([0-9]+)$', views.departmentApi)  # we will need id to delete
    path('department', views.departmentApi, name='department_list'),
    path('department/<int:id>', views.departmentApi, name='department_detail')
]
