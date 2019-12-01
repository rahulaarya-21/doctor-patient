from django.urls import path,include
from .import views
urlpatterns = [
  #path("",views.homepage,name="home")
   path("",views.Indexpage,name="Index"),
   path("registeredPage/",views.RegisterPage,name="RegisteredPage"),
   path("showpage/",views.show,name="showpage")

]
