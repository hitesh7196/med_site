# Generated by Django 2.1.7 on 2019-04-28 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('med', '0004_stock_lead_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Declined', 'Declined')], default=None, max_length=15)),
                ('date_time', models.DateTimeField(verbose_name='date_placed')),
                ('order_id', models.CharField(blank=True, max_length=5, null=True)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicine_orders', to='med.medicine')),
                ('placed_by', models.ForeignKey(limit_choices_to={'is_supplier': False}, on_delete=django.db.models.deletion.CASCADE, related_name='order_placed', to='med.UserProfile')),
                ('placed_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_recieved', to='med.UserProfile')),
            ],
        ),
    ]
