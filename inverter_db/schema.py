import graphene
from graphene_django import DjangoObjectType
from .models import InverterData

class InverterDataType(DjangoObjectType):
    class Meta:
        model = InverterData
        fields = '__all__'

class Query(graphene.ObjectType):
    all_inverter_data = graphene.List(
        InverterDataType,
        order_by=graphene.String()
    )

    def resolve_all_inverter_data(self, info, order_by=None):
        queryset = InverterData.objects.all()
        if order_by:
            queryset = queryset.order_by(order_by)
        return queryset

schema = graphene.Schema(query=Query)