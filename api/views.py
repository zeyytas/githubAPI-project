
from django.core import serializers
from django.http import HttpResponse
from rest_framework import viewsets
from projectapp.models import Label, Repositories, Language


class APIViewSet(viewsets.ReadOnlyModelViewSet):

    def get_queryset(self):
        return Repositories.objects.all()

    def list(self, request, *args, **kwargs):
        parameter = request.build_absolute_uri().split('/')[-2]
        try:
            if parameter == 'label':
                return HttpResponse(serializers.serialize('json', Label.objects.all()))
            if parameter == 'language':
                return HttpResponse(serializers.serialize('json', Language.objects.all()))
            if parameter == 'repository':
                return HttpResponse(serializers.serialize('json', Repositories.objects.all()))
        except Exception:
            return HttpResponse([])
