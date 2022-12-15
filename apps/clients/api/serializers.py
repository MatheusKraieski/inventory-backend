from rest_framework import serializers
from apps.clients.models import Client

class ClientSerializer(serializers.ModelSerializer):
    def add_client(self, request):
        try:
            Client.objects.create(
                name=request.data.get('name'),
                email=request.data.get('email'),
                cpf=request.data.get("cpf"),
                cnpj=request.data.get('cnpj'),
                first_phone=request.data.get('first_phone'),
                second_phone=request.data.get('second_phone'),
            )
            return {'detail': 'Cliente adicionado com sucesso.'}, 201
        except Exception as e:
            print(e)
            return {'detail': 'Cliente não pode ser criado.'}, 400    