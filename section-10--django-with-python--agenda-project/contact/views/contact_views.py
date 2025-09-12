from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator

from contact.models import Contact


def index(request):
    contacts = Contact.objects.filter(show=True).order_by("-id")
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "head_title": "Contatos - ",
    }
    return render(request, "contact/index.html", context)


def contact(request, contact_id):
    _contact = get_object_or_404(Contact, id=contact_id, show=True)

    context = {
        "contact": _contact,
        "head_title": f"{_contact.first_name} {_contact.last_name} - ",
    }
    return render(request, "contact/contact.html", context)


def search(request):
    search_value = request.GET.get("q", "").strip()

    if not search_value:
        return redirect("contact:index")

    contacts = (
        Contact.objects.filter(show=True)
        .filter(
            Q(first_name__icontains=search_value)
            | Q(last_name__icontains=search_value)
            | Q(email__icontains=search_value)
            | Q(phone__icontains=search_value)
        )
        .order_by("-id")
    )
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "head_title": "Search - ",
        "search_value": search_value,
    }
    return render(request, "contact/index.html", context)
