"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include

from pages.views import homepage_view
# from products.views import prodcuts_details_view, products_form_view, dynamic_links, products_delete_view, product_lsit_view

urlpatterns = [
    path('', homepage_view, name="home"),
    
    # NORMAL FORM
    # path('products/', prodcuts_details_view, name="products"),
    # path('products_form/', products_form_view, name="products_form"),
    # #path('products/<str:my_title>/',dynamic_links, name="dynamic_product"),
    # path('products/<int:my_id>/',dynamic_links, name="dynamic_product"),
    #  path('list/', product_lsit_view, name="list_product"),
    # path('delete/<int:my_id>/',products_delete_view, name="delete_product"),

    # DYNAMIC FORM
    path('products/', include('products.urls')),
    path('articles/', include('blog.urls')),
    #
    path('admin/', admin.site.urls),
]
