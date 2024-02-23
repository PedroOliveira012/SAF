from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from user_authentication.models import UserProfile

from .models import Project, Project_errors


# Create your views here.
def new_register(request, id):
    if request.user.is_authenticated:
        project = Project.objects.get(pk=id)
        return render(request,
                      'budget_evaluation_register/pages/form.html',
                      {'project': project})


def details(request, id):
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        details = get_object_or_404(Project, pk=id)
        return render(
            request,
            'budget_evaluation_register/pages/reports_details.html',
            {'details': details, 'user': user_profile}
        )


def add_project(request):
    if request.user.is_authenticated:
        new_project = Project()
        new_project.evaluated = request.user.username
        new_project.project_number = request.POST.get('project_number')
        new_project.project_name = request.POST.get('project_name')
        new_project.client_name = request.POST.get('client')
        new_project.save()

        new_errors = Project_errors()
        new_errors.evaluated = request.user.username
        new_errors.project_number = request.POST.get('project_number')
        new_errors.project_name = request.POST.get('project_name')
        new_errors.client_name = request.POST.get('client')
        new_errors.save()

    return HttpResponseRedirect(reverse('reports'))


def add_report(request, id):
    if request.user.is_authenticated:
        report = Project.objects.get(pk=id)
        report.documentation = request.POST.get('documentation')
        report.reason_documentation = request.POST.get(
            'reason_documentation')
        report.material_list = request.POST.get('material_list')
        report.reason_material_list = request.POST.get(
            'reason_material_list')
        report.price = request.POST.get('price')
        report.reason_price = request.POST.get('reason_price')
        report.layout = request.POST.get('layout')
        report.reason_layout = request.POST.get('reason_layout')
        report.network = request.POST.get('network')
        report.reason_network = request.POST.get('reason_network')
        report.tecnical_offer = request.POST.get('tecnical_offer')
        report.reason_tecnical_offer = request.POST.get(
            'reason_tecnical_offer')
        report.commercial_offer = request.POST.get('commercial_offer')
        report.reason_commercial_offer = request.POST.get(
            'reason_commercial_offer')
        report.save()

        new_errors = Project_errors.objects.get(pk=id)
        new_errors.documentation = request.POST.get('documentation')
        new_errors.reason_documentation = request.POST.get(
            'reason_documentation')
        new_errors.material_list = request.POST.get('material_list')
        new_errors.reason_material_list = request.POST.get(
            'reason_material_list')
        new_errors.price = request.POST.get('price')
        new_errors.reason_price = request.POST.get('reason_price')
        new_errors.layout = request.POST.get('layout')
        new_errors.reason_layout = request.POST.get('reason_layout')
        new_errors.network = request.POST.get('network')
        new_errors.reason_network = request.POST.get('reason_network')
        new_errors.tecnical_offer = request.POST.get('tecnical_offer')
        new_errors.reason_tecnical_offer = request.POST.get(
            'reason_tecnical_offer')
        new_errors.commercial_offer = request.POST.get('commercial_offer')
        new_errors.reason_commercial_offer = request.POST.get(
            'reason_commercial_offer')
        new_errors.save()

        return HttpResponseRedirect(reverse('reports'))


def delete(request, id):
    if request.user.is_authenticated:
        report = Project.objects.get(id=id)
        report.delete()
        return HttpResponseRedirect(reverse('reports'))


def finish(request, id):
    if request.user.is_authenticated:
        report = Project.objects.get(id=id)
        report.finished = True
        report.save()
        return HttpResponseRedirect(reverse('reports'))


def analyzed_documentation(request, id):
    if request.user.is_authenticated:
        report = Project.objects.get(id=id)
        report.documentation = 'correct'
        report.save()
        # url = 'reports/details/' + str(report.id)
        return HttpResponseRedirect(reverse('details', kwargs={'id': report.id}))


