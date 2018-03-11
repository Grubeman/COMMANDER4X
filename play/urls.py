from django.urls import path
from . import views
from .custom_views import StarSystemViews
from .custom_views import PlanetViews

urlpatterns = [
    path('', views.index, name='index'),
    # ex: /play/starsystem/5/
    path('starsystem/<int:ss_id>', StarSystemViews.overview, name='overview'),
    path('starsystem/<int:ss_id>/overview', StarSystemViews.overview, name='overview'),
    path('planet/<int:p_id>/details', PlanetViews.detail, name='detail'),
]