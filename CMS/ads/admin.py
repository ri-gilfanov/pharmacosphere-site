from django.contrib import admin
from .models import Ad, AdDraft


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_filter = ('category',)
    list_display = ('title', 'creator', 'company', 'premium',)
    raw_id_fields = ('creator', 'company',)


def create_or_update_ad(modeladmin, request, queryset):
    for draft in queryset:
        if draft.ad:
            ad = Ad.objects.get(id=draft.ad.id)
            ad.category = draft.category
            ad.company = draft.company
            ad.creator = draft.creator
            ad.text = draft.text
            ad.title = draft.title
            ad.save()
            draft.is_published = True
            draft.save()
        else:
            ad = Ad.objects.create(
                category=draft.category,
                company=draft.company,
                creator=draft.creator,
                text=draft.text,
                title=draft.title,
            )
            draft.ad = ad
            draft.is_published = True
            draft.save()
create_or_update_ad.short_description = 'Создать или обновить объявления по черновикам'


@admin.register(AdDraft)
class AdDraftAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'is_ready', 'is_published',)
    list_filter = ('category',)
    raw_id_fields = ('ad', 'creator', 'company',)
    readonly_fields = ('is_published', 'ad',)
    actions = [create_or_update_ad]

    def save_model(self, request, obj, form, change):
        obj.is_published = False
        obj.save()
