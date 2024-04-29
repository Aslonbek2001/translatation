from django.shortcuts import render
from .logics import translate_text
from django.views import View
from rest_framework import status
from rest_framework.decorators import api_view
from .serializers import TranslateSerializer
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse


class TranslateView(APIView):
    def post(self, request):
        serializer = TranslateSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            target_language = serializer.validated_data['target_language']
            if target_language == 'kk' or target_language == 'ky':
                answer = {
                    'old_text': text,
                    'language': target_language,
                    'translated_text': translate_text(text=text, target_language=target_language)
                }
                return Response(answer, status=status.HTTP_200_OK)
            else:
                message = "Error: 'target_language' is not True"
                return Response(message, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(" Xatolik ", status=status.HTTP_400_BAD_REQUEST)
    

