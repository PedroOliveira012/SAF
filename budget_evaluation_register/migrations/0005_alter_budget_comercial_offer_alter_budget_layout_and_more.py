# Generated by Django 4.2.3 on 2023-10-06 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budget_evaluation_register', '0004_alter_budget_material_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='comercial_offer',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='layout',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='network',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='price',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='budget',
            name='tecnical_offer',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
