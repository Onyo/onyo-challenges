from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.cache import cache_page
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import requests
import json

from django.core.cache import caches
cache = caches['default']

API_URL = 'http://68.183.172.30:7000/api/v1'
# Create your views here.


@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated, ))
def list_sorteios(request):
    """
    Lista todos os sorteios ou cria um novo
    """
    if request.method == 'GET':
        cached = cache.get('user_{}_sorteios'.format(
            request.user.id), 'expired')
        if cached != 'expired':
            return Response(json.loads(cached))

        response = requests.get(
            '{}/user/{}/sorteios/'.format(API_URL, request.user.id))
        if response.status_code == 200:
            response = response.json()
            cache.set('user_{}_sorteios'.format(
                request.user.id), json.dumps(response), 24 * 60 * 60)
            return Response(response)
        return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        data = request.data
        data['owner'] = request.user.id
        response = requests.post(
            '{}/sorteios/'.format(API_URL), data=data)
        if response.status_code == 201:
            cache.delete('user_{}_sorteios'.format(
                request.user.id))
            return Response(response.json(), status=status.HTTP_201_CREATED)
        elif response.status_code == 404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        elif response.status_code == 400:
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class CachedResponse(object):
    def __init__(self, status_code, cached):
        self.status_code = status_code
        self.cached = cached

    def json(self):
        return json.loads(self.cached)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((IsAuthenticated, ))
def sorteio(request, pk):
    cached = cache.get('user_{}_sorteio_{}'.format(
        request.user.id, pk), 'expired')
    if cached != 'expired':
        response = CachedResponse(200, cached)
    else:
        response = requests.get(
            '{}/user/{}/sorteios/{}/'.format(API_URL, request.user.id, pk))
        if response.status_code == 200:
            cache.set('user_{}_sorteio_{}'.format(
                request.user.id, pk), json.dumps(response.json()), 24*60*60)
        if response.status_code == 404:
            return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if response.status_code == 200:
            return Response(response.json())
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        data = request.data
        data['owner'] = request.user.id
        response = requests.put(
            '{}/user/{}/sorteios/{}/'.format(API_URL, request.user.id, pk), data=data)
        if response.status_code == 200:
            cache.delete('user_{}_sorteio_{}'.format(
                request.user.id, pk))
            cache.delete('user_{}_sorteios'.format(
                request.user.id))
            return Response(response.json())
        elif response.status_code == 400:
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        response = requests.delete(
            '{}/user/{}/sorteios/{}/'.format(API_URL, request.user.id, pk))
        if response.status_code == 204:
            cache.delete('user_{}_sorteio_{}'.format(
                request.user.id, pk))
            cache.delete('user_{}_sorteios'.format(
                request.user.id))
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif response.status_code == 400:
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
# Cacheando o resultado por uma hora, já que ele nunca se alterará
@cache_page(60 * 60)
def resultado(request, pk):
    response = requests.get(
        '{}/sorteios/{}/resultado/'.format(API_URL, pk))
    if response.status_code == 404:
        response = requests.post(
            '{}/sorteios/{}/resultado/'.format(API_URL, pk), data={})
        if response.status_code == 201:
            cache.delete('user_{}_sorteio_{}'.format(
                request.user.id, pk))
            cache.delete('user_{}_sorteios'.format(
                request.user.id))
            return Response(response.json())
        elif response.status_code == 404:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif response.status_code == 200:
        return Response(response.json())
    return Response(status=status.HTTP_400_BAD_REQUEST)
