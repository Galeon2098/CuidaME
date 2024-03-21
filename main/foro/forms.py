from django import forms

from .models import Thread, Comment

class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ['title','description']
        labels = {
            'title': 'Título',
            'description': 'Descripción'
        }
    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        description = cleaned_data.get("description")
        
        if title and len(title) > 75:
            raise forms.ValidationError("El título no puede tener más de 75 caracteres.")
        
        if description and len(description) > 300:
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
            if text and len(text) > 1000:
                self.add_error('text', "El comentario no puede tener más de 1000 caracteres.")
            return cleaned_data

