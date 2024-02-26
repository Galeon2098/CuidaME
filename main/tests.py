from datetime import date
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from cuidaMe.forms import ClienteRegistrationForm, CuidadorRegistrationForm
from .models import Cuidador


class TestClienteRegistro(TestCase):
    def setUp(self):
        self.register_url = reverse('registro_cliente')


    def test_registro_cliente(self):
        data = {
            'username': 'cliente1',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'cliente1@example.com',
            'tipo_dependencia': 'some_value',  
            'password': 'password123',
            'password2': 'password123',
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 200)

    def test_registro_cliente_datos_invalidos(self):
        data = {
            'username': 'cliente2',
            'first_name': 'Jane',
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 200) 
        self.assertFalse(User.objects.filter(username='cliente2').exists())

        # passwords no coinciden
        data = {
            'username': 'cliente2',
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'cliente2@example.com',
            'tipo_dependencia': 'some_value',
            'password': 'password123',
            'password2': 'password456',
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='cliente2').exists())


class TestCuidadorRegistro(TestCase):
    def setUp(self):
        self.register_url = reverse('registro_cuidador')
        self.user1 = User.objects.create_user(username='test_user1', password='password123')
        self.user2 = User.objects.create_user(username='test_user2', password='password456')

    def test_registro_cuidador(self):
        data = {
            'username': 'cuidador1',
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'cuidador1@example.com',
            'dni': '12345678A',
            'numero_seguridad_social': '987654321',
            'fecha_nacimiento': '1990-01-01',
            'formacion': 'Formación cuidador',
            'experiencia': 'Experiencia cuidador',
            'tipo_publico_dirigido': 'Tipo de público dirigido',
            'password': 'password123',
            'password2': 'password123',
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 200)

    def test_registro_cuidador_datos_invalidos(self):
        data = {
            'username': 'cuidador2',
            'first_name': 'John',
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 200) 
        self.assertFalse(User.objects.filter(username='cuidador2').exists())

        # passwords no coinciden
        data = {
            'username': 'cuidador2',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'cuidador2@example.com',
            'dni': '12345678A',
            'numero_seguridad_social': '1234567890',
            'fecha_nacimiento': '2000-01-01',
            'formacion': 'some_education',
            'experiencia': 'some_experience',
            'tipo_publico_dirigido': 'some_public',
            'password': 'password123',
            'password2': 'password456',  
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 200)  
        self.assertFalse(User.objects.filter(username='cuidador2').exists())


        fecha_nacimiento = date(1990, 1, 1)

        # Intenta crear dos cuidadores con el mismo número de DNI 
        cuidador1 = Cuidador.objects.create(user=self.user1, dni='12345678A', fecha_nacimiento=fecha_nacimiento,numero_seguridad_social= '1234567890')
        # Intenta crear un segundo cuidador con el mismo número de DNI 
        with self.assertRaises(Exception) as context:
            cuidador2 = Cuidador.objects.create(user=self.user2, dni='12345678A', fecha_nacimiento=fecha_nacimiento)

        # Comprueba que se produce un error al intentar crear un segundo cuidador con el mismo DNI 
        self.assertTrue('UNIQUE constraint failed' in str(context.exception))

    def test_registro_cuidador_nroseg_duplicado(self):
        data = {
            'username': 'cuidador2',
            'first_name': 'John',
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 200) 
        self.assertFalse(User.objects.filter(username='cuidador2').exists())

        # passwords no coinciden
        data = {
            'username': 'cuidador2',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'cuidador2@example.com',
            'dni': '12345678A',
            'numero_seguridad_social': '1234567890',
            'fecha_nacimiento': '2000-01-01',
            'formacion': 'some_education',
            'experiencia': 'some_experience',
            'tipo_publico_dirigido': 'some_public',
            'password': 'password123',
            'password2': 'password456',  
        }
        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 200)  
        self.assertFalse(User.objects.filter(username='cuidador2').exists())


        fecha_nacimiento = date(1990, 1, 1)

        # Intenta crear dos cuidadores con el mismo número de DNI 
        cuidador1 = Cuidador.objects.create(user=self.user1, dni='12345678A', fecha_nacimiento=fecha_nacimiento,numero_seguridad_social= '1234567890')
        # Intenta crear un segundo cuidador con el mismo número de DNI 
        with self.assertRaises(Exception) as context:
            cuidador2 = Cuidador.objects.create(user=self.user2, dni='12345658A', fecha_nacimiento=fecha_nacimiento,numero_seguridad_social= '1234567890')

        # Comprueba que se produce un error al intentar crear un segundo cuidador con el mismo DNI 
        self.assertTrue('UNIQUE constraint failed' in str(context.exception))


class TestClienteLogin(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='cliente1', password='password123')
        self.login_url = reverse('login')

    def test_login_cliente(self):
        data = {
            'username': 'cliente1',
            'password': 'password123',
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 302)

    def test_login_cliente_datos_invalidos(self):
        data = {
            'username': 'cliente2',
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='cliente2').exists())
        user = User.objects.create_user(username='cliente2', password='password123')
        data = {
            'username': 'cliente2',
            'password': 'incorrect_password', 
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 200)  



class TestCuidadorLogin(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='cuidador1', password='password123')
        self.login_url = reverse('login')

    def test_login_cuidador(self):
        data = {
            'username': 'cuidador1',
            'password': 'password123',
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 302)

    def test_login_cuidador_datos_invalidos(self):
        data = {
            'username': 'cuidador',
            'password': 'wrong_password'
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 200)  
        self.assertFalse(response.context['user'].is_authenticated)
        data = {
            'username': 'nonexistent_user',
            'password': 'password123'
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, 200)  
        self.assertFalse(response.context['user'].is_authenticated)

class TestScriptingProteccion(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='password123')

    def test_proteccion_scripting(self):
        response = self.client.get(reverse('profile_detail', kwargs={'user_id': self.user.id}), HTTP_USER_AGENT='Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)')
        self.assertEqual(response.status_code, 302)
