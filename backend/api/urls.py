from django.urls import path
from .views import SignUpView, LoginView, countries

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('countries/', countries, name='countries'),
]
