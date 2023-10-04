from django.db import models


class Budget(models.Model):
    assessing = models.CharField(max_length=20)
    evaluated = models.CharField(max_length=20)
    project_number = models.CharField(max_length=14)
    project_name = models.CharField(max_length=255)
    client_name = models.CharField(max_length=100)
    documentation = models.CharField(max_length=6)
    documentation_comment = models.CharField(max_length=255, null=True)
    material_list = models.CharField(max_length=6)
    material_list_comment = models.CharField(max_length=255, null=True)
    price = models.CharField(max_length=6)
    price_comment = models.CharField(max_length=255, null=True)
    layout = models.CharField(max_length=6)
    layout_comment = models.CharField(max_length=255, null=True)
    network = models.CharField(max_length=6)
    network_comment = models.CharField(max_length=255, null=True)
    tecnical_offer = models.CharField(max_length=6)
    tecnical_offer_comment = models.CharField(max_length=255, null=True)
    comercial_offer = models.CharField(max_length=6)
    comercial_offer_comment = models.CharField(max_length=255, null=True)
    comment = models.CharField(max_length=255, null=True)
