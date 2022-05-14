
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Accounts',include("Accounts.urls")),
    path('Answers',include("Answers.urls")),
    path('Articles',include("Articles.urls")),
    path('home/',views.home),
    path('', views.home)
]

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  