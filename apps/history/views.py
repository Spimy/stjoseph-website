from django.views.generic import ListView
from .models import History


class HistoryView(ListView):
    template_name = 'history/history.html'
    queryset = History.objects.sort()
