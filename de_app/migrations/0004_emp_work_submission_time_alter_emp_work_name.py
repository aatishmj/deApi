# Generated by Django 4.2.5 on 2023-09-22 15:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('de_app', '0003_alter_ad_data_drawing'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp_work',
            name='submission_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='emp_work',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='de_app.emp'),
        ),
    ]