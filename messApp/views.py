import math
from django.shortcuts import render
from django.views import generic
from .models import Member, Expense, Meal, Deposit
from django.utils import timezone
from django.db.models import Sum
from datetime import timedelta

today_date = timezone.datetime.now().date()
next_day = today_date + timedelta(1)


def index(request):
    return render(request, 'index.html')


class MemberView(generic.ListView):
    model = Member
    template_name = 'messapp/member.html'


class MemberDetails(generic.DetailView):
    model = Member
    template_name = 'messapp/member_details.html'
    context_object_name = 'member_details'

    def get_context_data(self, *args, **kwargs):
        context = super(MemberDetails, self).get_context_data(*args, **kwargs)
        # context['member_expense'] = Member.objects.member_expense()

        return context


class ExpenseView(generic.ListView):
    model = Expense
    template_name = 'messapp/expense_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ExpenseView, self).get_context_data(*args, **kwargs)
        total = 0
        for cost in Expense.objects.all():
            total += cost.price
            context['total_expense'] = total

        return context


def balance_view(request):

    deposit = Deposit.objects.all().aggregate(Sum('total'))['total__sum']
    members = Member.objects.all()
    template_name = 'messapp/balance.html'

    context ={
        'member_obj': members,
        'deposit': deposit
    }

    return render(request, template_name, context)


def breakfastview(request):
    template_name = 'messapp/breakfast.html'

    obj = Expense.objects.breakfast()
    next_day = today_date + timedelta(1)
    next_day_obj = Expense.objects.filter(meal_type='breakfast', date=next_day)

    context = {
        'breakfast_expense': obj,
        'tomorrow_obj': next_day_obj,
        'next_day': next_day
    }
    return render(request, template_name, context)


def launchview(request):
    template_name = 'messapp/launch.html'

    obj = Expense.objects.launch()
    next_day = today_date + timedelta(1)
    next_day_obj = Expense.objects.filter(meal_type='launch', date=next_day)
    context = {
        'breakfast_expense': obj,
        'tomorrow_obj': next_day_obj,
        'next_day': next_day
    }
    return render(request, template_name, context)


def dinnerview(request):
    template_name = 'messapp/launch.html'

    obj = Expense.objects.dinner()
    next_day = today_date + timedelta(1)
    next_day_obj = Expense.objects.filter(meal_type='dinner', date=next_day)

    context = {
        'breakfast_expense': obj,
        'tomorrow_obj': next_day_obj,
        'next_day': next_day
    }
    return render(request, template_name, context)


def mealview(request):
    template_name = 'messapp/meal_list.html'
    obj = Meal.objects.filter(date=today_date)
    total_expense = Expense.objects.filter(date=today_date).aggregate(Sum('price'))['price__sum']
    total_meal = Meal.objects.all().aggregate(Sum('total'))['total__sum']
    if total_expense and total_meal is not None:
        rate_per_meal = total_expense / total_meal
    else:
        rate_per_meal = None
    context = {
        'meal_list': obj,
        'total_expense': total_expense,
        'total_meal': total_meal,
         'rate_per_meal': rate_per_meal
    }
    return render(request, template_name, context)