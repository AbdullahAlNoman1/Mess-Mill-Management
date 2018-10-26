from django.shortcuts import render
from django.views import generic
from django.utils.timezone import datetime
from .models import Member, Expense


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


# class BreakfastView(generic.ListView):
#     model = Expense
#     template_name = 'messapp/breakfast.html'
#
#     def get_context_data(self, *args, **kwargs):
#         context = super(BreakfastView, self).get_context_data(*args, **kwargs)
#         # total = 0
#         # for cost in Expense.objects.breakfast():
#         #     total += cost.price
#         #     context['total_expense'] = total
#
#         return context


def breakfastview(request):
    template_name = 'messapp/breakfast.html'

    obj = Expense.objects.filter(date=datetime.now().date())

    context = {
        'breakfast_expense': obj
    }
    return render(request, template_name, context)