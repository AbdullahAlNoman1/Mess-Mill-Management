from django.contrib import admin
from .models import Member, Expense


class MemberAdmin(admin.ModelAdmin):

    list_display = ['name', 'phone', 'active', 'timestimp']

    class Meta:
        model = Member


admin.site.register(Member, MemberAdmin)


class ExpenseAdmin(admin.ModelAdmin):

    list_display = ['name', 'buyer', 'price', 'meal_type', 'active', 'date']
    list_filter = ['meal_type', 'timestimp']

    class Meta:
        model = Expense


admin.site.register(Expense, ExpenseAdmin)
