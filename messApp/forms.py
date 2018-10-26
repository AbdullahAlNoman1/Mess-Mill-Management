from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        models = Member
        fields = '__all__'
