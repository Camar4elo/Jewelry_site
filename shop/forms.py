from django import forms


class ContactMe(forms.Form):
    name = forms.CharField(label='Ваше имя:', required=True)
    phone_number = forms.IntegerField(required=True,
                                      label='Ваш номер телефона:')
    message = forms.CharField(required=True, label='Сообщение:')
