from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.cheznous, name='nous'),
    url(r'^images/(\d+)',views.images, name ='images'),
    url(r'^petpic/',views.petpic, name ='petpic'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)