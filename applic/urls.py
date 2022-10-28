from django.urls import re_path
from applic import views


urlpatterns = [
    re_path(r'^Details/$',views.DetailsApi),
    re_path(r'^Details/([0-9]+)$',views.DetailsApi),
    re_path(r'^Bill/$',views.BillApi),
    re_path(r'^Bill/([0-9]+)$',views.BillApi)
    ]
