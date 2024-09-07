from django.urls import path
from .views import home, about, password

urlpatterns = [
    path('home/', home, name="home"),
    path('about/', about, name="about"),
    path('password/', password, name="password")
    
]

"""
from django.urls import path
from .views import HomeView, AboutView, PasswordView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Ruta para la vista HomeView
    path('about/', AboutView.as_view(), name='about'),  # Ruta para la vista AboutView
    path('password/', PasswordView.as_view(), name='password'),  # Ruta para la vista PasswordView
]
"""
