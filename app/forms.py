from django import forms
from .models import Avtosalon, Brand, Cars

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['title','context','brand_salon']

        widget = {
        'title':forms.TextInput(attrs={'class':'form-control'}),
        'context':forms.Textarea(attrs={'class':'form-control','rows':5}),
        'brand_salon':forms.Select(attrs={'class':'form-control'}),
        }

        label = {
            'title':'name',
            'context':'text',
            'brand_salon':'Avtosalon'
        }
        

class AvtosalonForm(forms.Form):
    title = forms.CharField(max_length = 40,
                           widget=forms.TextInput(attrs={'class':'form-control'}),
                           label='name')
    context = forms.CharField(label='text',required=False,
                              widget=forms.Textarea(
                                  attrs={'class':'form-control','rows':5}))
    email =forms.EmailField(required=False,widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    image = forms.ImageField(required=False,
                             label='upload image')



class CarForm(forms.Form):
    salon = forms.ModelChoiceField(queryset=Avtosalon.objects.all(),
                                        widget=forms.Select(attrs=
                                        {'class':'form-control'}))
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(),
                                        widget=forms.Select(attrs=
                                        {'class':'form-control'}))
    model = forms.CharField(max_length = 40,
                           widget=forms.TextInput(attrs={'class':'form-control'}),
                           label='name')
    price = forms.DecimalField(max_digits=12,decimal_places=2)
    year = forms.IntegerField()
    color = forms.CharField(max_length=30)