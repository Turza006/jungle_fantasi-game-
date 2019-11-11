from django.urls import path

from .views import PlayersCreateAPI,PlayersListAPI,DeletePlayersAPI,UpdatePlayersAPI,PlayersDetailsAPI

urlpatterns = [
    path('', PlayersListAPI.as_view(), name='Players List'),
    path('create', PlayersCreateAPI.as_view(), name='Create Players API'),
    path('details', PlayersDetailsAPI.as_view(), name='details List'),
    path('delete', DeletePlayersAPI.as_view(), name='Delete Players API'),
    path('update', UpdatePlayersAPI.as_view(), name='Update Players API'),

]
