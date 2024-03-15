from django import forms
from django.contrib.auth.models import User
from main.models import Cliente, Cuidador
from main.offer.choices import POB_CHOICES
import datetime, re

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class ClienteRegistrationForm(forms.ModelForm):
    # Añade campos adicionales de Cliente
    tipo_dependencia = forms.ChoiceField(label='Tipo de Dependencia', choices=Cliente.OPCIONES_DEPENDENCIA)
    poblacion = forms.ChoiceField(label='Población', choices=POB_CHOICES)  
    first_name = forms.CharField(label='Nombre', required=True)
    last_name = forms.CharField(label='Apellidos', required=True)
    tipo_dependencia = forms.ChoiceField(label='Tipo de Dependencia', choices=Cliente.OPCIONES_DEPENDENCIA, required=True)
    email = forms.EmailField(label='Email', required=True)

    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso. Elige otro nombre de usuario.")
        return username

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cd['password2']

    def save(self, commit=True):
            user = super(ClienteRegistrationForm, self).save(commit=False)
            user.set_password(self.cleaned_data['password'])
            if commit:
                user.save()
                # Guarda los campos adicionales de Cliente
                Cliente.objects.create(user=user, tipo_dependencia=self.cleaned_data['tipo_dependencia'])
            return user, Cliente

class CuidadorRegistrationForm(forms.ModelForm):

    dni = forms.CharField(label='DNI', max_length=20)
    numero_seguridad_social = forms.CharField(label='Número seguridad social', max_length=20)
    fecha_nacimiento = forms.DateField(
        label="Fecha de nacimiento",
        widget=forms.DateInput(attrs={'type': 'date'}),)
    formacion = forms.CharField(label="Formación")
    experiencia = forms.CharField(label="Experiencia")
    tipo_publico_dirigido = forms.CharField(label="Tipo de público al que te diriges", max_length=100)
    poblacion = forms.ChoiceField(label='Población', choices=POB_CHOICES)  
    # Añade campos adicionales de Cuidador
    dni = forms.CharField(label='DNI', max_length=20, required=True)
    numero_seguridad_social = forms.CharField(label='Número seguridad social', max_length=20, required=True)
    fecha_nacimiento = forms.DateField(
        label="Fecha de nacimiento",
        widget=forms.DateInput(attrs={'type': 'date'}),required=True)
    formacion = forms.CharField(label="Formación", required=True)
    experiencia = forms.CharField(label="Experiencia", required=True)
    tipo_publico_dirigido = forms.CharField(label="Tipo de público al que te diriges", max_length=100, required=True)

    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso. Elige otro nombre de usuario.")
        return username

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cd['password2']
    
    def clean_dni(self):
        dni = self.cleaned_data['dni']
        dni_regex = r'^\d{8}[a-zA-Z]$'
        
        if not re.match(dni_regex, dni):
            raise forms.ValidationError("El DNI no tiene un formato válido.")
        
        # Verifica si el DNI ya existe en la base de datos
        if Cuidador.objects.filter(dni=dni).exists():
            raise forms.ValidationError("Este DNI ya está registrado en el sistema.")
        return dni
    
    def clean_numero_seguridad_social(self):
        numero_seguridad_social = self.cleaned_data['numero_seguridad_social']
        nss_regex = r'^\d{12}$'
        if not re.match(nss_regex, numero_seguridad_social):
            raise forms.ValidationError("El número de seguridad social no tiene un formato válido.")
        if Cuidador.objects.filter(numero_seguridad_social=numero_seguridad_social).exists():
            raise forms.ValidationError("Este numero de seguridad social ya está registrado en el sistema.")
        return numero_seguridad_social
    
    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data['fecha_nacimiento']
        today = datetime.date.today()
        age = today.year - fecha_nacimiento.year - ((today.month, today.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
        if age < 18:
            raise forms.ValidationError("Debes tener al menos 18 años para registrarte como cuidador.")
        return fecha_nacimiento

    def save(self, commit=True):
            user = super(CuidadorRegistrationForm, self).save(commit=False)
            user.set_password(self.cleaned_data['password'])
            if commit:
                user.save()
                # Guarda los campos adicionales de Cliente
                Cuidador.objects.create(user=user, 
                                        dni=self.cleaned_data['dni'],
                                        numero_seguridad_social=self.cleaned_data['numero_seguridad_social'],
                                        fecha_nacimiento=self.cleaned_data['fecha_nacimiento'],
                                        formacion=self.cleaned_data['formacion'],
                                        experiencia=self.cleaned_data['experiencia'],
                                        tipo_publico_dirigido=self.cleaned_data['tipo_publico_dirigido'])
            return user, Cuidador
    
class ClienteProfileForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['apellidos', 'tipo_dependencia','poblacion']

class CuidadorProfileForm(forms.ModelForm):
    class Meta:
        model = Cuidador
        fields = ['dni', 'numero_seguridad_social', 'fecha_nacimiento', 'formacion', 'experiencia', 'tipo_publico_dirigido','poblacion']