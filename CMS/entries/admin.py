from django.contrib import admin
from .models import Category, Entry, EntryDraft
from django.utils import timezone
from mptt.admin import DraggableMPTTAdmin, TreeRelatedFieldListFilter


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    pass


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category',)
    list_filter = (
        ('category', TreeRelatedFieldListFilter),
        'is_chosen',
    )
    raw_id_fields = ('creator', 'company',)


def create_or_update_entry(modeladmin, request, queryset):
    for draft in queryset:
        if draft.entry:
            entry = Entry.objects.get(id=draft.entry.id)
            entry.category = draft.category
            entry.company = draft.company
            entry.creator = draft.creator
            entry.is_anonymously = draft.is_anonymously
            entry.text = draft.text
            entry.title = draft.title
            entry.save()
            draft.pub_date=entry.pub_date
            draft.is_published = True
            draft.save()
        else:
            timezone_now = timezone.now()
            if draft.pub_date < timezone_now:
                draft.pub_date = timezone_now
            entry = Entry.objects.create(
                category=draft.category,
                company=draft.company,
                creator=draft.creator,
                is_anonymously = draft.is_anonymously,
                pub_date=draft.pub_date,
                text=draft.text,
                title=draft.title,
            )
            draft.entry = entry
            draft.is_published = True
            draft.save()
create_or_update_entry.short_description = 'Создать или обновить публикации по черновикам'


@admin.register(EntryDraft)
class EntryDraftAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'is_ready', 'is_published',)
    list_filter = ('category',)
    readonly_fields = ('is_published', 'entry',)
    raw_id_fields = ('creator', 'company', 'entry',)
    actions = [create_or_update_entry]

    def save_model(self, request, obj, form, change):
        obj.is_published = False
        obj.save()
