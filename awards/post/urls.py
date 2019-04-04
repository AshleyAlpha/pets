from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^theProfile/(\d+)', views.theProfile, name='theProfile'),
    url(r'^project/', views.project, name='project'),
    url(r'^images/(\d+)',views.images, name ='images'),
    # url(r'^comments/(\d+)', views.comments, name='comments'),
    # url(r'^like/',views.like,name ='like'),



]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)