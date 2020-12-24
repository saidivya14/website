"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from chatting import views as chatting_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',chatting_views.home, name='home'),
    path('logout/', chatting_views.logout_view, name='logout'),
    path('login/', chatting_views.Login, name='login'),
    path('register/', chatting_views.register, name='register'),
    path('chat/', chatting_views.chat_view, name='chats'),
    path('chat/<int:sender>/<int:receiver>/', chatting_views.message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>/', chatting_views.message_list, name='message-detail'),
    path('api/messages/', chatting_views.message_list, name='message-list'),
]

if settings.DEBUG:
    urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
