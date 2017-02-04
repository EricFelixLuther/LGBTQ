"""opracowanie_pytan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import ListView
from opracowanie_pytan.questions.views import Edit_Question,\
    Quiz_Set_Create_View, Quiz_View
from opracowanie_pytan.questions.models import Quiz_Set, Question

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^create_quiz/$', Quiz_Set_Create_View.as_view(), name="create_quiz"),
    url(r'^quiz/(?P<quiz_id>\d+)$', Quiz_View.as_view(), name="quiz"),
    url(r'^edit_quiz/(?P<quiz_id>\d+)$', Quiz_Set_Create_View.as_view(), name="edit_quiz"),
    url(r'^new_question/$', Edit_Question.as_view(), name="new_question"),
    url(r'^edit_question/<+P>$', Edit_Question.as_view(), name="edit_question"),
    url(r'^$', ListView.as_view(model=Quiz_Set, template_name="quiz_sets.html"), name="home"),
    # delete quiz
    # delete question
]
