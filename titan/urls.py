from django.urls import path

# add this to import our views file
from titan import views

urlpatterns = [

    # add these to configure our home page (default view) and result web page
    path('', views.home, name='home'),
    path('result/', views.result, name='result'),
]