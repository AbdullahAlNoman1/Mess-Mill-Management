from django.db import models
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta

today_date = timezone.datetime.now().date()
next_day = today_date + timedelta(1)

class MemberQuerySet(models.query.QuerySet):

    def active(self):
        return self.filter(active=True)

    def self_expense(self):
        return self.filter(pk=self.pk).expense_set.all()


class MemberManager(models.Manager):

    def get_queryset(self):
        return MemberQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def member_expense(self):
        return self.get_queryset().self_expense()


class Member(models.Model):
    name = models.CharField(max_length=50)
    phone = models.PositiveIntegerField(blank=True, null=True)
    timestimp = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    objects = MemberManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('messapp:member_details', kwargs={'pk': self.pk})


class Deposit(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    total = models.DecimalField(decimal_places=2, max_digits=10)
    date = models.DateField(default=timezone.datetime.now().date())
    timestimp = models.DateTimeField(default=timezone.datetime.now())

    def __str__(self):
        return self.member.name

MEAL_TIME = (
    ('breakfast', 'Breakfast'),
    ('launch', 'Launch'),
    ('dinner', 'Dinner')
)



class ExpenseQuerySet(models.query.QuerySet):

    def active(self):
        return self.filter(active=True)

    def breakfast(self):
        # day = datetime.
        return self.filter(meal_type='breakfast', date=today_date)

    def launch(self):
        return self.filter(meal_type='launch', date=today_date)

    def dinner(self):
        return self.filter(meal_type='dinner', date=today_date)


class ExpenseManager(models.Manager):

    def get_queryset(self):
        return ExpenseQuerySet(self.model, using=self._db)

    def breakfast(self):
        return self.get_queryset().breakfast().active()

    def launch(self):
        return self.get_queryset().launch().active()

    def dinner(self):
        return self.get_queryset().dinner().active()


class Expense(models.Model):
    meal_type = models.CharField(max_length=20, choices=MEAL_TIME, blank=True, null=True)
    buyer = models.ForeignKey(Member, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    details = models.TextField(blank=True)
    date = models.DateField(auto_now=False, auto_now_add=False, default=timezone.datetime.now().date())
    timestimp = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = ExpenseManager()

    def __str__(self):
        return self.name


class Meal(models.Model):
    member = models.OneToOneField(Member, models.CASCADE)
    total = models.PositiveIntegerField()
    date = models.DateField(default=timezone.datetime.now().date())

    def __str__(self):
        return self.member.name
