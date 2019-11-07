from django.shortcuts import render
from .models import Poll, Choice, Vote
from django.http import JsonResponse

#Serializer
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer

# DRF imports
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics



# Create your views here.




'''
API using APIView
'''
'''
class PollList(APIView):
    def get(self, request):

        polls = Poll.objects.all()
        data = PollSerializer(polls, many =True).data
        return Response(data)

class PollDetail(APIView):
    def get(self, request, pk):

        poll = get_object_or_404(Poll, pk = pk)
        data = PollSerializer(poll).data
        return Response(data)


'''

'''
API using generic views

'''

class PollList(generics.ListCreateAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class PollDetail(generics.RetrieveDestroyAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class CreateVote(generics.CreateAPIView):
    serializer_class = VoteSerializer



        
'''
A glimpse of API views with Pure Django

def polls_list(request):

    MAX_OBJECTS = 20
    polls= Poll.objects.all()[:MAX_OBJECTS]
    data = {'results': list(polls.values('question', 'created_by__username', 'pub_date'))}

    return JsonResponse(data)

def polls_detail(request, pk):
    pass

'''