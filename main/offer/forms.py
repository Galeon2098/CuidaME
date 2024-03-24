from django import forms
from .models import Offer
from main.offer.choices import POB_CHOICES

class OfferForm(forms.ModelForm):
    TYPE_CHOICES = (
        ('CO', 'COMPAÑÍA'),
        ('CU', 'CUIDADO'),
        ('TR', 'TRANSPORTE'),
        ('DO', 'COMPRA A DOMICILIO'),
        ('OT', 'OTROS')
    )

    CLIENT_CHOICES = (
        ('DF', 'DISCAPACIDAD FÍSICA'), 
        ('DM', 'DISCAPACIDAD MENTAL'), 
        ('NI', 'NIÑOS'), 
        ('AN', 'ANCIANOS'), 
        ('OT', 'OTROS') 
    )

    title = forms.CharField(label='Título')
    offer_type = forms.ChoiceField(label='Tipo de oferta', choices=TYPE_CHOICES, initial='OT')
    client = forms.ChoiceField(label='Tipo de cliente', choices=CLIENT_CHOICES, initial='OT')
    description = forms.CharField(label='Descripción', required=True, widget=forms.Textarea(attrs={'rows': 10, 'cols': 70}))
    price_per_hour = forms.DecimalField(label='Precio por hora', max_digits=10, decimal_places=2)
    address = forms.CharField(label='Dirección')
    poblacion = forms.ChoiceField(label='Población', choices=POB_CHOICES, initial='Sevilla')
    
    class Meta:
        model = Offer

        fields = ['title', 'offer_type', 'client', 'description', 'price_per_hour', 'address','poblacion']
        widgets = {
            'price_per_hour': forms.NumberInput(attrs={'step': '0.01'})
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

class ReviewForm(forms.Form):
    valoration = forms.IntegerField(
        widget=forms.RadioSelect(
            choices=[
                (5, 'Muy bueno'), (4, 'Bueno'),
                (3, 'Normal'), (2, 'Malo'), (1, 'Muy Malo')
            ]
        ),
        label='Valoración'
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 6, 'cols': 50}), label='Descripción de la revisión'
    )
