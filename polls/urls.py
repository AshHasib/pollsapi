
'''
=== app level urls.py ===
'''


from django.urls import path
from . import views
urlpatterns = [
    path('polls/', views.PollList.as_view(), name = 'polls'),
    path('polls/<int:pk>', views.PollDetail.as_view(), name = 'poll_detail'),
]