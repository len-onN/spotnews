# Generated by Django 4.2.3 on 2023-10-30 17:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0004_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="email",
            field=models.EmailField(max_length=200),
        ),
    ]
