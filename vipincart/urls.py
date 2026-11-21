
from django.contrib import admin
from django.urls import path,include
from home import views
from login import views 
from account import views
from modelfrom import views
from index import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.first, name='first'),
    path('admin/', admin.site.urls),
    path('form/', include('login.urls')),
    path('account/', include('account.urls')),
    path('models/', include('modelfrom.urls')),
     
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
    
