from generators_site import views
from django.urls import path, re_path

urlpatterns = [
    path('', views.main),
    re_path(r'^Linear_Congruential_generator/$', views.Linear_Congruential_generator),
    path('Square_Congruential_generator', views.Square_Congruential_generator),
    path('Fibonacci_generator', views.Fibonacci_generator),
    path('Reverse_Congruential_generator', views.Reverse_Congruential_generator),
    path('Associative_generator', views.Associative_generator),
    path('Three_sigma_generator', views.Three_sigma_generator),
    path('Poliar_Cords_generator', views.Poliar_Cords_generator),
    path('Relative_generator', views.Relative_generator),
    path('Logarithm_generator', views.Logarithm_generator),
    path('Arence_generator', views.Arence_generator),
]
