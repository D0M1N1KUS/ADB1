# Generated by Django 2.2.7 on 2019-11-04 23:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klienci',
            fields=[
                ('id_klienta', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='KlienciIndywidualni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=20)),
                ('nazwisko', models.CharField(max_length=20)),
                ('pesel', models.CharField(max_length=11)),
                ('miejsce_zamieszkania', models.CharField(max_length=30)),
                ('miejsce_zameldowania', models.CharField(max_length=30)),
                ('id_klienta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.Klienci')),
            ],
        ),
        migrations.CreateModel(
            name='KlienciFirmy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa_firmy', models.CharField(max_length=20)),
                ('nip', models.CharField(max_length=14)),
                ('siedziba', models.CharField(max_length=20)),
                ('id_klienta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.Klienci')),
            ],
        ),
    ]