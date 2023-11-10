from django.http import HttpResponse
from django.shortcuts import render

from budget_evaluation_register.models import Budget


# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/pages/dashboard.html')


def reports(request):
    if request.user.is_authenticated:
        data = Budget.objects.all()
        return render(request, 'dashboard/pages/reports.html', {'data': data})
    else:
        return HttpResponse('Voce precisa estar logado!')
