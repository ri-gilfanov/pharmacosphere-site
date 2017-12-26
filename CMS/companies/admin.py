from django.contrib import admin
from .models import (
    Company, CompanyDraft,
    PubCompContact, SugCompContact,
    PubPhone, SugPhone,
    PubEmail, SugEmail,
)
from imagekit.admin import AdminThumbnail
import nested_admin


class PubPhoneInline(nested_admin.NestedTabularInline):
    extra = 0
    model = PubPhone
    sortable_field_name = 'position'


class PubEmailInline(nested_admin.NestedTabularInline):
    extra = 0
    model = PubEmail
    sortable_field_name = 'position'


class PubCompContactInline(nested_admin.NestedTabularInline):
    extra = 0
    inlines = [PubPhoneInline, PubEmailInline]
    model = PubCompContact
    sortable_field_name = 'position'


class SugPhoneInline(nested_admin.NestedTabularInline):
    extra = 0
    model = SugPhone
    sortable_field_name = 'position'


class SugEmailInline(nested_admin.NestedTabularInline):
    extra = 0
    model = SugEmail
    sortable_field_name = 'position'


class SugCompContactInline(nested_admin.NestedTabularInline):
    extra = 0
    inlines = [SugPhoneInline, SugEmailInline]
    model = SugCompContact
    sortable_field_name = 'position'


@admin.register(Company)
class CompanyAdmin(nested_admin.NestedModelAdmin):
    admin_thumbnail = AdminThumbnail(image_field='image_50x50')
    admin_thumbnail.short_description = 'логотип'
    admin_thumbnail.template = 'companies/admin/imagekit/admin_thumbnail.html'
    filter_horizontal = ('employees',)
    inlines = (PubCompContactInline,)
    list_display = (
        'admin_thumbnail',
        'name',
    )
    list_display_links = ('admin_thumbnail', 'name',)
    raw_id_fields = ('creator',)


@admin.register(CompanyDraft)
class CompanyDraftAdmin(nested_admin.NestedModelAdmin):
    admin_thumbnail = AdminThumbnail(image_field='image_50x50')
    admin_thumbnail.short_description = 'логотип'
    admin_thumbnail.template = 'companies/admin/imagekit/admin_thumbnail.html'
    inlines = (SugCompContactInline,)
    list_display = (
        'admin_thumbnail',
        'name',
        'last_modified',
        'is_published',
    )
    list_display_links = ('admin_thumbnail', 'name',)
    raw_id_fields = ('creator',)
    readonly_fields = ('is_published', 'company', 'last_modified',)
