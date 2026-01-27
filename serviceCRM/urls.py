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

urlpatterns = [
    path("", view.home, name="home"),
    path("dashboard/", view.InsertListView.as_view(), name="dashboard"),
    path('admin/', admin.site.urls),
    path("insert/", view.InsertNew.insert, name="insert"),
    path("logout/", view.logout_view, name="logout"),
    path("track/", view.track_ticket, name="track_ticket"),
    path("ticket/<str:ticket_id>/", view.Nalog, name="nalog"),
    
    # Secure public links
    path("print/label/<str:ticket_id>/", view.print_label, name="print_label"),
    path("print/receipt/<str:ticket_id>/", view.print_receipt, name="print_receipt"),
    
    # Secure staff actions
    path("edit/<str:ticket_id>/", view.Update.as_view(), name="update"),
    path("close/<str:ticket_id>/", view.CloseTicketView.as_view(), name="close_ticket"),
    path("delete/<str:ticket_id>/", view.Delete.delete, name="delete"),
    
    path("done/", view.Done.as_view(), name="done"),
    path("done/<str:ticket_id>/", view.Done.done_by_id, name="done_detail"),
    path("datatable/", view.DatatableView.as_view(), name="datatable"),

    # Todo List
    path('todo/', view.todo_list, name='todo_list'),
    path('todo/toggle/<int:pk>/', view.todo_toggle, name='todo_toggle'),
    path('todo/edit/<int:pk>/', view.todo_edit, name='todo_edit'),
    path('todo/delete/<int:pk>/', view.todo_delete, name='todo_delete'),
]
