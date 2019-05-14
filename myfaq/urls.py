"""linux_item URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from django.conf.urls import  url
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),  loms_content_list
    url('^$', views.index ),
    url('^create_question',views.create_question),
    url('^loms_list_view',views.loms_list_view),
    url('^imt_list_view',views.itm_list_view),
    url('^twms_list_view',views.twms_list_view),
    url('^home', views.home),
    # url('^con_list',views.loms_content_list),
    path('book/loms_detail/<book_id>/<catgray>/', views.loms_book_detail, name='loms_detail'),
    path('book/itm_detail/<book_id>/<catgray>/', views.itm_book_detail, name='itm_detail'),
    path('book/twms_detail/<book_id>/<catgray>/', views.twms_book_detail, name='twms_detail'),
]
