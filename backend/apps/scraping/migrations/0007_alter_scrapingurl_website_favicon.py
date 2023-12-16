# Generated by Django 4.2.8 on 2023-12-16 10:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("scraping", "0006_scrapingurl_website_favicon_scrapingurl_website_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="scrapingurl",
            name="website_favicon",
            field=models.CharField(
                blank=True,
                default="https://tenplestay.kro.kr/logo.svg",
                help_text="제출한 url의 favicon의 경로를 저장한 field 입니다.",
                max_length=200,
                null=True,
                verbose_name="favicon url",
            ),
        ),
    ]