def analyzed_material_list(request, id):
    if request.user.is_authenticated:
        report = Project.objects.get(id=id)
        report.material_list = 'correct'
        report.save()
        # url = 'reports/details/' + str(report.id)
        return HttpResponseRedirect(reverse('details', kwargs={'id': report.id}))


def analyzed_price(request, id):
    if request.user.is_authenticated:
        report = Project.objects.get(id=id)
        report.price = 'correct'
        report.save()
        # url = 'reports/details/' + str(report.id)
        return HttpResponseRedirect(reverse('details', kwargs={'id': report.id}))


def analyzed_layout(request, id):
    if request.user.is_authenticated:
        report = Project.objects.get(id=id)
        report.layout = 'correct'
        report.save()
        # url = 'reports/details/' + str(report.id)
        return HttpResponseRedirect(reverse('details', kwargs={'id': report.id}))


def analyzed_network(request, id):
    if request.user.is_authenticated:
        report = Project.objects.get(id=id)
        report.network = 'correct'
        report.save()
        # url = 'reports/details/' + str(report.id)
        return HttpResponseRedirect(reverse('details', kwargs={'id': report.id}))


def analyzed_tecnical_offer(request, id):
    if request.user.is_authenticated:
        report = Project.objects.get(id=id)
        report.tecnical_offer = 'correct'
        report.save()
        # url = 'reports/details/' + str(report.id)
        return HttpResponseRedirect(reverse('details', kwargs={'id': report.id}))


def analyzed_commercial_offer(request, id):
    if request.user.is_authenticated:
        report = Project.objects.get(id=id)
        report.commercial_offer = 'correct'
        report.save()
        # url = 'reports/details/' + str(report.id)
        return HttpResponseRedirect(reverse('details', kwargs={'id': report.id}))


def to_analyze_documentation(request, id):
    if request.user.is_authenticated:
        report = Project.objects.get(id=id)
        report.documentation = 'analyzing'
        report.save()
        # url = 'reports/details/' + str(report.id)
        return HttpResponseRedirect(reverse('details', kwargs={'id': report.id}))


def to_analyze_material_list(request, id):
    if request.user.is_authenticated:
        report = Project.objects.get(id=id)
        report.material_list = 'analyzing'
        report.save()
        # url = 'reports/details/' + str(report.id)
        return HttpResponseRedirect(reverse('details', kwargs={'id': report.id}))


def to_analyze_price(request, id):
    if request.user.is_authenticated:
        report = Project.objects.get(id=id)
        report.price = 'analyzing'
        report.save()
        # url = 'reports/details/' + str(report.id)
        return HttpResponseRedirect(reverse('details', kwargs={'id': report.id}))


def to_analyze_layout(request, id):
    if request.user.is_authenticated:
        report = Project.objects.get(id=id)
        report.layout = 'analyzing'
        report.save()
        # url = 'reports/details/' + str(report.id)
        return HttpResponseRedirect(reverse('details', kwargs={'id': report.id}))


def to_analyze_network(request, id):
    if request.user.is_authenticated:
        report = Project.objects.get(id=id)
        report.network = 'analyzing'
        report.save()
        # url = 'reports/details/' + str(report.id)
        return HttpResponseRedirect(reverse('details', kwargs={'id': report.id}))


def to_analyze_tecnical_offer(request, id):
    if request.user.is_authenticated:
        report = Project.objects.get(id=id)
        report.tecnical_offer = 'analyzing'
        report.save()
        # url = 'reports/details/' + str(report.id)
        return HttpResponseRedirect(reverse('details', kwargs={'id': report.id}))


def to_analyze_commercial_offer(request, id):
    if request.user.is_authenticated:
        report = Project.objects.get(id=id)
        report.commercial_offer = 'analyzing'
        report.save()
        # url = 'reports/details/' + str(report.id)
        return HttpResponseRedirect(reverse('details', kwargs={'id': report.id}))
