from django import forms
from .models import User, UserDraft
from django.utils import timezone
from django.contrib.auth.password_validation import validate_password


class AbsUserForm(forms.ModelForm):
    birth_date = forms.DateField(
        label='Дата рождения',
        required=False,
        widget=forms.SelectDateWidget(
            years=tuple(
                range(timezone.now().year - 18, timezone.now().year - 101, -1)
            ),
        ),
    )
    image = forms.ImageField(
        label='Фотография или аватарка',
        required=False,
    )


class UserForm(AbsUserForm):
    class Meta:
        fields = ('last_name', 'first_name', 'patronymic', 'text', 'birth_date', 'image')
        model = User


class UserDraftForm(AbsUserForm):
    class Meta:
        fields = ('last_name', 'first_name', 'patronymic', 'text', 'birth_date', 'image')
        model = UserDraft
