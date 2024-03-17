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
    
class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Comment
        fields = [ 'text']
        labels = {
            'text': 'Comentario'
        }

