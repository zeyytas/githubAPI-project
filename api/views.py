
from django.core import serializers
from django.http import HttpResponse
from rest_framework import viewsets
from projectapp.models import Label, Repositories, Language


class LabelViewSet(viewsets.ReadOnlyModelViewSet):

    def get_queryset(self):
        return Label.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            return HttpResponse(serializers.serialize('json', Label.objects.all()))
        except Exception:
            return HttpResponse([])


class LanguageViewSet(viewsets.ReadOnlyModelViewSet):

    def get_queryset(self):
        return Language.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            return HttpResponse(serializers.serialize('json', Language.objects.all()))
        except Exception:
            return HttpResponse([])


class RepositoryViewSet(viewsets.ReadOnlyModelViewSet):

    def get_queryset(self):
        return Repositories.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            language = request.GET.get('l')
            if not language:
                return HttpResponse(serializers.serialize('json', Repositories.objects.all()))
            return HttpResponse(serializers.serialize(
                'json', Repositories.objects.filter(repository_language__repo_language=language)))
        except Exception:
            return HttpResponse([])