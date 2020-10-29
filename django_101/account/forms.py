from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(
        max_length=254,
        required=True,
        help_text='Enter a valid email address'
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        # user = User.objects.filter(email=email).exist()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                    'email is exist',
            )
        return email

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            ]


# Profile Form
class ProfileForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            ]
