from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'contactus'}), max_length= 100)
    phone = forms.CharField(widget=forms.TextInput(attrs={'class' : 'contactus'}), max_length= 13)
    mail = forms.CharField(widget=forms.TextInput(attrs={'class' : 'contactus'}), max_length= 100)
    message = forms.CharField(widget=forms.Textarea(attrs={'class' : 'textarea'}), max_length= 2000)