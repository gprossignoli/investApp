from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from profiles.business.models import UserProfile


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = UserCreationForm.Meta.fields + ('email', )


class AuthForm(AuthenticationForm):
    class Meta:
        model = UserProfile
        fields = UserCreationForm.Meta.fields
