from django import forms

class NewPostForm(forms.Form):
    text = forms.CharField(label='Message', max_length=200)

class ReplyForm(forms.Form):
    text = forms.CharField(label='Reply', max_length=200)