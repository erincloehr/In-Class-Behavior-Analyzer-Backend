# Generated by Django 2.1.5 on 2019-01-22 17:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20190122_1248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='id',
            field=models.UUIDField(default=uuid.UUID('dfa06cb2-24ed-4b3d-b0fd-0f287ae7a893'), editable=False, primary_key=True, serialize=False),
        ),
    ]