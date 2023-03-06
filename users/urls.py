from django.urls import path
from .views import home, profile, RegisterView, course_create, MoocDetailView, discipline_create

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/add-mooc/', course_create, name='users-mooc'),
    path('profile/add-disc/', discipline_create, name='users-disc'),
    #path('profile/home'), MoocDetailView.as_view(), name='mooc-detail'),
    path('profile/', profile, name='users-profile'),
]
