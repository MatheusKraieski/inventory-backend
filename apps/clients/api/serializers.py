from rest_framework import serializers
from apps.clients.models import Client
from django.db import transaction

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

    def update_client(self, client, request):
        try:
            with transaction.atomic():
                client.name = request.data.get("name", client.name)
                client.email = str(request.data.get("email", client.email))
                client.cpf = str(request.data.get("cpf", client.cpf))
                client.cnpj = str(request.data.get("cnpj", client.cnpj))
                client.first_phone = str(request.data.get("first_phone", client.first_phone))
                client.second_phone = str(request.data.get("second_phone", client.first_phone))
                
                client.save()

                return {"detail": "client was updated successfully."}, 201
        except Exception as e:
            print(e)
            return {"error": "Client could not be changed."}, 400        

    def get_client(self, client):
        client_dict = self.build_client_dict(client)
        return client_dict, 200


    def build_client_dict(self, client):
        product_dict = {
            "id": client.pk,
            "name": client.name,
            "email": client.email,
            "cpf": client.cpf,
            "cnpj": client.cnpj,
            "first_phone": client.first_phone,
            "second_phone": client.second_phone,
        }
        return product_dict

    def delete_client(self, client):
        try:
            if transaction.atomic():
                client.delete()
            return {"detail": "Product was deleted successfully"}, 201
        except Exception as err:
            print(err)
            return {"error": "Product could not be deleted"}, 400    