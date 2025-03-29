from django.contrib import admin
from django.urls import path
from .views import ShortenURLView,ReturnDataView,UpdateURLView,DeleteURLView,CountURlView

urlpatterns = [
    path("shorten/", ShortenURLView.as_view(), name="shorten"),
    path("return/<str:Short_URL>/", ReturnDataView.as_view(), name="return_data"),
    path("update/<str:Short_URL>/", UpdateURLView.as_view(), name="update"),
    path("delete/<str:Short_URL>/", DeleteURLView.as_view(), name="delete"),
    path("count/<str:Short_URL>/", CountURlView.as_view(), name="count"),
    
    
    

    
    
]
 