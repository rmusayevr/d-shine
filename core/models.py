from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    class Meta:
        verbose_name = 'Contact Us Message'
        verbose_name_plural = 'Contact Us Messages'

    def __str__(self):
        return self.name
    
class Team(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='team/')
    designation = models.CharField(max_length=50)
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    gmail = models.EmailField(null=True, blank=True)

    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'

    def __str__(self):
        return self.name
