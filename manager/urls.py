
from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('create/',views.create,name='create'),
    path('reports/',views.reports,name='reports'),   
    path('list/',views.list,name='list'),
    path('admin/',views.admin,name='admin'),
    path('all_products/',views.all_products,name='all_products'),
    path('edit/<pk>',views.edit,name='edit'),
    path('del_cnf/<pk>',views.del_cnf,name='del_cnf'),
    path('details/<pk>',views.details,name='details'),
    path('order_delcnf/<pk>',views.order_delcnf,name='order_delcnf'),
    path('reports/',views.reports,name='reports'),
    path('sales_reports/',views.sales_reports,name='sales_reports'),
    path('show_cupboard/',views.show_cupboard,name='show_cupboard'),
    path('show_table/',views.show_table,name='show_table'),
    path('show_tv_stand/',views.show_tv_stand,name='show_tv_stand'),
    path('show_sofa/',views.show_sofa,name='show_sofa'),
    path('bedroom_set/',views.bedroom_set,name='bedroom_set'),
    path('pooja_stand/',views.pooja_stand,name='pooja_stand'),
    path('order/',views.order,name='order'),
    path('orders_det/',views.orders_det,name='orders_det'),
    path('order_det/',views.order_det,name='order_det'),
    path('others/',views.others,name='others'),

    
]