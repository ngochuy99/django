# Generated by Django 3.2.3 on 2021-05-23 09:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Bookstore', '0005_alter_customer_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('type', models.TextField()),
                ('price', models.BigIntegerField()),
                ('inStock', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('image', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Clothe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('type', models.TextField()),
                ('price', models.BigIntegerField()),
                ('inStock', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('image', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Electronic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('type', models.TextField()),
                ('price', models.BigIntegerField()),
                ('inStock', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('image', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipper', models.TextField()),
                ('destination', models.TextField()),
                ('fee', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='cart_item',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cart_item',
            name='item',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Cart_Item',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='electronic',
            name='order',
            field=models.ManyToManyField(to='Bookstore.Order'),
        ),
        migrations.AddField(
            model_name='clothe',
            name='order',
            field=models.ManyToManyField(to='Bookstore.Order'),
        ),
        migrations.AddField(
            model_name='book',
            name='order',
            field=models.ManyToManyField(to='Bookstore.Order'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipment',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='Bookstore.shipment'),
            preserve_default=False,
        ),
    ]
