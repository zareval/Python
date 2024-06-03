import json
from django.test import TestCase
from django.urls import reverse

from inges_api.models import pelicula

class TestPelicula(TestCase): 
    @classmethod
    def setUpTestData(cls):
        pelicula.objects.create(
            nombre='Pelicula1',
            genero='Acción',
            duracion=120,
            pais='EE. UU.',
            f_estreno='2022-01-01',
            trailer='https://www.youtube.com/trailer1',
            e_produccion='https://www.estudio.com/produccion1',
            poster='https://www.estudio.com/poster1',
            director='Director1',
        )

    def tearDown(self):
        pass

    def test_view_pelicula_listar(self):
        response = self.client.get('/api/peliculas/creacionPe')
        data = json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(data), 0)


    def test_serieView_post(self):
        response = self.client.post(
            'api/peliculas/creacionPe',
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



    def test_peliView_put(self):
        pkid = pelicula.objects.first().id
        data = {
            'nombre': 'PeliculaModificada',
            'genero': 'Comedia',
            'duracion': 110,
            'pais': 'España',
            'f_estreno': '2023-12-31',
            'trailer': 'https://www.youtube.com/trailer-modificado',
            'e_produccion': 'https://www.estudio.com/produccion-modificada',
            'poster': 'https://www.estudio.com/poster-modificado',
            'director': 'DirectorModificado'
        }
        response = self.client.put(reverse('actualizacion', kwargs={'pkid': pkid}), data=json.dumps(data), content_type='application/json')
        self.assertIn(response.status_code, [200])

    def test_peliView_delete(self):
        pkid = pelicula.objects.first().id
        response = self.client.delete(reverse('eliminacion', kwargs={'pkid': pkid}))
        self.assertIn(response.status_code, [200])
