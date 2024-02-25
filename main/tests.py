from datetime import datetime
from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from cuidaMe.forms import ClienteProfileForm, CuidadorProfileForm
from main.models import Cliente, Cuidador

class ProfileViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
    def test_my_profile_detail_view(self):
        is_logged = self.client.login(username='testuser', password='testpassword')
        self.assertTrue(is_logged)
        
        response = self.client.get(reverse('my_profile_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/my_profile_detail.html')
        self.assertEqual(response.context['user'], self.user)
    
    def tearDown(self):
        self.user.delete()
        

class ProfileDetailViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
    def test_my_profile_detail_view(self):
        is_logged = self.client.login(username='testuser', password='testpassword')
        self.assertTrue(is_logged)
        
        response = self.client.get(reverse('profile_detail', args=[self.user.id]))
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/profile_detail.html')
        self.assertEqual(response.context['user'], self.user)
    
    def tearDown(self):
        self.user.delete()

class EditProfileViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        
    def test_edit_profile_cliente(self):
        self.cliente = Cliente.objects.create(user=self.user, apellidos='Test Apellidos', tipo_dependencia='personaSolitaria')
        
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('edit_profile'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/edit_profile.html')
        self.assertIsInstance(response.context['form'], ClienteProfileForm)
        
        form_data = {
            'apellidos': 'Apellido Ejemplo',
            'tipo_dependencia': 'enfermedad',
        }
        form = ClienteProfileForm(data=form_data)

        self.assertTrue(form.is_valid())
        response = self.client.post(reverse('edit_profile'), form_data)
        self.assertEqual(response.status_code, 302)

        self.cliente.refresh_from_db()

        self.assertEqual(self.cliente.apellidos, 'Apellido Ejemplo')
        self.assertEqual(self.cliente.tipo_dependencia, 'enfermedad')
        
        self.cliente.delete()
        
    def test_edit_profile_cuidador(self):
        
        self.cuidador = Cuidador.objects.create(user=self.user, dni='12345678A', numero_seguridad_social='1234567890A', fecha_nacimiento='1990-01-01', formacion='Formacion', experiencia='Experiencia', tipo_publico_dirigido='Tipo de publico')
        
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('edit_profile'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/edit_profile.html')
        self.assertIsInstance(response.context['form'], CuidadorProfileForm)
        
        form_data = {
            'dni': 'Apellido nuevo',
            'numero_seguridad_social': '0004567890A',
            'fecha_nacimiento': '2002-11-22',
            'formacion': 'Test formacion',
            'experiencia': 'Ninguna',
            'tipo_publico_dirigido': 'Abuelos'
        }
        form = CuidadorProfileForm(data=form_data)
        
        self.assertTrue(form.is_valid())
        response = self.client.post(reverse('edit_profile'), form_data)
        
        self.assertEqual(response.status_code, 302)
        self.cuidador.refresh_from_db()
        self.assertEqual(self.cuidador.dni, form_data['dni'])
        self.assertEqual(self.cuidador.numero_seguridad_social, form_data['numero_seguridad_social'])
        self.assertEqual(self.cuidador.fecha_nacimiento, datetime.strptime(form_data['fecha_nacimiento'], '%Y-%m-%d').date())
        self.assertEqual(self.cuidador.formacion, form_data['formacion'])
        self.assertEqual(self.cuidador.experiencia, form_data['experiencia'])
        self.assertEqual(self.cuidador.tipo_publico_dirigido, form_data['tipo_publico_dirigido'])
        
        self.cuidador.delete()
        
    def tearDown(self):
            self.user.delete()
            
