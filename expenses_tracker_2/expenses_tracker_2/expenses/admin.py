from django.contrib import admin

# Register your models here.
from expenses_tracker_2.expenses.models import Expense

admin.site.register(Expense)
