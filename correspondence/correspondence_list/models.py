import os
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

class Correspondence(models.Model):
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(max_length=200, editable=False)
    outcoming_mail_number = models.CharField(max_length=100)
    outcoming_mail_receiver = models.CharField(max_length=200, blank=True)
    department = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=200, blank=True)
    header = models.CharField(max_length=400, blank=True)
    date = models.DateField(blank=True, null=True)
    outcoming_file = models.FileField(upload_to="%Y_%m-%d/", null=True, blank=True) 
    incoming_file = models.FileField(upload_to="%Y_%m-%d/", null=True, blank=True)

    class Meta:
        verbose_name = 'Корреспонденция'
        verbose_name_plural = 'Корреспонденция'
    
    
    def __str__(self):
        return f"{self.outcoming_mail_number} {self.date}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.department}_{self.outcoming_mail_number}_{self.date}', allow_unicode=True)
        super(Correspondence, self).save(*args, **kwargs)
    
    @property
    def outcoming_filename(self):
        return os.path.basename(self.outcoming_file.name)
    
    @property
    def incoming_filename(self):
        return os.path.basename(self.incoming_file.name)