from employees.models import  Position,Employee
from rest_framework import serializers



class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ('__all__')
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model =Employee
        fields = ['name',]

    def to_representation(self, instance):
        serialized_data = super(EmployeeSerializer, self).to_representation(instance)
        serialized_data['position'] = PositionSerializer(instance.position).data
        return serialized_data