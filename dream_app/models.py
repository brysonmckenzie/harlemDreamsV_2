from __future__ import unicode_literals
from django.db import models


class Event(models.Model):
    opponent = models.CharField(max_length=30)
    date = models.DateField(auto_now=False, auto_now_add=False)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    description = models.TextField(max_length=200)
    location = models.CharField(max_length=50)
    image = models.ImageField(upload_to='events', blank=True)
    hd_event_logo = models.ImageField(
        upload_to='events/hd_logo_main', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return(self.opponent + " vs The Harlem Dreams")



class Photo(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='carousel')
    description = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    photo_order = models.PositiveIntegerField(
        default=0, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        ordering = ['photo_order']

    def __str__(self):
        return(self.name + " - " + self.description)
 
class mediaPhoto(models.Model):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='media-carousel')
    description = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    photo_order = models.PositiveIntegerField(
        default=0, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        ordering = ['photo_order']

    def __str__(self):
        return(self.name + " - " + self.description)


class Notice(models.Model):
    name = models.CharField(primary_key=True, max_length=50, blank=True)
    message = models.TextField(max_length=600, blank=True, null=False)
    active = models.BooleanField(default=True)
    color = models.CharField(max_length=256, choices=[(
        'green', 'green'), ('red', 'red'), ('blue', 'blue')], null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.active:
            return(self.name + "(active)")
        else:
            return(self.name + "(inactive)")


class Player(models.Model):
    image = models.ImageField(upload_to='team')
    number = models.CharField(max_length=3, blank=True, null=True)
    show_number = models.BooleanField(default=True)
    number_sign = models.BooleanField(default=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(max_length=1000, blank=True, null=True)
    position = models.CharField(max_length=20, blank=True, null=True)
    quote = models.TextField(max_length=1000, blank=True, null=True)
    active = models.BooleanField(default=True)
    player_order = models.PositiveIntegerField(
        default=0, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        ordering = ['player_order']

    def __str__(self):
        if self.active:
            return(self.name + "(active)")
        else:
            return(self.name + "(inactive)")


class Video(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(max_length=200)
    link = models.TextField(max_length=1000)
    active = models.BooleanField(default=True)
    video_order = models.PositiveIntegerField(
        default=0, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        ordering = ['video_order']

    def __str__(self):
        return(self.title)


class Camp(models.Model):
    camp_title = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    info = models.TextField(max_length=600, blank=True, null=False)
    info_2 = models.TextField(max_length=600, blank=True, null=False)
    event_info = models.TextField(max_length=600, blank=True, null=False)
    event_image = models.ImageField(upload_to='camps')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class SiteConfiguration(models.Model):
    facebook = models.CharField(max_length=150, blank=True, null=True)
    instagram = models.CharField(max_length=150, blank=True, null=True)
    twitter = models.CharField(max_length=150, blank=True, null=True)
    homepage_phone = models.CharField(max_length=15, blank=True, null=True)
    contact_page_phone = models.CharField(max_length=15, blank=True, null=True)
    contact_email = models.CharField(max_length=40, blank=True, null=True)
    carousel_off = models.BooleanField(default=True)

    def __str__(self):
        return("links configurations (limit to one record)")
