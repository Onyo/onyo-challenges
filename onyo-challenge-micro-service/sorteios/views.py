from secrets import randbelow
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from sorteios.models import Sorteio, Resultado
from sorteios.serializers import SorteioSerializer, ResultadoSerializer

from datetime import datetime


@api_view(['GET', 'POST'])
def sorteios_list(request, format=None):
    """
    Lista todos os sorteios ou cria um novo
    """
    if request.method == 'GET':
        sorteios = Sorteio.objects.all()
        serializer = SorteioSerializer(sorteios, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SorteioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def sorteios_user_list(request, ownerpk, format=None):
    """
    Lista todos os sorteios ou cria um novo
    """
    if request.method == 'GET':
        sorteios = Sorteio.objects.filter(owner=ownerpk)
        serializer = SorteioSerializer(sorteios, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def sorteio_view(request, ownerpk, pk, format=None):
    """
    Retorna, atualiza ou exclui um sorteio
    """
    try:
        sorteio = Sorteio.objects.get(pk=pk, owner=ownerpk)
    except Sorteio.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SorteioSerializer(sorteio)
        data = serializer.data
        print(data)
        if(data['realizado'] == True):
            resultado = Resultado.objects.get(sorteio=data['id'])
            data['resultado'] = ResultadoSerializer(resultado).data
        return Response(data)

    elif request.method == 'PUT':
        serializer = SorteioSerializer(sorteio, data=request.data)
        if(sorteio.realizado == True):
            return Response({'message': 'Você não pode editar um sorteio já realizado.'}, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if(sorteio.realizado == True):
            resultado = Resultado.objects.get(sorteio=sorteio.id)
            resultado.delete()
        sorteio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def resultado_view(request, pk, format=None):
    """
    Lista todos os sorteios ou cria um novo
    """
    try:
        sorteio = Sorteio.objects.get(pk=pk)
    except Sorteio.DoesNotExist:
        return Response({'message': 'O sorteio indicado não existe.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        try:
            resultado = Resultado.objects.get(sorteio=pk)
        except Resultado.DoesNotExist:
            return Response({'message': 'Este sorteio ainda não foi realizado.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ResultadoSerializer(resultado)
        return Response(serializer.data)

    elif request.method == 'POST':
        return sortear_resultado(sorteio)


def sortear_resultado(sorteio):
    try:
        resultado = Resultado.objects.get(sorteio=sorteio.id)
    except Resultado.DoesNotExist:
        loops = sorteio.quantidadeValores
        valoresSorteados = []
        while loops > 0:
            valorSorteado = randbelow(
                sorteio.maximo - (1 + sorteio.minimo)) + sorteio.minimo
            if valorSorteado not in valoresSorteados:
                valoresSorteados.append(valorSorteado)
                loops = loops - 1

        valoresSorteados = sorted(valoresSorteados)
        stringResultado = '{}'.format(valoresSorteados[0])
        for i in range(1, len(valoresSorteados)):
            stringResultado = stringResultado + \
                ',{}'.format(valoresSorteados[i])

        resultado_serializer = ResultadoSerializer(
            data={'sorteio': sorteio.id, 'resultado': stringResultado})
        if resultado_serializer.is_valid():
            resultado_serializer.save()
            sorteio_serializer = SorteioSerializer(sorteio)
            sorteio_data = sorteio_serializer.data
            sorteio_data['realizado'] = True
            sorteio_data['data_realizado'] = datetime.now()
            serializer = SorteioSerializer(sorteio, sorteio_data)
            if serializer.is_valid():
                serializer.save()
                return Response(resultado_serializer.data, status=status.HTTP_201_CREATED)

    return Response({'message': 'Este sorteio já foi efetuado a já tem um resultado.'}, status=status.HTTP_400_BAD_REQUEST)
