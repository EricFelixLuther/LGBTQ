'''
Created on May 11, 2016

@author: root
'''
from django import forms
from opracowanie_pytan.questions.models import Quiz_Set, Question


class Quiz_Set_Form(forms.ModelForm):
    class Meta:
        model = Quiz_Set
        fields = "__all__"


class Question_Form(forms.ModelForm):
    class Meta:
        model = Question
        fields = "__all__"
