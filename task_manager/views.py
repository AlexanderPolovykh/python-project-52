# from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.views.generic import FormView

from .forms import ContactForm, ContactFormSet  # , FilesForm


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # messages.set_level(self.request, messages.WARNING)
        messages.info(self.request, "Hello from Task Manager!")
        return context


class GetParametersMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["layout"] = self.request.GET.get("layout", None)
        context["size"] = self.request.GET.get("size", None)
        return context


class DefaultFormsetView(GetParametersMixin, FormView):
    template_name = "formset.html"
    form_class = ContactFormSet


class DefaultFormView(GetParametersMixin, FormView):
    template_name = "form.html"
    form_class = ContactForm


def index(request):
    return render(
        request,
        "index.html",
        context={
            "name": "Task Manager",
        },
    )


# return HttpResponse("Hello from Task Manager!")
