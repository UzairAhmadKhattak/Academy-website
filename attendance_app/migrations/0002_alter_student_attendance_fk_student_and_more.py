# Generated by Django 4.0.2 on 2022-10-03 09:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_attendance',
            name='fk_student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance_app.student'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='fk_teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
