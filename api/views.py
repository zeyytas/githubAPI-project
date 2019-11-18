
from django.core import serializers
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route

from projectapp.models import Label, Repositories, Language


class APIViewSet(viewsets.ReadOnlyModelViewSet):

    @staticmethod
    def model_label():
        data = serializers.serialize('json', Label.objects.all())
        return HttpResponse(data)

    @staticmethod
    def model_repositories():
        data = serializers.serialize('json', Repositories.objects.all())
        return HttpResponse(data)

    @staticmethod
    def model_language():
        data = serializers.serialize('json', Language.objects.all())
        return HttpResponse(data)

    @staticmethod
    def model_language2(lang):
        data = serializers.serialize('json', Repositories.objects.filter(repository_language__repo_language=lang))
        return HttpResponse(data)
