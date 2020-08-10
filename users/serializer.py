from django.contrib.auth import authenticate

from users.models import User
from  employees.serializer import PositionSerializer
from rest_framework import serializers, exceptions
from rest_framework.serializers import ModelSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'national_id', 'phone_number', 'email', 'status', 'registered_time','date_of_birth',)

    def to_representation(self, instance):
        serialized_data = super(UserSerializer, self).to_representation(instance)
        serialized_data['position'] = PositionSerializer(instance.position).data
        return serialized_data




    #login serializer

class LoginSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField()

        def validate(self, data):
            username = data.get("username", "")
            password = data.get("password", "")
            if username and password:
                user = authenticate(username=username, password=password)
                if user:
                    if user.is_active:
                        data["user"] = user

                    else:
                        msg = "user is deactivated"
                        raise exceptions.ValidationError(msg)

                else:
                    msg = "unable to login with given crediants"
                    raise exceptions.ValidationError(msg)
            else:
                msg = "Must provide username and password both"
                raise exceptions.ValidationError(msg)

            return data
