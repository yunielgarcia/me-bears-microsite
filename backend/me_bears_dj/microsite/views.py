from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse

from microsite.models import Content
from microsite.serializers import ContentModelSerializer


def get_data(request):
    data = Content.objects.all()
    if request.method == 'GET':
        serializer = ContentModelSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
