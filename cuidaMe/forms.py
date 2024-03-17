from django import forms
from django.contrib.auth.models import User
from main.models import Cliente, Cuidador

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

class ClienteRegistrationForm(forms.ModelForm):
    # Añade campos adicionales de Cliente
    imagen_perfil = forms.ImageField(label='Imagen de perfil', required=False)
    tipo_dependencia = forms.ChoiceField(label='Tipo de Dependencia', choices=Cliente.OPCIONES_DEPENDENCIA)

    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'imagen_perfil']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
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
    imagen_perfil = forms.ImageField(label='Imagen de perfil', required=False)
    dni = forms.CharField(label='DNI', max_length=20)
    numero_seguridad_social = forms.CharField(label='Número seguridad social', max_length=20)
    fecha_nacimiento = forms.DateField(
        label="Fecha de nacimiento",
        widget=forms.DateInput(attrs={'type': 'date'}),)
    formacion = forms.CharField(label="Formación")
    descripcion = forms.CharField(label="Descripción", widget=forms.Textarea)
    tipo_publico_dirigido = forms.ChoiceField(label="Tipo de público al que te diriges", choices=Cuidador.PUBLICO_DIRIGIDO)

    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'imagen_perfil']

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    def save(self, commit=True):
            user = super(CuidadorRegistrationForm, self).save(commit=False)
            user.set_password(self.cleaned_data['password'])
            if commit:
                user.save()
                # Guarda los campos adicionales de Cliente
                Cuidador.objects.create(user=user, 
                                        imagen_perfil=self.cleaned_data['imagen_perfil'],
                                        dni=self.cleaned_data['dni'],
                                        numero_seguridad_social=self.cleaned_data['numero_seguridad_social'],
                                        fecha_nacimiento=self.cleaned_data['fecha_nacimiento'],
                                        formacion=self.cleaned_data['formacion'],
                                        descripcion=self.cleaned_data['descripcion'],
                                        tipo_publico_dirigido=self.cleaned_data['tipo_publico_dirigido'])
            return user, Cuidador
    
class ClienteProfileForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['imagen_perfil', 'apellidos', 'tipo_dependencia']

class CuidadorProfileForm(forms.ModelForm):
    class Meta:
        model = Cuidador
        fields = ['imagen_perfil', 'dni', 'numero_seguridad_social', 'fecha_nacimiento', 'formacion', 'descripcion', 'tipo_publico_dirigido']
