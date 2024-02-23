from django.db import models


class Project(models.Model):
    evaluator = models.CharField(max_length=20)
    evaluated = models.CharField(max_length=20)
    project_number = models.CharField(max_length=14)
    project_revision_history = models.IntegerField(default=0)
    project_name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=100)
    documentation = models.CharField(max_length=12)
    reason_documentation = models.CharField(
        max_length=255, null=True, default='N/A')
    material_list = models.CharField(max_length=12, null=True)
    reason_material_list = models.CharField(
        max_length=255, null=True, default='N/A')
    price = models.CharField(max_length=12, null=True)
    reason_price = models.CharField(max_length=255, null=True, default='N/A')
    layout = models.CharField(max_length=12, null=True)
    reason_layout = models.CharField(max_length=255, null=True, default='N/A')
    network = models.CharField(max_length=12, null=True)
    reason_network = models.CharField(max_length=255, null=True, default='N/A')
    tecnical_offer = models.CharField(max_length=12, null=True)
    reason_tecnical_offer = models.CharField(
        max_length=255, null=True, default='N/A')
    commercial_offer = models.CharField(max_length=12, null=True)
    reason_commercial_offer = models.CharField(
        max_length=255, null=True, default='N/A')
    comment = models.CharField(max_length=255, null=True, default='N/A')
    finished = models.BooleanField(null=False, default=False)


class Project_errors(models.Model):
    evaluator = models.CharField(max_length=20)
    evaluated = models.CharField(max_length=20)
    project_number = models.CharField(max_length=14)
    project_name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=100)
    documentation = models.CharField(max_length=12)
    reason_documentation = models.CharField(
        max_length=255, null=True, default='N/A')
    material_list = models.CharField(max_length=12, null=True)
    reason_material_list = models.CharField(
        max_length=255, null=True, default='N/A')
    price = models.CharField(max_length=12, null=True)
    reason_price = models.CharField(max_length=255, null=True, default='N/A')
    layout = models.CharField(max_length=12, null=True)
    reason_layout = models.CharField(max_length=255, null=True, default='N/A')
    network = models.CharField(max_length=12, null=True)
    reason_network = models.CharField(max_length=255, null=True, default='N/A')
    tecnical_offer = models.CharField(max_length=12, null=True)
    reason_tecnical_offer = models.CharField(
        max_length=255, null=True, default='N/A')
    commercial_offer = models.CharField(max_length=12, null=True)
    reason_commercial_offer = models.CharField(
        max_length=255, null=True, default='N/A')
    comment = models.CharField(max_length=255, null=True, default='N/A')
    finished = models.BooleanField(null=False, default=False)
