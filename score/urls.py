from django.urls import path

from .views import ScoreCreateAPI,ScoreListAPI,DeleteScoreAPI,UpdateScoreAPI,ScoreDetailsAPI

urlpatterns = [
    path('', ScoreListAPI.as_view(), name='Score List'),
    path('create',ScoreCreateAPI.as_view(), name='Create Score API'),
    path('details', ScoreDetailsAPI.as_view(), name='details List'),
    path('delete',DeleteScoreAPI.as_view(), name='Delete Score API'),
    path('update', UpdateScoreAPI.as_view(), name='Update Score API'),
]
