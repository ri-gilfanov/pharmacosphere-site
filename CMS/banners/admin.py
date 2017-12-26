from django.contrib import admin
from .models import TopBanner, SideBanner


class AbsBannerAdmin(admin.ModelAdmin):
    list_display = ('name', 'company',)
    search_fields = ('name', 'company__name',)


@admin.register(TopBanner)
class TopBannerAdmin(AbsBannerAdmin):
    pass


@admin.register(SideBanner)
class SideBannerAdmin(AbsBannerAdmin):
    pass
