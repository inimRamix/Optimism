from rest_framework import serializers

from services.models import Subscription, Plan, Service


# class ServiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Service
#         fields = ('__all__')


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('__all__')


class SubscriptionSerializer(serializers.ModelSerializer):
    # service = ServiceSerializer()
    plan = PlanSerializer()

    client_name = serializers.CharField(source='client.company_name')
    email = serializers.CharField(source='client.user.email')
    price = serializers.SerializerMethodField()

    def get_price(self, instance):
        return instance.price

    class Meta:
        model = Subscription
        fields = ('id', 'client_name', 'email', 'service_id', 'plan', 'price')