from django.db import models


class PageContent(models.Model):
    PAGE_CHOICES = (
        ('home', 'Home Page'),
        ('about', 'About Us Page'),
        ('contact', 'Contact Page'),
    )
    page_name = models.CharField(max_length=20, choices=PAGE_CHOICES, unique=True)
    title = models.CharField(max_length=200)
    content = models.TextField(help_text="Main text content for the page.")
    image = models.ImageField(upload_to='pages/', blank=True, null=True, help_text="Optional image for the page.")
    
    def __str__(self):
        return self.get_page_name_display()

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    order = models.IntegerField(default=0, help_text="Order in which service is displayed")
    
    class Meta:
        ordering = ['order', 'title']
        
    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f"Message from {self.name} regarding {self.subject}"
