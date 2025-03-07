from django.db import models
from django.contrib.auth.models import User,AbstractUser,Group, Permission


# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Storing as hashed later
    terms_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Lead(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'), ('qualified', 'Qualified'), ('quoted', 'Quoted'), ('negotiating', 'Negotiating'),
        ('ordered', 'Ordered'), ('invoiced', 'Invoiced'), ('delivered', 'Delivered'), ('closed', 'Closed'), ('lost', 'Lost')
    ]
    VISIBILITY_CHOICES = [
        ('public', 'Public'), ('private', 'Private'), ('select_people', 'Select People')
    ]
    name = models.CharField(max_length=255)
    lead_type = models.CharField(max_length=50, choices=[('person', 'Person'), ('organization', 'Organization')], default='person')
    company_name = models.CharField(max_length=255, blank=True, null=True)
    company_image = models.ImageField(upload_to='company_images/', blank=True, null=True)
    # company_address = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    currency = models.CharField(max_length=10, choices=[('$', 'USD'), ('€', 'Euro')], default='$')
    phone = models.CharField(max_length=15)
    phone_type = models.CharField(max_length=50, choices=[('work', 'Work'), ('home', 'Home')], default='work')
    email = models.EmailField()
    source = models.CharField(max_length=100, choices=[
        ('phone_calls', 'Phone Calls'), ('social_media', 'Social Media'), ('referral_sites', 'Referral Sites'), 
        ('web_analytics', 'Web Analytics'), ('previous_purchase', 'Previous Purchase')
    ], default='phone_calls')
    industry = models.CharField(max_length=100, choices=[
        ('retail', 'Retail Industry'), ('banking', 'Banking'), ('hotels', 'Hotels'), 
        ('financial_services', 'Financial Services'), ('insurance', 'Insurance')
    ], default='retail')
    owner = models.CharField(max_length=255)
    tags = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # visibility = models.CharField(max_length=50, choices=VISIBILITY_CHOICES, default='public')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name
