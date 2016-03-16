from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Reader


class ReaderForm(AuthenticationForm):
    username = forms.CharField(max_length=30)

    class Meta:
        model = Reader
        fields = ('username', 'password')


class PictureForm(forms.ModelForm):
    picture = forms.ImageField()

    class Meta:
        model = Reader
        fields = ('picture',)


class ReaderCreationForm(forms.ModelForm):
    error_messages = {
        'duplicate_username': "A user with that username already exists.",
        'password_mismatch': "The two password fields didn't match.",
    }
    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'id': 'registration_username'}),
                               max_length=30, help_text="Required. 30 characters or fewer. Letters, and digits.",
                               error_messages={'invalid': "This value may contain only letters, and numbers"})
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(attrs={'id': 'registration_password'}))
    password2 = forms.CharField(label="Password confirmation",
                                widget=forms.PasswordInput(attrs={'id': 'registration_password2'}),
                                help_text="Enter the same password as above, for verification.")

    class Meta:
        model = Reader
        fields = ('username', 'password', 'password2')

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            Reader.objects.get(username=username)
        except Reader.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(ReaderCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
