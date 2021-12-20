from django.urls import path

from expenses_tracker_2.expenses.views import create_expense, edit_expense, delete_expense

urlpatterns = [
    path('create/', create_expense, name='create expense'),
    path('edit/<int:pk>', edit_expense, name='edit expense'),
    path('delete/<int:pk>', delete_expense, name='delete expense'),
]
