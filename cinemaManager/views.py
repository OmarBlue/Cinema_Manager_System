import re
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from cinemaManager.forms import LogMessageForm
from cinemaManager.models import LogMessage
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import LogMessage
from django.template.loader import get_template 

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

def delete(request,id):
    film = LogMessage.objects.get(id=id) 
    film.delete()
    return HttpResponseRedirect(reverse("home"))

def update(request, id):
    films = LogMessage.objects.get(id=id)
    template = get_template("cinemaManager/updateFilm.html")
    context = {
        "films": films,
    }
    return HttpResponse(template.render(context, request))

def updatefilm(request, id):
  title = request.POST['title']
  age_rating = request.POST['age_rating']
  duration = request.POST['duration']
  description = request.POST['description']
  film = LogMessage.objects.get(id=id)
  film.title = title
  film.age_rating = age_rating
  film.duration = duration
  film.description = description
  film.save()
  return HttpResponseRedirect(reverse('home'))