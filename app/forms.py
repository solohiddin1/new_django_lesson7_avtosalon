from django import forms
from .models import Avtosalon, Brand, Cars
import re
from django.core.exceptions import ValidationError

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


class AvtosalonForm(forms.ModelForm):
    class Meta:
        model = Avtosalon
        fields = ['title','context','email','phone','address','image']

        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'context':forms.Textarea(attrs={'class':'form-control','rows':5}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'phone':forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.TextInput(attrs={'class':'form-control'}),
            'image':forms.ClearableFileInput(attrs={'class':'form-control-file'})

        }
        
        label = {
            'title':'name',
            'context':'text',
            'email':'enter email',
            'phone':'phone number',
            'image':'upload image',
        }

    # def clean_title(self):
        # title = self.cleaned_data['title']
# 
        # if re.match(r'\d',title):
            # raise ValidationError('Title da raqam bolmasin!')
        # return title
    
    # def clean_email(self):
    #     email = self.cleaned_data['email']

    #     if re.match(r'[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+',email):
    #         raise ValidationError('Togri emalil kiriting!')
    #     return email
    
    # def clean_phone(self):
    #     phone = self.cleaned_data['phone']

    #     if re.match(r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$',phone):
    #         raise ValidationError('togri telefon raqam kiriting!')        
    #     return phone


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
    image = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={'class':'form-control-file'}),
            label='image'
            )