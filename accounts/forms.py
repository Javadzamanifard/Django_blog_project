from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model 

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # model = get_user_model()
        # fields = UserCreationForm.Meta.fields + (, )
        fields = ('username', 'email', )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # model = get_user_model()
        # fields = UserChangeForm.Meta.fields + (, )
        fields = ('username', 'email', )
