"""kurs_2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from app1.views import salary, salary_sheet, start, plan, ekzam, ekzam_print, student_list, oplata, oplata_print, \
    sertifikat, sertifikat_print, algor_add, algor_new, algor, open_algor, dell, calc, add_custo
from loginsys.views import login, logout, register

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', start),
    url(r'^salary/', salary),
    url(r'^sheet/', salary_sheet),
    url(r'^plan/', plan),
    url(r'^ekzam/$', ekzam),
    url(r'^ekzam/print/', ekzam_print),
    url(r'^student/$', student_list),
    url(r'^oplata/$', oplata),
    url(r'^oplata/print/', oplata_print),
    url(r'^sertifikat/$', sertifikat),
    url(r'^sertifikat/print/', sertifikat_print),
    url(r'^login/', login),
    url(r'^logout/', logout),
    url(r'^register/', register),
    url(r'^algor/change/(?P<algorithm_id>\d+)/$', algor_add),
    url(r'^algor/add/$', algor_add),
    url(r'^algor/new/', algor_new),
    url(r'^algor/$', algor),
    url(r'^algor/open/(?P<algorithm_id>\d+)/$', open_algor),
    url(r'^algor/del/(?P<algorithm_id>\d+)/', dell),
    url(r'^algor/open/(?P<algorithm_id>\d+)/calc/', calc),
    url(r'^add_custo/(?P<algorithm_id>\d+)/$', add_custo),

]
