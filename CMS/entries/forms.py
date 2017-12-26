from django import forms
from .models import Entry, EntryDraft


BooleanWidget = forms.Select(choices=((True, 'Да'), (False, 'Нет')))


class EntryForm(forms.ModelForm):
    class Meta:
        fields = ('category', 'title', 'image', 'text', 'company', 'pub_date', 'is_anonymously', 'is_chosen')
        model = Entry
        widgets = {'is_anonymously': BooleanWidget, 'is_chosen': BooleanWidget}


class EntryDraftForm(forms.ModelForm):
    class Meta:
        fields = ('category', 'title', 'image', 'text', 'company', 'pub_date', 'is_anonymously', 'is_ready')
        model = EntryDraft
        widgets = {'is_anonymously': BooleanWidget, 'is_ready': BooleanWidget}


class PublishedEntryDraftForm(forms.ModelForm):
    class Meta:
        fields = ('category', 'title', 'image', 'text', 'company', 'is_anonymously')
        model = EntryDraft
        widgets = {'is_anonymously': BooleanWidget}
