from django import forms
from .models import Thread, Comment

class ThreadForm(forms.ModelForm):
    anonymous = forms.BooleanField(required=False, label='Publicar de forma anónima')
    class Meta:
        model = Thread
        fields = ['title','description']
        labels = {
            'title': 'Título',
            'description': 'Descripción'
        }
    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data.get('anonymous'):
            instance.author = None  # Si el usuario elige la opción anónima, no se establece un autor
        if commit:
            instance.save()
        return instance
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")
        if len(title) > 75:
            raise forms.ValidationError("El título no puede tener más de 75 caracteres.")
        if len(description) > 300:
            self.add_error('description', "La descripción no puede tener más de 300 caracteres.")
        return cleaned_data
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [ 'text']
        labels = {
            'text': 'Comentario'
        }
        def clean(self):
            cleaned_data = super().clean()
            text = cleaned_data.get("text")
            if len(text) > 1000:
                self.add_error('text', "El comentario no puede tener más de 1000 caracteres.")
            return cleaned_data

