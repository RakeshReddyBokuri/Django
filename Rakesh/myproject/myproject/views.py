from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Send the email
        send_mail(
            subject=f"Message from {name}",
            message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
            from_email=email,
            recipient_list=[settings.EMAIL_HOST_USER],  # Your email address
        )
        
        # After sending the email, redirect to a thank you page (or reload the same page)
        return render(request, 'home.html', {'success': True})

    return render(request, 'home.html')
