from django import forms

class FormContactServicePipedrive(forms.Form):
    name = forms.CharField(max_length=55, widget=forms.TextInput(
        attrs={
            "id": "name",
            "name": "name",
            "class": "form-control",
            "placeholder": "nome"
        }
    ))
    cpf = forms.CharField(max_length=14, widget=forms.TextInput(
        attrs={
            "id": "cpf",
            "name": "cpf",
            "class": "form-control",
            "placeholder": "000.000.000-00"
        }
    ))
    cnpj = forms.CharField(max_length=18, widget=forms.TextInput(
        attrs={
            "id": "cnpj",
            "name": "cnpj",
            "class": "form-control",
            "placeholder": "00.000.000/0000-00"
        }
    ))
    whatsapp = forms.CharField(max_length=55, widget=forms.TextInput(
        attrs={
            "id": "whatsapp",
            "name": "whatsapp",
            "class": "form-control",
            "placeholder": "(00) 9 9999-9999"
        }
    ))
    email = forms.EmailField(max_length=55, widget=forms.EmailInput(
        attrs={
            "id": "email",
            "name": "email",
            "class": "form-control",
            "placeholder": "seu@email.com"
        }
    ))
    