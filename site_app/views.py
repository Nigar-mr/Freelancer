from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from site_app.models import *
from .forms import ContactForm
from django.contrib import messages
# Create your views here.


def home_page(request):
    context = {}
    context["form"] = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Sizinle elaqe saxlanilacaq"
            )
            return redirect("/#contact")
        else:
            messages.error(
                request,
                "Form yanlishdir"
            )
            context["form"] = form

    context["menu_list"] = MenuModel.objects.filter().order_by('-num')
    context["portfolio_list"] = PortfolioModel.objects.all()
    context["about_list"] = AboutModel.objects.all()
    context["contact_list"] = ContactFormModel.objects.all()
    context["info_list"] = InfoModel.objects.all()
    context["icon_list"] = IconModel.objects.all()
    context["unique_list"] = UniqeModel.objects.first()

    return render(request, "index.html", context)