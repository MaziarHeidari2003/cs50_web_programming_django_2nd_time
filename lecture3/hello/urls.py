from django.urls import path
from . import views

urlpatterns = [
  path("", views.index, name="index"),
  path("maziar",views.maziar, name="maziar"),
  path("messi", views.messi , name="messi"),
  path("<str:name>",views.greet, name = "greet")
]