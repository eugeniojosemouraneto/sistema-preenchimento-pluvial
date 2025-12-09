from django import forms
from django.core.validators import FileExtensionValidator


class UploadArquivoForm(forms.Form):
    arquivo = forms.FileField(
        label="Selecione o arquivo CSV",
        validators=[FileExtensionValidator(allowed_extensions=["csv"])],
    )
