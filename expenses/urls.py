from django.contrib import admin
from django.urls import path
from expenses import views

urlpatterns = [
    path('', views.index, name='expenses'),
    path('add', views.add, name='add'),
    path('buy/<int:id>', views.buy, name='buy'),
    path('add-proxy', views.add_proxy, name='add-proxy'),
    path('added', views.added, name='added'),
    path('edit-expense/<int:id>', views.expense_edit, name='expense-edit'),
    path('expense-delete/<int:id>', views.expense_delete, name='expense-delete'),

]
