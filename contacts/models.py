from __future__ import unicode_literals
from django.utils.translation import ugettext as _
from django.db import models
from datetime import datetime

class Group(models.Model):
    group_name = models.CharField(max_length=16, blank=False, null=False)
    slug = models.SlugField(_('slug'), max_length=50)
    about = models.TextField(_('about'), blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'contacts_groups'
        ordering = ('group_name',)
        verbose_name = _('group')
        verbose_name_plural = _('groups')

class Address(models.Model):

    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=150, blank=True)
    state = models.CharField(max_length=2, blank=True)
    zip = models.CharField(max_length=15, blank=True)

class Contact(models.Model):

    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    birthdate = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=25, blank=True)
    email = models.EmailField(blank=True)
    address = models.ForeignKey(Address, null=True)
    group = models.ManyToManyField(Group, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'contacts_contact'
        ordering = ('last_name', 'first_name')
        verbose_name = _('contact')
        verbose_name_plural = _('contacts')
