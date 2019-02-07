from django import forms

class EmailForm(forms.Form):
    reciever_address = forms.EmailField()
    email_content = forms.CharField(max_length=200)
