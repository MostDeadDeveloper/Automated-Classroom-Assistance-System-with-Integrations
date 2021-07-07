from rest_framework.generics import ListAPIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from ..serializers.account import AccountSerializer

from account.models import Account


class AccountListAPIView(ListAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()


class DiscordAccountAuthenticationAPIView(APIView):

    def post(self, request):
        discord_id = self.request.data.get('discord_id')
        data = {}

        existing_account = Account.objects.filter(discord_id=discord_id)

        if existing_account:
            account = existing_account.first()
            data['account_id'] = account.id

            existing_token = Token.objects.filter(user=account)

            if existing_token:
                data['token'] = existing_token.first().key
            else:
                new_token = Token.objects.create(user=account)
                data['token'] = new_token.key

            data['status'] = 'Success!'

            return Response(
                data=data,
                status=status.HTTP_200_OK,
            )
        else:
            data['status'] = 'Failed. Error Encountered'

        return Response(
            data=data,
            status=status.HTTP_400_BAD_REQUEST,
        )


