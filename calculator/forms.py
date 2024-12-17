from django import forms

from .models import Calculator
from django.core.exceptions import ValidationError


class HintFilterForm(forms.Form):
    HINT_CHOICES = [
        ('+', '+'),
        ('-', '-'),
        ('*', '*'),
        ('/', '/')
    ]

    hint = forms.ChoiceField(
        choices=HINT_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    def save(self):
        hint = self.cleaned_data["hint"]
        hint_filter = Calculator.objects.filter(hint=hint)
        return hint_filter
    

class ActionFrom(forms.Form):
    value1 = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"type": "number"})
    )

    HINT_CHOICES = [
        ('+', '+'),
        ('-', '-'),
        ('*', '*'),
        ('/', '/')
    ]

    hint = forms.ChoiceField(
        choices=HINT_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"}),
    )

    value2 = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={"type": "number"})
    )

    def save(self):
        action = Calculator.objects.create(
            value_1 = self.cleaned_data["value1"],
            value_2 = self.cleaned_data["value2"],
            hint = self.cleaned_data["hint"]
        )
        return action
    
    def clean(self):
        if self.cleaned_data["hint"]== '/' and self.cleaned_data["value2"] == 0:
            raise ValidationError("0 ga bo'lish mumkin emas!")
