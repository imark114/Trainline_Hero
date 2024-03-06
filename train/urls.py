from django.urls import path
from . import views

urlpatterns = [
    path('all_trains/', views.TrainView, name='all_trains'),
    path('filter_train/', views.FilterTrain, name='filter_train'),
    path('train_details/<int:id>', views.TrainDetailsView.as_view(), name='train_details')
]
