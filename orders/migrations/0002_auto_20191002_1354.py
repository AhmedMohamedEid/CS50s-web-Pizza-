# Generated by Django 2.2.5 on 2019-10-02 13:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_type', models.CharField(choices=[('r', 'Regular'), ('s', 'Sicilian')], max_length=1)),
                ('item_size', models.CharField(choices=[('s', 'Small'), ('l', 'Lagre')], max_length=1)),
                ('num_topping', models.IntegerField()),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('r', 'Regular'), ('s', 'Sicilian')], max_length=1)),
                ('size', models.CharField(choices=[('s', 'Small'), ('l', 'Lagre')], max_length=1)),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pizza_price', to='orders.ItemPricing')),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='cateqgory',
        ),
        migrations.DeleteModel(
            name='MenuCategory',
        ),
        migrations.DeleteModel(
            name='MenuItem',
        ),
        migrations.AddField(
            model_name='menuitems',
            name='topping',
            field=models.ManyToManyField(blank=True, related_name='pizza_topping', to='orders.Topping'),
        ),
    ]
