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
        'Get All between 2 people': 'all/?p1=n1&p2=n2',
        'Get All since date between 2 people': 'all/?since=datetime&p1=n1&p2=n2',
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
    if request.query_params:
        qpdict = request.query_params.dict()
        if 'since' in qpdict:
            dt = datetime.strptime(qpdict['since'], "%Y-%m-%dT%H:%M:%S.%fZ")
            msgs = Message.objects.filter(datetime__gte=dt, msg_from__in=[qpdict['p1'], qpdict['p2']], msg_to__in=[qpdict['p1'], qpdict['p2']]).order_by('datetime')[1:]
        else:
            msgs = Message.objects.filter(msg_from__in=[qpdict['p1'], qpdict['p2']], msg_to__in=[qpdict['p1'], qpdict['p2']]).order_by('datetime')        
    else:
        msgs = Message.objects.all()

    serializer = MessageSerializer(msgs, many=True)
    return Response(serializer.data)


