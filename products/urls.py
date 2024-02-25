from . import views
from django.urls import path,include

urlpatterns = [
   
    path('iin/',views.Item_in,name='item_in'),
    path('iv/',views.item_view,name='item_view'),
    path('supi/',views.supplier_in,name='supplier_in'),
    path('supv/',views.supplier_view,name='supplier_view'),
    path('pin/',views.product_in,name='product_in'),
    path('pv/',views.product_view,name='product_view'),
]