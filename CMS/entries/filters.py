import django_filters
from .models import Entry
from .models import Category
from mptt.fields import TreeNodeChoiceField


class EntryFilter(django_filters.FilterSet):
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all(), method='filter_category')

    def __init__(self, *args, **kwargs):
        super(EntryFilter, self).__init__(*args, **kwargs)
        self.filters['category'].field_class = TreeNodeChoiceField

    def filter_category(self, queryset, name, value):
        return queryset.filter(category__in=value.get_descendants(include_self=True))

    class Meta:
        model = Entry
        fields = ['category']
