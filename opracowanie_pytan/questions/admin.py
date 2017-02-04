from django.contrib import admin

from .models import Quiz_Set, Question

admin.site.register([Quiz_Set, Question])
