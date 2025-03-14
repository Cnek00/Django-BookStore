# Generated by Django 5.1.5 on 2025-02-10 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Kitap Adı')),
                ('author', models.CharField(max_length=255, verbose_name='Yazar')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Açıklama')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Fiyat')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='book_covers/', verbose_name='Kapak Resmi')),
                ('stock', models.PositiveIntegerField(default=0, verbose_name='Stok Miktarı')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Eklenme Tarihi')),
            ],
        ),
    ]
