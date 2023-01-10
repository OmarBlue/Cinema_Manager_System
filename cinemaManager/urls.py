from django.urls import path
from cinemaManager import views
from cinemaManager.models import LogMessage
from . import views

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :10 limits the results to the five most recent
    context_object_name="film_list",
    template_name="cinemaManager/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("addFilm/", views.addFilm, name="addFilm"),
    path("delete/<int:id>", views.delete, name="delete"),
    path('update/<int:id>', views.update, name='update'),
    path('update/updatefilm/<int:id>', views.updatefilm, name='updatefilm'),
]

