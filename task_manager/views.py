# from django.http import HttpResponse
# from django.shortcuts import render

# from django.contrib import messages

# from django.views.generic import FormView
# from .forms import ContactForm, ContactFormSet  # , FilesForm

from django.utils.translation import gettext as _
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from task_manager.models import User


class MainPageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context |= {
            "brand": _("Task Manager"),
            "users": _("Users"),
            "input": _("Sign In"),
            "reg": _("Log In"),
            "hello": _("Hello from Hexlet!"),
            "about": _("Practical programming courses"),
            "info": _("To learn more"),
        }
        # messages.set_level(self.request, messages.WARNING)
        # messages.info(self.request, "Hello from Task Manager!")
        return context


class UsersListPageView(ListView):
    # model = User
    queryset = User.objects.order_by('-created_at')
    template_name = "users.html"
    context_object_name = "user_list"


# class GetParametersMixin:
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["layout"] = self.request.GET.get("layout", None)
#         context["size"] = self.request.GET.get("size", None)
#         return context


# class DefaultFormsetView(GetParametersMixin, FormView):
#     template_name = "formset.html"
#     form_class = ContactFormSet


# class DefaultFormView(GetParametersMixin, FormView):
#     template_name = "form.html"
#     form_class = ContactForm
