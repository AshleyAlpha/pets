from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.cheznous, name='nous'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^theProfile/(\d+)', views.theProfile, name='theProfile'),
    url(r'^picture/', views.picture, name='picture'),
    url(r'^images/(\d+)',views.images,name ='images'),


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)