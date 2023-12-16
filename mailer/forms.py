from django import forms

from mailer.models import SendOptions, Client


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name:
                field.widget.attrs['class'] = 'form-control'


class SendOptionsForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = SendOptions
        fields = '__all__'


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
