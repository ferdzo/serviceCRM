"""
URL configuration for serviceCRM project.

The `urlpatterns` list routes URLs to views.py. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views.py
    1. Add an import:  from my_app import views.py
    2. Add a URL to urlpatterns:  path('', views.py.home, name='home')
Class-based views.py
    1. Add an import:  from other_app.views.py import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import serviceCRM.views as view
from rest_framework import routers


urlpatterns = [
    path("", view.InsertListView.as_view(), name="index"),
    path('admin/', admin.site.urls),
    path("insert/", view.InsertNew.insert, name="insert"),
    path("edit/<int:pk>/", view.Update.as_view(), name="update"),
    path("nalog/<int:id>/", view.Nalog, name="nalog"),
    path("delete/<int:id>/", view.Delete.delete, name="delete"),
    path("done/", view.Done.as_view(), name="done"),
    path("done/<int:id>/", view.Done.done_by_id, name="done"),
    path("api/", view.get_all_inserts, name="api"),
    # path("datatable/", view.DatatableView.as_view(), name="datatable"),
]
