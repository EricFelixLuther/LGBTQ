# -*- coding: UTF-8 -*-
'''
Created on Apr 20, 2016

@author: k.maciejczuk
'''

from django.views.generic.base import View
from django.shortcuts import render, redirect
from opracowanie_pytan.questions.models import Kierunek


class View_All(View):
    template = "view_all.html"

    def get(self, request, *args, **kwargs):
        specs = Kierunek.objects.all()
        return render(request,
                      self.template,
                      {"specs": specs}
                      )

    def post(self, request, *args, **kwargs):
        return redirect("edit", question_id=request.POST.get("question_id"))
        #return redirect('/some/url/')

    def dispatch(self, *args, **kwargs):
        return super(View_All, self).dispatch(*args, **kwargs)


class Edit(View):
    template = "edit.html"

    def get(self, request, *args, **kwargs):
        return render(request,
                      self.template,
                      {"key": "val"})

    def post(self, request, *args, **kwargs):
        pass

    def dispatch(self, *args, **kwargs):
        return super(Edit, self).dispatch(*args, **kwargs)



class TemplateView(View):
    template = "template.html"

    def get(self, request, *args, **kwargs):
        return render(request,
                      self.template,
                      {"key": "val"})

    def post(self, request, *args, **kwargs):
        pass

    def dispatch(self, *args, **kwargs):
        return super(TemplateView, self).dispatch(*args, **kwargs)
