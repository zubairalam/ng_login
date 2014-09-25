from django.conf.urls import patterns, url
from .views import UserRegistrationView

urlpatterns = patterns('',
                       url(r'^signup/$', UserRegistrationView.as_view()),
)
