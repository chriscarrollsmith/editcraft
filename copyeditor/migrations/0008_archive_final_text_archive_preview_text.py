# Generated by Django 5.0.1 on 2024-02-01 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("copyeditor", "0007_archive_tracker"),
    ]

    operations = [
        migrations.AddField(
            model_name="archive",
            name="final_text",
            field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="archive",
            name="preview_text",
            field=models.TextField(default=""),
        ),
    ]
