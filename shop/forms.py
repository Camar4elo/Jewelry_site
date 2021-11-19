from django import forms


class ContactMe(forms.Form):
    name = forms.CharField(label='Ваше имя:', required=True,
                           widget=forms.TextInput
                           (attrs={'class': 'contact-form'}))
    phone_number = forms.CharField(label='Ваш номер телефона:', required=True,
                                   widget=forms.TextInput
                                   (attrs={'class': 'contact-form'}))
    message = forms.CharField(label='Сообщение:', required=True,
                              max_length=1500, widget=forms.Textarea
                              (attrs={'class': 'contact-form',
                               'style': 'line-height: 20px'}))
