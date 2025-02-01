from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Message
from .serializers import MessageSerializer

from rest_framework import serializers
from rest_framework import status
from datetime import datetime
 
@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_msg': '/',
        'Get All': 'all/',
        'Get All since date': 'all/?since=datetime',
        'Add': '/create',
    }
 
    return Response(api_urls)


@api_view(['POST'])
def add_msg(request):
    msg = MessageSerializer(data=request.data)
 
    if msg.is_valid():
        msg.save()
        return Response(msg.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['GET'])
def view_msgs(request):
    # checking for the parameters from the URL

    if request.query_params:
        msgs = Message.objects.filter(datetime__gte=datetime.strptime(request.query_params.dict()['since'], "%Y-%m-%dT%H:%M:%S.%fZ"))
    else:
        msgs = Message.objects.all()
 
    # if there is something in items else raise error
    if msgs:
        serializer = MessageSerializer(msgs, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

