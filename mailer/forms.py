from datetime import datetime, timedelta

from django import forms
from django.utils import timezone

from mailer.models import SendOptions, Client, Message
from users.models import User


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name in ['send_period', 'mail_title', 'client_email']:
                field.widget.attrs['class'] = 'form-select'
            elif field_name == 'is_active':
                field.widget.attrs['class'] = 'form'
            else:
                field.widget.attrs['class'] = 'form-control'


class SendOptionsForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = SendOptions
        exclude = ('interval_try', 'options_owner', 'send_status',)


class ClientForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Client
        exclude = ('client_owner',)


class MessageForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Message
        exclude = ('message_owner',)


class UsersForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ('is_active',)


class SendOptionsManagerForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = SendOptions
        fields = ('is_active',)
