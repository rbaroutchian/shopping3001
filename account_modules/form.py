from django import forms
from django.core import validators
from django.core.exceptions import ValidationError


class RegistrationForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator()
        ]
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
            # validators.MinLengthValidator(8)  # اضافه شده برای امنیت بیشتر
        ]
    )
    confirm_password = forms.CharField(
        label='Confirm Password',  # اصلاح برچسب
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise ValidationError({
                'confirm_password': 'Passwords do not match'
            })
        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator()
        ]
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )


class ForgetPasswordForm(forms.Form):
    email = forms.EmailField(
        label='Email',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator()
        ]
    )


class VerifyCodeForm(forms.Form):
    verification_code = forms.CharField(
        label='Verification Code',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter verification code'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )


class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter new password'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
            validators.MinLengthValidator(8)  # اضافه شده برای امنیت بیشتر
        ]
    )
    confirm_new_password = forms.CharField(
        label='Confirm New Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm new password'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_new_password = cleaned_data.get('confirm_new_password')

        if new_password and confirm_new_password and new_password != confirm_new_password:
            raise ValidationError({
                'confirm_new_password': 'Passwords do not match'
            })
        return cleaned_data