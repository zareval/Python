import json
from django.test import TestCase
from django.urls import reverse

from inges_api.models import serie

class TestSerie(TestCase): 
    @classmethod
    def setUpTestData(cls):
        serie.objects.create(
            nombre='Serie1',
            genero='Drama',
            duracion=45,
            pais='EE. UU.',
            f_estreno='2022-01-01',
            trailer='https://www.youtube.com/trailer1',
            e_produccion='https://www.estudio.com/produccion1',
            poster='https://www.estudio.com/poster1',
            director='Director1',
        )

    def tearDown(self):
        pass

    def test_view_serie_listar(self):
        response = self.client.get('/api/peliculas/creacionSe')
        data = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(data), 0)
    def test_serieView_post(self):
        response = self.client.post(
            'api/peliculas/creacionSe',
            data={
                "genero": "ACcion",
                "duracion": 120,
                "director": "Akira",
                "pais": "japon",
                "protagonistas": [
                    3,
                    4,
                    6
                ],
                "f_estreno": "2024-05-06",
                "trailer": "https://www.ejemplo.com/trailer",
                "e_produccion": "https://www.ejemplo.com/produccion",
                "poster": "https://www.ejemplo.com/poster"
            }
        )


    def test_serieView_put(self):
        pkid = serie.objects.first().id
        data = {
            'nombre': 'SerieModificada',
            'genero': 'Acción',
            'duracion': 60,
            'pais': 'España',
            'f_estreno': '2023-12-31',
            'trailer': 'https://www.youtube.com/trailer-modificado',
            'e_produccion': 'https://www.estudio.com/produccion-modificada',
            'poster': 'https://www.estudio.com/poster-modificado',
            'director': 'DirectorModificado'
        }
        response = self.client.put(reverse('actualizacionSe', kwargs={'pkid': pkid}), data=json.dumps(data), content_type='application/json')
        self.assertIn(response.status_code, [200])

    def test_serieView_delete(self):
        pkid = serie.objects.first().id
        response = self.client.delete(reverse('eliminacionSe', kwargs={'pkid': pkid}))
        self.assertIn(response.status_code, [200])