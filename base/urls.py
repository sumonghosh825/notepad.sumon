from django.urls import path
from .views import register_view, login_view,dashboard,task,board,details,timeline,profile
urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('task/', task, name='task'),
    path('board/', board, name='board'),
    path('details/', details, name='details'),
    path('timeline/', timeline, name='timeline'),
    path('profile/', profile, name='profile'),
]

