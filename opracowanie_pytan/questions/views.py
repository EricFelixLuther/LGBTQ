# -*- coding: UTF-8 -*-
'''
Created on Apr 20, 2016

@author: k.maciejczuk
'''

from django.views.generic.base import View
from django.shortcuts import render, redirect
from opracowanie_pytan.questions.models import Quiz_Set, Question
from opracowanie_pytan.questions.forms import Quiz_Set_Form, Question_Form
from opracowanie_pytan.questions.templatetags.templatetags import CELL_PARSE_SYMBOL,\
    ROW_PARSE_SYMBOL
from django.core.urlresolvers import reverse

class Quiz_Set_Create_View(View):
    template_name = "quiz_set_create_form.html"
    def get(self, request, quiz_id=None, *args, **kwargs):
        if quiz_id:
            form = Quiz_Set_Form(instance=Quiz_Set.objects.get(pk=quiz_id))
        else:
            form = Quiz_Set_Form()
        return render(request, self.template_name,
                      {"form": form})

    def post(self, request, quiz_id=None, *args, **kwargs):
        if quiz_id:
            form = Quiz_Set_Form(instance=Quiz_Set.objects.get(pk=quiz_id),
                                            data=request.POST)
        else:
            form = Quiz_Set_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, self.template_name,
                          {"form": form})


class Quiz_View(View):
    template_name = "quiz.html"
    def get(self, request, quiz_id, *args, **kwargs):
        quiz = Quiz_Set.objects.get(pk=quiz_id)
        return render(request, self.template_name,
                      {"quiz": quiz})


class Edit_Question(View):
    template = "edit.html"

    def get(self, request, question_id=None, *args, **kwargs):
        if question_id == None:
            form = Question_Form()
        else:
            form = Question_Form(instance=Question.objects.get(pk=question_id))
        return render(request,
                      self.template,
                      {"form": form,
                       "cell_parse": CELL_PARSE_SYMBOL,
                       "row_parse": ROW_PARSE_SYMBOL})

    def post(self, request, question_id=None, *args, **kwargs):
        if question_id == None:
            form = Question_Form(request.POST)
        else:
            form = Question_Form(instance=Question.objects.get(pk=question_id),
                                 data=request.POST)

        if form.is_valid():
            obj = form.save()
            if request.POST.get("save"):
                return redirect(reverse("quiz", kwargs={"quiz_id": obj.quiz_set.id}))
            elif request.POST.get("another"):
                return redirect(reverse("new_question"))

        return render(request,
                      self.template,
                      {"form": form,
                       "cell_parse": CELL_PARSE_SYMBOL,
                       "row_parse": ROW_PARSE_SYMBOL})

    def dispatch(self, *args, **kwargs):
        return super(Edit_Question, self).dispatch(*args, **kwargs)
