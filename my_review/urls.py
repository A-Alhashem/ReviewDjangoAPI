"""my_review URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from my_app.views import ReviewListView, ReviewDetailView, ReviewUpdateView, ReviewDeleteView, ReviewCreateView, UserCreateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list/', ReviewListView.as_view(), name='list'),
    path('detail/<detail_id>', ReviewDetailView.as_view(), name='detail'),
    path('update/<update_id>', ReviewUpdateView.as_view(), name='update'),
    path('delete/<delete_id>', ReviewDeleteView.as_view(), name='delete'),
    path('create/', ReviewCreateView.as_view(), name='create'),
    path('register/', UserCreateAPIView.as_view(), name='register'),

]

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)