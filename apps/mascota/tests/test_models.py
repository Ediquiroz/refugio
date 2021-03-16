from django.test import TestCase
from apps.mascota.models import Mascota, Vacuna

class MascotaTestCase(TestCase):
    def setUp(self):
        Mascota.objects.create(nombre="lola", sexo="Femenino", edad_aproximada=2, fecha_rescate="2021-02-02")
        Mascota.objects.create(nombre="lupito", sexo="Femenino", edad_aproximada=1, fecha_rescate="2021-01-01")
    
    def test_mascotas_tienen_sexo(self):
        """Las mascotas pueden tener el sexo correctamente definido"""
        lola = Mascota.objects.get(sexo="Femenino")
        lupito = Mascota.objects.get(sexo="Femenino")
        self.assertEqual(lola.sexo, lupito.sexo, "Femeni")
        self.assertEqual(lupito.sexo, lola.sexo, "Femeni")
