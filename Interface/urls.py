from django.urls import path
from .views import homepage, subjectsPage, topicsPage, getQuestions, aboutPage

urlpatterns = [
    path("", homepage, name="home-page"),
    path("subjects/", subjectsPage, name="subjects-page"),
    path("subject/<int:pk>", topicsPage, name="topics-page"),
    path("topic/<int:pk>", getQuestions, name="get-questions"),
    path("about", aboutPage, name="about-page"),
]


