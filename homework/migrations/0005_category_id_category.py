# Generated by Django 4.2.1 on 2023-06-06 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0004_student_product_id_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='id_category',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='homework.student'),
        ),
    ]
