from django.db import models
from garpix_page.models import BasePage


class MainPage(BasePage):
    template = "pages/main.html"

    class Meta:
        verbose_name = "Main"
        verbose_name_plural = "Mains"
        ordering = ("-created_at",)
