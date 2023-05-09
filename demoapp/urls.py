from django.urls import path
from demoapp import views
 


urlpatterns=[
  
    path('about/', views.about),
    # path('careers/<int:pageno>', views.careers),

    path('careers/', views.careers),
    # path('contact/', views.contact),
     path ('', views.index),

]                                                                   