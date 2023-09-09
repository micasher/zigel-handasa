# Generated by Django 4.2.4 on 2023-09-06 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0006_remove_accountingdoc_base_price_proposal_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountingdoc',
            name='childs',
        ),
        migrations.CreateModel(
            name='AccountingDocRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='accounting.accountingdoc')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='childs', to='accounting.accountingdoc')),
            ],
            options={
                'unique_together': {('parent', 'child')},
            },
        ),
        migrations.AddField(
            model_name='accountingdoc',
            name='based_on',
            field=models.ManyToManyField(blank=True, related_name='related_to', through='accounting.AccountingDocRelation', to='accounting.accountingdoc'),
        ),
    ]
