from django import forms

from mailer.models import SendOptions, Client, Message


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name in ['send_period', 'send_status', 'client_email']:
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'


class SendOptionsForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = SendOptions
        exclude = ('send_next_try', 'options_owner', )


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('client_owner', )


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('message_owner', )
