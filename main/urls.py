from django.urls import path
from main.views import show_main, add_product, edit_product, delete_product, show_xml, show_json
from main.views import show_xml_by_id, show_json_by_id, register, login_user, logout_user
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add_product', add_product, name='add_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<uuid:product_id>/', add_product, name='add_product'),
    path('edit_product/<uuid:product_id>/', edit_product, name ='edit_product'),
    path('delete_product/<uuid:product_id>/', delete_product, name ='delete_product')
]