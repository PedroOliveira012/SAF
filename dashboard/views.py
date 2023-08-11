from django.shortcuts import render


# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/pages/dashboard.html')


def reports(request):
    return render(request, 'dashboard/pages/reports.html')
