from django.shortcuts import render
from .models import Calculator, Math_hints
from .forms import HintFilterForm, ActionFrom

# Create your views here.

def calculator(request):
    actions = Calculator.objects.exclude(hint=Math_hints.BULISH, value_2=0.0)
    form = HintFilterForm()
    if request.method == "GET":
        form = HintFilterForm(data=request.GET)
        if form.is_valid():
            actions = form.save()

    action_form = ActionFrom()
    action_obj = ''
    if request.method == 'POST':
        action_form = ActionFrom(data=request.POST)
        if action_form.is_valid():
            action_obj = action_form.save() #redirect
        
    context = {
        'form':form,
        'action_form':action_form,
        'actions':actions,
        'action_obj':action_obj,
        }
    return render(request, 'calculator.html', context)