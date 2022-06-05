from django import forms

class SignupForm(forms.Form):
    full_name=forms.CharField(
        widget=forms.TextInput(attrs={'class':'formControl'}),
        label="full_name",
        min_length=3,
        max_length=50,
        required=True
    )
    email=forms.EmailField(
        widget=forms.TextInput(attrs={'class':'formControl'}),
        label="email",
        required=True
    )
    password=forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'formControl'}),
        min_length=7,
        required=True
    )
    confirm_password= forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'formControl'}),
        min_length=7,
        required=True
    )

class LoginForm(forms.Form):
    email=forms.EmailField(
        widget=forms.TextInput(attrs={'class':'formControl'}),
        label="email",
        required=True
    )
    password=forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'formControl'}),
        label='password',
        required=True
    )

