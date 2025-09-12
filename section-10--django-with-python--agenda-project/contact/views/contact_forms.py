from typing import Any

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from contact.forms import ContactForm
from contact.models import Contact


@login_required(login_url="contact:login")
def create(request):
    form_action = reverse("contact:create")

    context: dict[str, Any] = {
        "form_action": form_action,
    }

    if request.method == "POST":
        contact_form = ContactForm(request.POST, request.FILES)

        if contact_form.is_valid():
            contact = contact_form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect("contact:update", contact_id=contact.id)

        context.update({"form": contact_form})
    else:
        context.update({"form": ContactForm()})

    return render(request, "contact/create.html", context)


@login_required(login_url="contact:login")
def update(request, contact_id):
    contact = get_object_or_404(
        Contact, id=contact_id, show=True, owner=request.user
    )
    form_action = reverse("contact:update", args=(contact_id,))

    context: dict[str, Any] = {
        "form_action": form_action,
    }

    if request.method == "POST":
        contact_form = ContactForm(
            request.POST, request.FILES, instance=contact
        )

        if contact_form.is_valid():
            contact = contact_form.save()
            return redirect("contact:update", contact_id=contact.id)

        context.update({"form": contact_form})
    else:
        context.update({"form": ContactForm(instance=contact)})

    return render(request, "contact/create.html", context)


@login_required(login_url="contact:login")
def delete(request, contact_id):
    contact = get_object_or_404(
        Contact, id=contact_id, show=True, owner=request.user
    )
    confirmation = request.POST.get("confirmation", "no")

    if confirmation == "yes":
        contact.delete()
        return redirect("contact:index")

    context = {
        "contact": contact,
        "confirmation": confirmation,
    }

    return render(request, "contact/contact.html", context)
