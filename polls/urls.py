
'''
=== app level urls.py ===
'''

from django.urls import path
from . import views

'''
urlpatterns = [
    path('polls/', views.PollList.as_view(), name = 'polls'),
    path('polls/<int:pk>/', views.PollDetail.as_view(), name = 'poll_detail'),
    path('choices/', views.ChoiceList.as_view(), name = 'choice_list'),
    path('vote/', views.CreateVote.as_view(), name = 'create_vote'),
]

'''

urlpatterns = [
    path('polls/', views.PollList.as_view(), name = 'polls'),
    path('polls/<int:pk>', views.PollDetail.as_view(), name = 'poll_detail'),
    path('polls/<int:pk>/choices/', views.ChoiceList.as_view(), name = 'choice_list'),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', views.CreateVote.as_view(), name = 'create_vote'),
]