from django.contrib import admin
from .models import User, UserDraft
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.admin import UserAdmin
from imagekit.admin import AdminThumbnail


@admin.register(User)
class UserAdmin(UserAdmin):
    form = UserChangeForm
    admin_thumbnail = AdminThumbnail(image_field='image_50x50')
    admin_thumbnail.short_description = 'фотография'
    admin_thumbnail.template = 'users/admin/imagekit/admin_thumbnail.html'
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Права доступа', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Важные даты', {'fields': ('last_login', 'date_joined',)}),
        ('Группы', {'fields': ('groups',)}),
        ('Личная информация', {
            'fields': (
                'last_name',
                'first_name',
                'patronymic',
                'birth_date',
                'image',
                'text',
            )
        }),
    )
    list_display = (
        'admin_thumbnail',
        'username',
        'last_name',
        'first_name',
        'patronymic',
        'is_staff',
        'is_active',
    )
    list_display_links = ('admin_thumbnail', 'username',)
    def get_formsets_with_inlines(self, request, obj=None):
        for inline in self.get_inline_instances(request, obj):
            if isinstance(inline, UserImageInline) and obj is None:
                continue
            yield inline.get_formset(request, obj), inline


def create_or_update_user_profile(modeladmin, request, queryset):
    for draft in queryset:
        if draft.user:
            user = User.objects.get(id=draft.user.id)
            user.last_name = draft.last_name
            user.first_name = draft.first_name
            user.patronymic = draft.patronymic
            user.text = draft.text
            user.birth_date = draft.birth_date
            user.save()
            draft.is_published = True
            draft.save()
        else:
            user = User.objects.create(
                last_name=draft.last_name,
                first_name=draft.first_name,
                patronymic=draft.patronymic,
                text=draft.text,
                birth_date=draft.birth_date,
            )
            draft.user = user
            draft.is_published = True
            draft.save()
create_or_update_user_profile.short_description = 'Создать или обновить объявления по черновикам'


@admin.register(UserDraft)
class UserDraftAdmin(admin.ModelAdmin):
    actions = [create_or_update_user_profile]
    admin_thumbnail = AdminThumbnail(image_field='image_50x50')
    admin_thumbnail.short_description = 'фотография'
    admin_thumbnail.template = 'users/admin/imagekit/admin_thumbnail.html'
    list_display = (
        'admin_thumbnail',
        'user',
        'last_name',
        'first_name',
        'patronymic',
        'image',
        'last_modified',
        'is_published',
    )
    list_display_links = ('admin_thumbnail', 'user',)
    raw_id_fields = ('user',)
    readonly_fields = ('is_published', 'last_modified',)

    def save_model(self, request, obj, form, change):
        obj.is_published = False
        obj.save()
