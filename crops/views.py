from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import CropBriefSerializer, CropSerializer
from .models import Crop


# Create your views here.
class CropList(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        cropname = request.GET.get("cropname")
        if not cropname:
            qs = Crop.objects.all()
            serializer = CropBriefSerializer(qs, many=True)
            return Response(serializer.data)
        else:
            crop = Crop.objects.get(name=cropname)
            serializer = CropBriefSerializer(crop)
            return Response(serializer.data)


class CropSingle(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        cropname = request.GET.get('cropname')
        print(cropname)
        if cropname:
            crop = Crop.objects.get(name=cropname)
            serializer = CropSerializer(crop)
            return Response(serializer.data)
        else:
            return Response({"what":"what"})