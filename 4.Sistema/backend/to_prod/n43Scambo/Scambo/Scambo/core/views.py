from django.views.generic.base import TemplateView
from django.apps.config import AppConfig
from django.conf import settings
from .models import HomePage

class HomePageView(TemplateView):
    
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_ar'] = HomePage.objects.all()[:5]
        return context
