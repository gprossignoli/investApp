from django import forms

from profiles.business.models import UserProfile


class RegisterForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    confirm_password = forms.CharField(max_length=32, widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'confirm_password',)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            self.add_error(field="password", error="Las contraseñas no coinciden")
        return cleaned_data

