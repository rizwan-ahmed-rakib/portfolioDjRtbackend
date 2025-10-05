from django.db import models
from django.core.validators import MaxValueValidator,FileExtensionValidator

# Create your models here.
class AboutMe(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    designation = models.CharField(max_length=300)
    resume = models.FileField(
    upload_to="aboutMe/resume",null=True,
    validators=[FileExtensionValidator(allowed_extensions=['pdf', 'doc', 'docx'])],
    help_text="শুধুমাত্র PDF, DOC বা DOCX ফাইল আপলোড করুন"
        )
    hero_image = models.ImageField(upload_to="aboutMe/hero_image", null=True, blank=True)
    about_me = models.TextField()
    experience = models.TextField(null=True, blank=True)
    hilight_in_experience = models.TextField(null=True, blank=True)
    education_title = models.TextField(null=True, blank=True)
    education_institute = models.TextField(null=True, blank=True)
    short_educational_description = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.first_name + " " + self.last_name


class Skill(models.Model):
    name = models.CharField(max_length=100)
    percentage = models.IntegerField()
    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=300)
    def __str__(self):
        return self.name + " " + self.short_description

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Portfolio(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='portfolio_images/')
    live_url = models.URLField()
    github_url = models.URLField()
    tags = models.ManyToManyField(Tag, related_name='projects')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name + " "

class Message(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.CharField(max_length=100)
    message = models.TextField()
