'''
Created on May 11, 2016

@author: k.maciejczuk
'''
from django.db import models


class Kierunek(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)

    def get_questions(self):
        return Pytanie.objects.filter(spec=self)

    def __unicode__(self):
        return self.name


class Pytanie(models.Model):
    name = models.CharField(max_length=256, null=False, blank=False)
    spec = models.ForeignKey(Kierunek, null=False, blank=False, related_name="spec")
    reserved = models.CharField(max_length=64, null=True, blank=True)

    def get_answers(self):
        return Odpowiedz.objects.filter(question=self)

    def __unicode__(self):
        return self.name

class Odpowiedz(models.Model):
    text = models.CharField(max_length=2048, null=True, blank=True)
    question = models.ForeignKey(Pytanie, null=False, blank=False, related_name="question")
    author = models.CharField(max_length=32, null=False, blank=False)

    def __unicode__(self):
        return self.text