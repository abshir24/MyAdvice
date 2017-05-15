from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^home$', views.home, name = 'home'),
    url(r'^answer$', views.answer, name = 'answer'),
    url(r'^addanswer$', views.addAnswer, name = 'addanswer'),
    url(r'^newquestion$', views.newquestion, name = 'newquestion')
]
