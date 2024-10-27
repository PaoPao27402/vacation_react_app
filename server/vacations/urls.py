from django.urls import path
from .views import LoginView, LogoutView, StatisticsView, UserCountView, LikesCountView, LikesDistributionView, VacationListCreateView, VacationDetailView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('statistics/', StatisticsView.as_view(), name='statistics'),
    path('user-count/', UserCountView.as_view(), name='user_count'),
    path('likes-count/', LikesCountView.as_view(), name='likes_count'),
    path('likes-distribution/', LikesDistributionView.as_view(), name='likes_distribution'),
    path('vacations/', VacationListCreateView.as_view(), name='vacation-list-create'),
    path('vacations/<int:pk>/', VacationDetailView.as_view(), name='vacation-detail'),
]
