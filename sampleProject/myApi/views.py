from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.models import Item
from .serializers import ItemSerializer
from django.shortcuts import redirect

@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('plate taken')
    return Response(serializer.data)

@api_view(['DELETE'])
def delete(request, name_id):
    namedel = Item.objects.get(pk=name_id)
    namedel.delete()

    return redirect('/sample')
