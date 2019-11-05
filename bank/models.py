from django.db import models

# Create your models here.


# class Wnioski(models.Model):
#     rodzaj_weryfikacji = models.CharField(max_length=14)
#     decyzja = models.CharField(max_length=10)
#     kredyt = models.CharField(max_length=20)
#     kwota = models.DecimalField(max_digits=10, decimal_places=2)
#     id_klienta = models.ForeignKey('Klienci', on_delete=models.CASCADE)
#     id_pracownika = models.ForeignKey('Pracownicy', on_delete=models.CASCADE)
#     wsk_przeterminowania = models.DecimalField(max_digits=5, decimal_places=2)
#     wsparcie_innej_komorki = models.CharField(max_length=3)
#     firma_niepotwierdzajaca = models.CharField(max_length=3)


class Klienci(models.Model):
    id_klienta = models.AutoField(primary_key=True)


class KlienciIndywidualni(models.Model):
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=20)
    pesel = models.CharField(max_length=11)
    miejsce_zamieszkania = models.CharField(max_length=30)
    miejsce_zameldowania = models.CharField(max_length=30)
    id_klienta = models.ForeignKey('Klienci', on_delete=models.CASCADE)


class KlienciFirmy(models.Model):
    nazwa_firmy = models.CharField(max_length=20)
    nip = models.CharField(max_length=14)
    siedziba = models.CharField(max_length=20)
    id_klienta = models.ForeignKey('Klienci', on_delete=models.CASCADE)
