from django import forms

class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    inquiry_type = forms.ChoiceField(choices=[('general', 'General'), ('support', 'Soporte')])
    message = forms.CharField(widget=forms.Textarea)
