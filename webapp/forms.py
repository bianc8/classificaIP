from django import forms

class ClassiForm(forms.Form):
    ip = forms.CharField(max_length=15,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder' : '192.168.0.0'
            }))

class SubnetForm(forms.Form):
    ip = forms.CharField(max_length=15,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder' : '192.168.0.0'
            }))
    subnetmask = forms.CharField(max_length=15,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder' : '255.255.255.0'
            }))

class Subnet2Form(forms.Form):
    ip = forms.CharField(max_length=15,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder' : '192.168.0.0'
            }))
    n_subnet = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder' : '50'
            }))

class MessaInAnd(forms.Form):
    ip1 = forms.CharField(max_length=15,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder' : '192.168.0.0'
            }))
    ip2 = forms.CharField(max_length=15,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder' : '192.168.0.1'
            }))
    subnetmask = forms.CharField(max_length=15,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder' : '255.255.255.0'
            }))

class CidrForm(forms.Form):
    ip = forms.CharField(max_length=15,
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder' : '192.168.0.0'
            }))
    n_host = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'class':'form-control',
            'placeholder' : '500'
            }))
