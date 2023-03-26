from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json
from .models import movies
from django.views import View
from myapi.serializers import moviesSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

# Create your views here.

# class movies_list():

#       def POST(request):
    
#         if request.method=='POST':
#             name=request.POST.get('name')
#             cast=request.POST.get('cast')
#             review=request.POST.get('review')
#             rating=request.POST.get('rating')
#             image=request.POST.get('image')
#             duration=request.POST.get('duration')
            
#             new_movie=movies(name=name,cast=cast,review=review,rating=rating,image=image,duration=duration)
#             new_movie.save()
            
#             return JsonResponse("movie submitted sucessfully")
#         if request.method=='GET':
#             myapi=movies.objects.all()
#             serializer = moviesSerializer(myapi, many=True)
#         return JsonResponse(serializer.data, safe=False)
        
@csrf_exempt
def movies_list(request):
    
    if request.method == 'GET':
        snippets = movies.objects.all()
        serializer = moviesSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = moviesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)        
            
@csrf_exempt
def movies_details(request,pk):
    try:
        movies=movies.objects.get(pk=pk)
    except movies.doesnotexist:
        return HttpResponse(status=404)
    if request.method=='GET':
        serializer=moviesSerializer(movies)
        return JsonResponse(serializer.data)
    elif request.method=='put':
        data = JSONParser().parse(request)
        serializer = moviesSerializer(movies, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == 'DELETE':
        movies.delete()
        return HttpResponse(status=204)

         
    
    
        
             
            
            
            
            
            
            
        
