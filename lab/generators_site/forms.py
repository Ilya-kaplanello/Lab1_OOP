from django import forms

class Linear_generator(forms.Form):
    m = forms.IntegerField()
    a = forms.IntegerField()
    c = forms.IntegerField()
