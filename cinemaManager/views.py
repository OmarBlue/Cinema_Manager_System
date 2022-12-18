import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from cinemaManager.forms import LogMessageForm
from cinemaManager.models import LogMessage
from django.views.generic import ListView

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def addFilm(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            title = form.save(commit=False)
            title.log_date = datetime.now()
            title.save()
            return redirect("home")
    else:
        return render(request, "cinemaManager/addFilm.html", {"form": form})
