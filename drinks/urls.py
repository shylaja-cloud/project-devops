from . import views
from django.urls import path

'app/model_viewtype'
'drinks/drink_detail.html'

urlpatterns = [
    path('', views.DrinkListView.as_view(), name="drinks-home"),
    path('drink/create/', views.DrinkCreateView.as_view(), name="drinks-create"),
    path('drink/<int:pk>', views.DrinkDetailView.as_view(), name="drinks-detail"),
    path('drink/<int:pk>/update/', views.DrinkUpdateView.as_view(), name="drinks-update"),
    path('drink/<int:pk>/delete/', views.DrinkDeleteView.as_view(), name="drinks-delete"),
    path('about/', views.about, name="drinks-about"),
    
]