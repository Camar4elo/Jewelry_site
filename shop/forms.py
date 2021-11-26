from django import forms


class ContactMe(forms.Form):
    name = forms.CharField(max_length=40, required=True,
                           widget=forms.TextInput(attrs={'class': 'contact-form', 'placeholder': 'Ваше имя:'}),
                           label='')
    phone_number = forms.CharField(max_length=16, required=True,
                                   widget=forms.TextInput(attrs={'class': 'contact-form',
                                                                 'placeholder': 'Ваш номер телефона:'}),
                                   label='')
    message = forms.CharField(max_length=1500, required=True,
                              widget=forms.Textarea(attrs={'class': 'contact-form', 'style': 'line-height: 20px',
                                                           'placeholder': 'Напишите сообщение:'}),
                              label='')
