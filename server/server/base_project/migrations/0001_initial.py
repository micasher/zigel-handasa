# Generated by Django 4.2.4 on 2023-08-31 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounting', '0001_initial'),
        ('comment', '0001_initial'),
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('total', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('last_comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.client')),
                ('comments', models.ManyToManyField(blank=True, to='comment.comment')),
                ('docs', models.ManyToManyField(blank=True, to='accounting.accountingdoc')),
            ],
        ),
    ]
