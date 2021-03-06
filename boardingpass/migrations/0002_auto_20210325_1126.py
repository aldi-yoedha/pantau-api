# Generated by Django 2.2 on 2021-03-25 04:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boardingpass', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='pengguna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nik', models.CharField(max_length=16, null=True, unique=True)),
                ('nama', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now=True, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='tiket',
            old_name='Updated_at',
            new_name='updated_at',
        ),
        migrations.AlterField(
            model_name='tiket',
            name='kode_booking',
            field=models.CharField(blank=True, max_length=31, null=True),
        ),
        migrations.AlterField(
            model_name='tiket',
            name='status',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='tiket',
            name='nik',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boardingpass.pengguna', to_field='nik'),
        ),
    ]
