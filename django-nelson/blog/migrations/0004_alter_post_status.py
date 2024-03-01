# Generated by Django 5.0.2 on 2024-03-01 14:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0003_post_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="status",
            field=models.CharField(
                choices=[("drf", "Draft"), ("pud", "Published"), ("trs", "Trash")],
                default="drf",
                max_length=3,
            ),
        ),
    ]