from django import forms
from .models import AddProduct, Order,Products

class AddProductForm(forms.ModelForm):
    image = forms.ImageField(required=True, label='Product Image')
    class Meta:
        model = Products
        exclude = ['user']

        widgets={
            "title":forms.TextInput(attrs={'class': 'form-control d-flex justify-content-center'}),
            "price":forms.TextInput(attrs={'class': 'form-control d-flex justify-content-center'}),
            "varient":forms.TextInput(attrs={'class': 'form-control d-flex justify-content-center'}),
            "description":forms.TextInput(attrs={'class': 'form-control d-flex justify-content-center'}),
            
        }

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance    
    
    




class CheckoutForm(forms.Form):
    billing_address = forms.CharField(required=True)
    
    card_number = forms.IntegerField(required=True)
    card_expiry = forms.DateField(required=True)
    card_cvv = forms.IntegerField(required=True)   

    
     

# class OrderForm(forms.ModelForm):
#     class Meta:
#         model = Order
#         fields = []    