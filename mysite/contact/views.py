from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context_processors import csrf
from forms import ContactForm

def contact(request):
    errors = []
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            fromDict = form.cleaned_data
            # send_mail(request.POST["subject"], request.POST["message"], request.POST["email"], ['siteowner@example.com'])
            return HttpResponseRedirect("/contact/thanks/")
    else:
        form = ContactForm(initial={'subject': 'I love your site!'})

    content = {}
    content.update((csrf(request)))
    content["form"] = form
    return render_to_response("contact_form.html", content)