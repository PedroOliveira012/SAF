# from django.contrib.auth.models import User
# from django.http import HttpResponse
from django.shortcuts import redirect, render

from budget_evaluation_register.models import Budget
from user_authentication.models import UserProfile


# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/pages/dashboard.html')


def reports(request):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        job = user_profile.job
        if job == 'Orçamentista chefe' or request.user.is_superuser:
            data = Budget.objects.all()
        else:
            user = request.user.username
            data = Budget.objects.filter(evaluated=user)

        return render(request, 'dashboard/pages/reports.html', {'data': data, 'user': user_profile})
    else:
        return redirect('login')
