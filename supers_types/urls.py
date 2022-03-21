from django.urls import path
from supers import views 


urlpatterns= [
    path('', views.SupersList.as_view()),
    path('<int:pk>/', views.SupersDetails.as_view())
]