from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="product_management" ),
    path("new_product/", views.create_product_page, name="new_product" ),
    path("update_product/<int:id>", views.update_product_page, name="update_product"),
    path("add_product_stocks/<int:id>", views.add_stocks_view, name="add_stocks"),
    path("stocks_management/", views.stocks_view, name="stocks_management"),
]