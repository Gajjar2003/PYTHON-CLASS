from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_api(requset):
    return Response("GET API calling ")

@api_view(['POST'])
def post_api(requset):
    return Response("POST API calling ")

@api_view(['PUT'])
def put_api(requset):
    return Response("PUT API calling ")

@api_view(['DELETE'])
def delete_api(requset):
    return Response("DELETE API calling ")