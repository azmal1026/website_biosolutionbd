from django.shortcuts import render, redirect
from django.contrib import messages
from .models import PageContent, Service
from .forms import ContactForm

def home(request):
    content = PageContent.objects.filter(page_name='home').first()
    services = Service.objects.all()[:3] # Show top 3 services on home page
    return render(request, 'home.html', {'content': content, 'services': services})

def about(request):
    content = PageContent.objects.filter(page_name='about').first()
    return render(request, 'about.html', {'content': content})

def services(request):
    services_list = Service.objects.all()
    return render(request, 'services.html', {'services': services_list})

def contact(request):
    content = PageContent.objects.filter(page_name='contact').first()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
        
    return render(request, 'contact.html', {'content': content, 'form': form})
