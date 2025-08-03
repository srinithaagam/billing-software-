from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_bill, name='new_bill'),
    path('create_bill/', views.create_bill, name='create_bill'),
    path('add/', views.add_item, name='add_item'),
    path('bill/<int:bill_id>/', views.bill_view, name='bill_view'),
    path('bill/pdf/<int:bill_id>/', views.bill_pdf, name='bill_pdf'),
    path('history/', views.bill_history, name='history'),
    path('edit_item/<int:item_id>/', views.edit_item, name='edit_item'),
    path('delete_item/<int:item_id>/', views.delete_item, name='delete_item'),

]
##     path('', views.index, name='index'),
#     path('add/', views.add_item, name='add_item'),
#     path('bill/', views.bill_view, name='bill'),
# path('edit/<int:item_id>/', views.edit_item, name='edit_item'),
# path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
# path('new_bill/', views.new_bill, name='new_bill'),