from django import forms
from account_modules.models import User


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'phone_number', 'email', 'address',
                 'about_user']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'phone_number': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'about_user': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'id': 'message'
            })
        }

        labels = {
            'username': 'نام کاربری',
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'ایمیل',
            'phone_number': 'موبایل',
            'address': 'آدرس اصلی',
            'about_user': 'درباره شخص',
        }


class ChangePasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'رمز عبور جدید',
        'autocomplete': 'new-password',
        'style': 'border: 1px solid #6a11cb; padding: 10px; font-size: 14px;'

    }), label="رمز عبور جدید")
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'تأیید رمز عبور',
        'autocomplete': 'new-password',
        'style': 'border: 1px solid #2575fc; padding: 10px; font-size: 14px;'

    }), label="تأیید رمز عبور جدید")

    class Meta:
        model = User
        fields = ('password', 'confirm_password')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("رمز عبور و تأیید آن مطابقت ندارند.")
