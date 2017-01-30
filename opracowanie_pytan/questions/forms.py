'''
Created on May 11, 2016

@author: root
'''
from django.forms import models
from opracowanie_pytan.questions.models import Odpowiedz


class Edit(models.ModelForm):
    class Meta():
        model = Odpowiedz