# Generated by Django 3.0.7 on 2020-07-02 03:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(blank=True, max_length=30, null=True, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('middle_name', models.CharField(blank=True, max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=6)),
                ('birth_date', models.DateField()),
                ('phone', models.CharField(max_length=50, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_1', models.CharField(max_length=255, null=True)),
                ('street_2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('zipcode', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Professional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_size', models.CharField(choices=[('meter', 'Meter'), ('foot', 'Foot')], default='meter', max_length=10)),
                ('weight_unit', models.CharField(choices=[('kg', 'kg'), ('lb', 'lb')], default='kg', max_length=2)),
                ('user_type', models.CharField(choices=[('Practitioner', 'Practitioner'), ('Staff', 'Staff')], default='Practitioner', max_length=15)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
                ('practitioner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='professional.Professional')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='billing_address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address_as_billing', to='professional.Address'),
        ),
        migrations.AddField(
            model_name='user',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='professional.Organization'),
        ),
        migrations.AddField(
            model_name='user',
            name='shipping_address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address_as_shipping', to='professional.Address'),
        ),
    ]
