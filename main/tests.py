from datetime import date, datetime
from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from cuidaMe.forms import ClienteProfileForm, CuidadorProfileForm, ClienteRegistrationForm, CuidadorRegistrationForm
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
        
        self.cuidador = Cuidador.objects.create(user=self.user, dni='12345678A', numero_seguridad_social='12345678900A', fecha_nacimiento='1990-01-01', formacion='Formacion', descripcion='Descripcion', tipo_publico_dirigido='NI')
        
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('edit_profile'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/edit_profile.html')
        self.assertIsInstance(response.context['form'], CuidadorProfileForm)
        
        form_data = {
            'dni': '12345678B',
            'numero_seguridad_social': '00045678900A',
            'fecha_nacimiento': '2002-11-22',
            'formacion': 'Test formacion',
            'descripcion': 'Ninguna',
            'tipo_publico_dirigido': 'AN'
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
        self.assertEqual(self.cuidador.descripcion, form_data['descripcion'])
        self.assertEqual(self.cuidador.tipo_publico_dirigido, form_data['tipo_publico_dirigido'])
        
        self.cuidador.delete()
        
    def tearDown(self):
            self.user.delete()
            

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
            'descripcion': 'Descripción cuidador',
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
            'descripcion': 'some_description',
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
            'descripcion': 'some_description',
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

