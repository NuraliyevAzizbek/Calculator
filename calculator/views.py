from django.shortcuts import render
from .models import Calculator, Math_hints

# Create your views here.

def calculator(request):
    actions = Calculator.objects.exclude(hint=Math_hints.BULISH, value_2=0.0)

    hint_filter = request.GET.get("hint_filter", "")

    if request.method == 'POST':
        value1 = request.POST.get("value1", "")
        value2 = request.POST.get("value2", "")
        hint = request.POST.get("hint", "+")

        action_obj = Calculator.objects.create(
            value_1 = value1,
            value_2 = value2,
            hint = hint
        )


        context = {
            'actions':actions,
            "action_obj": action_obj
            }
        return render(request, 'calculator.html', context) #redirect
    
    if hint_filter:
        actions = actions.filter(hint = hint_filter)
        
    context = {
        'actions':actions,
        'hint_filter':hint_filter
        }
    return render(request, 'calculator.html', context)