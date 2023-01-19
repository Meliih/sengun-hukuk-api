from datetime import timedelta
import datetime
from http.client import HTTPResponse
import json
import os

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from .serializers import *
from .models import *

import random
import string


@api_view(['GET'])
def getIcras(request):
    # order by descending 
    icra = Icra.objects.all()
    #order_by('-id')[:50:-1]
    serializer = IcraSerializer(icra, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getDavas(request):
    # order by descending 
    dava = Dava.objects.all()
    serializer = DavaSerializer(dava, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getNotes(request):
    # order by descending 
    note = Note.objects.all()
    serializer = NoteSerializer(note, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getAppointments(request):
    # order by descending 
    appointment = Appointment.objects.all()
    serializer = AppointmentSerializer(appointment, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getOurServices(request):
    # order by descending 
    ourServices = OurService.objects.all()
    serializer = OurServiceSerializer(ourServices, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getArticleAndNews(request):
    # order by descending 
    articleAndNew = ArticleAndNew.objects.all()
    serializer = ArticleAndNewSerializer(articleAndNew, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getLawyers(request):
    # order by descending 
    lawyers = Lawyer.objects.all()
    serializer = LawyerSerializer(lawyers, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getReferences(request):
    # order by descending 
    references = Reference.objects.all()
    serializer = ReferenceSerializer(references, many=True)

    return Response(serializer.data)