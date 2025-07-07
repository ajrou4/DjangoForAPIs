from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# Form for creating a new user
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):  # Inheriting the inner Meta from UserCreationForm
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("name",)

# Form for updating an existing user
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
