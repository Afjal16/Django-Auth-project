from django.urls import path
from . import views

urlpatterns = [
    path('', views.auth_index, name='auth_index'),
    path('login/', views.Login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('logout/', views.Logout, name='logout'),
    path('edit_registration/', views.edit_registration, name='edit_registration'),
    path('change_password/', views.change_password, name='change_password'),
    path('ResetPassword/', views.ResetPassword.as_view(), name='ResetPassword'),
    path('ResetPassword_Done/done/', views.ResetPassword_Done.as_view(), name='ResetPassword_Done'),
    path('ResetPassword_Confirm/<uidb64>/<token>/', views.ResetPassword_Confirm.as_view(), name='ResetPassword_Confirm'),
    path('ResetPassword_Complete/done/', views.ResetPassword_Complete.as_view(), name='ResetPassword_Complete'),
]
