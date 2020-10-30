from django.urls import path
from ringer.views import RingerLoginView, RingerProfileView
urlpatterns = [
    path('login/', RingerLoginView.as_view(), name="ringer_login"),
    path('profile/', RingerProfileView.as_view(), name="ringer_profile"),
]
