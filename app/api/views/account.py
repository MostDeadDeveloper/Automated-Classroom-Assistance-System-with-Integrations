from rest_framework.generics import ListAPIView

from ..serializers.account import AccountSerializer

from account.models import Account


class AccountListAPIView(ListAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()
