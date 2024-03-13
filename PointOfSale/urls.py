from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="pos"),
    path("delete_item/<int:id>/", views.delete_item, name="delItem"),
    path("transaction/", views.transaction_view, name="transaction"),
    path("transaction/views", views.trasactions, name="transaction_views"),
    path("cancel_transaction/", views.cancel_transaction, name="cancel_transaction"),
    path("payment/<int:id>/", views.payment_view, name="payment"),
    path("cancel_payment/<int:id>/", views.cancel_payment_view, name="cancel_payment"),
]
