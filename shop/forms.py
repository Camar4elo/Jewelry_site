from django import forms


class ContactMe(forms.Form):
    name = forms.CharField(label='', required=True,
                           max_length=40, widget=forms.TextInput
                           (attrs={'class': 'contact-form',
                                   'placeholder': 'Ваше имя:'}))
    phone_number = forms.CharField(label='', required=True,
                                   widget=forms.TextInput
                                   (attrs={'class': 'contact-form',
                                           'placeholder': 'Ваш номер телефона:'}))
    message = forms.CharField(label='', required=True,
                              max_length=1500, widget=forms.Textarea
                              (attrs={'class': 'contact-form',
                               'style': 'line-height: 20px',
                                      'placeholder': 'Напишите сообщение:'}))
