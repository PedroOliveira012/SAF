from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Budget


# Create your views here.
def new_register(request):
    if request.user.is_authenticated:
        return render(request, 'budget_evaluation_register/pages/form.html')


def details(request, id):
    if request.user.is_authenticated:
        details = get_object_or_404(Budget, pk=id)
        return render(
            request,
            'budget_evaluation_register/pages/reports_details.html',
            {'details': details}
        )


def add_report(request):
    if request.user.is_authenticated:
        new_report = Budget()
        new_report.evaluated = request.POST.get('employee')
        new_report.project_number = request.POST.get('project_number')
        new_report.project_name = request.POST.get('project_name')
        new_report.client_name = request.POST.get('client')
        new_report.documentation = request.POST.get('documentation')
        new_report.reason_documentation = request.POST.get(
            'reason_documentation')
        new_report.material_list = request.POST.get('material_list')
        new_report.reason_material_list = request.POST.get(
            'reason_material_list')
        new_report.price = request.POST.get('price')
        new_report.reason_price = request.POST.get('reason_price')
        new_report.layout = request.POST.get('layout')
        new_report.reason_layout = request.POST.get('reason_layout')
        new_report.network = request.POST.get('network')
        new_report.reason_network = request.POST.get('reason_network')
        new_report.tecnical_offer = request.POST.get('tecnical_offer')
        new_report.reason_tecnical_offer = request.POST.get(
            'reason_tecnical_offer')
        new_report.commercial_offer = request.POST.get('commercial_offer')
        new_report.reason_commercial_offer = request.POST.get(
            'reason_commercial_offer')
        new_report.save()
        return HttpResponseRedirect(reverse('reports'))


def delete(request, id):
    if request.user.is_authenticated:
        report = Budget.objects.get(id=id)
        report.delete()
        return HttpResponseRedirect(reverse('reports'))


def finish(request, id):
    if request.user.is_authenticated:
        report = Budget.objects.get(id=id)
        report.finished = True
        report.save()
        return HttpResponseRedirect(reverse('reports'))
