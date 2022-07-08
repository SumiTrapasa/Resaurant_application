"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from restuarant.views import ( restuarant_details_view,
 restuarant_view, 
 items_view, 
 res_create,
 res_update,
 res_delete,
 item_update,
 item_delete,
 item_create,
 cuis_view,
 cuis_create,
 cuis_delete,
 cuis_update
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:id>/',res_update, name='res_update'),
    path('<int:id>/delete/',res_delete, name='res_delete'),
    path('add/',res_create, name='res_create'),
    path('add/cuisines',cuis_create, name='cuis_create'),
    path('edit/<int:id>/',cuis_update, name='cuis_update'),
    path('',restuarant_details_view, name= 'list'),
    path('restuarant/<int:id>/',restuarant_view , name='view'),
    path('restuarant/items/<int:id>/',items_view , name='item'),
    path('restuarant/<int:res_id>/<int:menu_id>/update/', item_update, name='item_update' ),
    path('restuarant/<int:res_id>/<int:menu_id>/delete/', item_delete, name='item_delete' ),
    path('restuarant/<int:res_id>/create/', item_create, name='item_create' ),
    path('restuarant/<int:res_id>/<int:cuis_id>/cuisines/', cuis_view, name='cuis_view' ),
    path('restuarant/<int:res_id>/<int:cuis_id>/cuisines/delete/', cuis_delete, name='cuis_delete' ),
]
