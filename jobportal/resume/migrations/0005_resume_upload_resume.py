# Generated by Django 5.0.4 on 2024-05-02 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0004_alter_resume_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='upload_resume',
            field=models.FileField(null=True, upload_to='resume'),
        ),
    ]