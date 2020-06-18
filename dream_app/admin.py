from django.contrib import admin
from django.contrib.admin import ModelAdmin, actions
from adminsortable2.admin import SortableAdminMixin
from .models import (Event, Player, Photo, Notice, SiteConfiguration, Video)


class AdminSite(admin.AdminSite):
    site_title = ('Harlem Dreams Basketball' )


class EventAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ("__unicode__", "timestamp")

        # model = Event
        admin.site.register(Event)


class VideoAdmin(SortableAdminMixin, admin.ModelAdmin):
    admin.site.register(Video)

class PlayerAdmin(SortableAdminMixin, admin.ModelAdmin):

    admin.site.register(Player)


class PhotoAdmin(admin.ModelAdmin):

    admin.site.register(Photo)

class NoticeAdmin(admin.ModelAdmin):
    admin.site.register(Notice)

    def has_add_permission(self, *args, **kwargs):
        return False if self.Notice.objects.count() > 0 else super().has_add_permission(request)


class SiteConfigurationAdmin(admin.ModelAdmin):
    admin.site.register(SiteConfiguration)

    def has_add_permission(self, *args, **kwargs):
        return False if self.SiteConfiguration.objects.count() > 0 else super().has_add_permission(request)
