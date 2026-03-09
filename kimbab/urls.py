from django.urls import re_path
from . import views

app_name = "kimbab"

urlpatterns = [
    re_path(r"^$", views.index, name="index"),
    re_path(r"^list/$", views.kimbab_list, name="kimbab_list"),
    re_path(r"^search/$", views.kimbab_search, name="kimbab_search"),
]
