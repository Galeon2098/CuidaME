from django import forms
from .models import Offer

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
    offer_type= forms.ChoiceField(label='Tipo de oferta', choices=TYPE_CHOICES, initial='OT')
    client = forms.ChoiceField(label='Tipo de cliente', choices=CLIENT_CHOICES, initial='OT')
    description = forms.CharField(label='Descripción', required=True,widget=forms.Textarea(attrs={'rows': 10, 'cols': 70}))
    price_per_hour = forms.DecimalField(max_digits=10,decimal_places=2)
    city = forms.CharField(label='Ciudad')                            
    
    class Meta:
        model = Offer
        fields = ['title','offer_type','client','description','price_per_hour','city']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)