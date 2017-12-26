from django import forms
from .models import Ad, AdDraft


BooleanWidget = forms.Select(choices=((True, 'Да'), (False, 'Нет')))


class AdForm(forms.ModelForm):
    class Meta:
        fields = ('category', 'title', 'text', 'company', 'premium')
        model = Ad
        widgets = {'is_chosen': BooleanWidget}


class AdDraftForm(forms.ModelForm):
    class Meta:
        fields = ('category', 'title', 'text', 'company', 'is_ready')
        model = AdDraft
        widgets = {'is_ready': BooleanWidget}



class PublishedAdDraftForm(forms.ModelForm):
    class Meta:
        fields = ('category', 'title', 'text', 'company')
        model = AdDraft
