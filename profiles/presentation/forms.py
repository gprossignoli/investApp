from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from markets.business.markets_service import MarketsService
from profiles.business.models import UserProfile
from utils.exceptions import SymbolNotFoundError


class RegisterForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = UserCreationForm.Meta.fields + ('email', )


class AuthForm(AuthenticationForm):
    class Meta:
        model = UserProfile
        fields = UserCreationForm.Meta.fields


class UserProfileUpdateForm(ModelForm):
    class Meta:
        model = UserProfile

        fields = ['username', 'email', 'fav_index']

    def clean(self):
        cleaned_data = super(UserProfileUpdateForm, self).clean()
        fav_index = cleaned_data.get('fav_index')
        try:
            MarketsService().get_symbol(ticker=fav_index)
        except SymbolNotFoundError:
            self.add_error(None, ValidationError('El indice favorito debe ser el ticker de un mercado valido'))
        return cleaned_data
