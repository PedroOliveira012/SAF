from django.shortcuts import render

from budget_evaluation_register.models import Budget


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/pages/dashboard.html')


def reports(request):
    data = Budget.objects.all()
    return render(request, 'dashboard/pages/reports.html', {'data': data})
