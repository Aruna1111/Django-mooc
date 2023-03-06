from django.urls import path
from mooclist.views import CoursesList

urlpatterns = [
    path('', CoursesList.as_view(template_name='users/home.html'), name='mooc-detail'),
]
