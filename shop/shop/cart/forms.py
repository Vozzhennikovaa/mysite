from django import forms
from .models import *
from main.models import Orders, Product
from django.forms import TextInput, CharField

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)



class LikeAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)


class OrdersbuyForm(forms.ModelForm):
   
    class Meta:
        model = Orders
        # exclude=[]
        fields = ["person", "email", "delivery",
                    "adress", "date", "time", "comment"]
        widgets = {
            "person": TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Введите ваше имя'
            }),
            "email": TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Введите вашу почту'
            }),
              "delivery": TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Введите способ доставки'
            }),
            "adress": TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Введите адрес доставки'
            }),
             "date": TextInput(attrs={
                'class': 'form-control'
            }),
             "time": TextInput(attrs={
                'class': 'form-control'
            }),
            "comment": TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Введите комментарий к заказу'
            })}

 