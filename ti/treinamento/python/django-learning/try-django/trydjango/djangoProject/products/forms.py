from django import forms
from .models import Products

class ProductModelForm(forms.ModelForm):
    title       = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "special",
                "id":"title_id",
                "placeholder":"AQUI"
                }
            ),
        label="AQUI",
        required=False
        )
    description = forms.CharField()
    price       = forms.DecimalField()
    
    class Meta:
        model = Products
        fields = [
            'title',
            'description',
            'price'
        ]

    def validation_title_field(self, *args, **kargs):
        title = self.cleaned_data.get("title")
        if title == "A dick":
            return title
        else:
            raise forms.ValidationError("This is not a valid title")

class DjangoProductsForm(forms.Form):
    title       = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "special",
                "id":"title_id",
                "placeholder":"AQUI"
                }
            ),
        label="AQUI",
        required=False
        )
    description = forms.CharField()
    price       = forms.DecimalField()

    def validation_title_field(self, *args, **kargs):
        title = self.cleaned_data.get("title")
        if title == "A dick":
            return title
        else:
            raise forms.ValidationError("This is not a valid title")