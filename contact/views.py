from django.shortcuts import render, redirect
from .models import Message
from .forms import ContactForm


def contact(request):
    error = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:main')
        else:
            error = 'Form not correct'


    form = ContactForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request,'contact/contact.html', context)
