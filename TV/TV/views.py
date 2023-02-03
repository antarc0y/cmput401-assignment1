# create all end points here
from django.http import JsonResponse
from .models import Show
from .serializers import ShowSerializer, ShowSerializerID
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# a decorator is this
@api_view(['GET','POST'])
def show_list(request, format=None):
    # get all shows
    # serialize them
    # return json
    if request.method == 'GET':
        # gets all shows
        shows = Show.objects.all()
        # get total show count
        total = Show.objects.all().count()
        serializer = ShowSerializer(shows, many=True)
        
        # get average rating by iteration
        avg_rating = 0
        for show in shows:
            avg_rating += show.rating
        if not total == 0:
            avg_rating = avg_rating / total
        
        # create custom response to include all information
        custom_response = ('total: '+str(total),'average rating: '+str(avg_rating), {'shows':serializer.data} )        
        return Response(custom_response)
    if request.method == 'POST':
        serializer = ShowSerializerID(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def show_detail(request, id, format=None):
    # assign id to the pk parameter
    try:
        show = Show.objects.get(pk=id)
    except Show.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ShowSerializerID(show)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ShowSerializerID(show, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        show.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)