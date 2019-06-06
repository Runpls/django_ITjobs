# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse
from markdown import markdown
from datetime import datetime
from django.utils.text import slugify
from django.utils.html import mark_safe


class Job(models.Model):
    sequence = models.AutoField(primary_key=True)
    created_at = models.TextField()
    title = models.TextField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'Job'
        ordering = ('-sequence', )

    def __str__(self):
        return self.title

    def get_description_as_markdown(self):
        return mark_safe(markdown(self.description, safe_mode='escape'))

    def get_time(self):
        return datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%SZ")

    def get_slug(self):
        return slugify(self.title)

    def get_absolute_url(self):
        url = reverse('job_detail',
                      kwargs={'pk': self.pk, 'slug': self.get_slug()})
        return url
