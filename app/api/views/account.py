from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

from ..serializers.account import AccountSerializer

from account.models import Account


class AccountListAPIView(ListAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()

class ConvertDiscordIdToCredentialsAPIView(APIView):

    def post(self, request):
        discord_id = self.request.data.get('discord_id')
        data = {}
        data['discord_id'] = discord_id

        existing_record = Account.objects.filter(discord_id=discord_id)

        if existing_record:
            account = existing_record.first()

            existing_token = Token.objects.filter(user=account)

            if existing_token:
                data['token'] = existing_token.first().key


            data['account_id'] = account.id
            data['status'] = 'Success!'

            return Response(
                data=data,
                status=status.HTTP_200_OK,
            )
        else:
            data['status'] = 'Failed!'

        return Response(
            data=data,
            status=status.HTTP_200_OK,
        )



