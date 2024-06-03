import json
from django.test import TestCase
from django.urls import reverse

from inges_api.models import persona

class TestPersona(TestCase): 
    @classmethod
    def setUpTestData(cls) -> None:
        mi_persona = persona.objects.create(
            nombre='Juan',
            nacionalidad='Colombiana',
            f_nacimiento='1990-01-01',
            biografia='es escritor'
        )

    
    def tearDown(self):
        pass

    def test_view_persona_listar(self):
        response=self.client.get('/api/peliculas/creacionDirector')
        data=json.loads(response.content.decode('utf-8'))

        self.assertEqual(response.status_code,200)
        self.assertGreater(len(data),0)


    def test_create_persona(self):
        response = self.client.post(
            '/api/peliculas/creacionDirector',
            data={
                'nombre': 'Goku',
                'nacionalidad':'peruano',
                'f_nacimiento':'2003-01-02',
                'biografia':'Nacido en peru'
            }
        )
        self.assertIn(response.status_code, [200, 201])
        filtered_persona = persona.objects.filter(nombre='Goku').first()
        self.assertEqual(filtered_persona.nacionalidad, 'peruano')


    def test_update_persona(self):
        mi_persona = persona.objects.create(
            nombre='Shikamaru',
            nacionalidad='Tierra del fuego',
            f_nacimiento='2003-01-05',
            biografia='ninja',
        )
        valid_persona = {
            'nombre': 'Shikamaru',
            'nacionalidad': 'Tierra del fuego',
            'f_nacimiento': '2003-01-05',
            'biografia': 'ninja',
        }
        url = reverse('actualizacion', kwargs={'pkid': mi_persona.id})
        valid_persona_json = json.dumps(valid_persona)
        response = self.client.put(url, valid_persona_json, content_type='application/json')
        self.assertIn(response.status_code, [200, 201])

    def test_delete_persona(self):
        mi_persona=persona.objects.create(
            nombre='Juan',
            nacionalidad='SUizo',
            f_nacimiento='2003-02-01',
            biografia='Archir'
        )
        url = reverse('eliminar', kwargs={'pkid': mi_persona.id})
        response=self.client.delete(url)
        self.assertEqual(response.status_code,200)
        self.assertFalse(persona.objects.filter(id=mi_persona.id).exists())


 



    






