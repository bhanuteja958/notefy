from django import forms


class SignupForm(forms.Form):
    user_name=forms.CharField(
        widget=forms.TextInput(attrs={'class':'formControl'}),
        label="user_name",
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
        widget=forms.PasswordInput(attrs={'class':'formControl'},),
        label='password',
        required=True
    )

class NoteForm(forms.Form):
    title=forms.CharField(
        widget=forms.TextInput(attrs={'class':'editor__titleInput', 'placeholder': 'Title here'}),
        label="title",
        required=True
    )
    markdown=forms.CharField(
        widget=forms.Textarea(attrs={'class':'editor__markdownInput', 'placeholder': 'Markdown here'}),
        label="markdown",
        required=True
    )


