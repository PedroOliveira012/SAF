from django.shortcuts import render


# Create your views here.
def new_register(request):
    return render(request, 'budget_evaluation_register/pages/form.html')
