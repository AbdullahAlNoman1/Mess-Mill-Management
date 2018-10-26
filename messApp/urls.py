from django.urls import path
from . import views

app_name = 'messApp'

urlpatterns = [
    path('', views.index, name="index"),
    path('member/', views.MemberView.as_view(), name='member'),
    path('member/<pk>', views.MemberDetails.as_view(), name="member_details"),
    path('expense/', views.ExpenseView.as_view(), name="expense"),
    # path('breakfast/', views.BreakfastView.as_view(), name="breakfast"),
    path('breakfast/', views.breakfastview, name="breakfast"),
]