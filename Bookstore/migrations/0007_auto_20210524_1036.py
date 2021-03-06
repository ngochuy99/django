# Generated by Django 3.1.7 on 2021-05-24 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bookstore', '0006_auto_20210524_1034'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='clothes_order',
            new_name='bookorder',
        ),
        migrations.RenameModel(
            old_name='electronics_order',
            new_name='clothesorder',
        ),
        migrations.RenameModel(
            old_name='book_order',
            new_name='electronicsorder',
        ),
        migrations.RemoveField(
            model_name='bookorder',
            name='clothes',
        ),
        migrations.RemoveField(
            model_name='clothesorder',
            name='electronics',
        ),
        migrations.RemoveField(
            model_name='electronicsorder',
            name='book',
        ),
        migrations.AddField(
            model_name='bookorder',
            name='book',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Bookstore.book'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clothesorder',
            name='clothes',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Bookstore.clothe'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='electronicsorder',
            name='electronics',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Bookstore.electronic'),
            preserve_default=False,
        ),
    ]
