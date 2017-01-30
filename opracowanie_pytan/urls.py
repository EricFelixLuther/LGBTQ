"""opracowanie_pytan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from opracowanie_pytan.questions.views import View_All, Edit

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^/', Login.as_view(), name="home"),
    #url(r'^create_user/', Create_User.as_view(), name="create_user"),
    url(r'^view_all/', View_All.as_view(), name="view_all"),
    url(r'^edit/<+P>', Edit.as_view(), name="edit"),
]
