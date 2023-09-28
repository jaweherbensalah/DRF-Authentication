
from django.urls import path
from .views import PersonList, set_language


urlpatterns = [
    path("persons/", PersonList.as_view(), name="persons"),

   # YENİ
    path("set_language/<str:language>", set_language, name="set-language"),

]