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
from django.db.models import Q

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

@api_view(['GET'])
def getDavaById(request, id):

    #dava = Dava.objects.filter(Q(dava=id) | Q(dava=id))
    davaci_user = User.objects.raw("select api_user.id,api_user.name,api_user.tc,api_user.email,api_user.birth_date,api_user.phone,api_user.password  from api_dava join api_davaci on api_dava.id=api_davaci.dava_id join api_user on api_user.id=api_davaci.user_id;")
    dava = Dava.objects.filter(id=id)
    davali_user = User.objects.raw("select api_user.id,api_user.name,api_user.tc,api_user.email,api_user.birth_date,api_user.phone,api_user.password  from api_dava join api_davali on api_dava.id=api_davali.dava_id join api_user on api_user.id=api_davali.user_id;")

    serializer = UserSerializer(davaci_user, many=True)
    serializer2 = DavaSerializer(dava, many=True)
    serializer3 = UserSerializer(davali_user, many=True)

    return Response(serializer.data + serializer2.data + serializer3.data,)

