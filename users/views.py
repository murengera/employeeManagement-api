from django.shortcuts import render
from django.contrib.auth.models import Group
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, mixins, response
from rest_framework.views import APIView

from  users.serializer import *
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.core.mail import EmailMessage
from rest_framework.authtoken.models import Token
from users.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import mixins, generics
from rest_framework.decorators import api_view, permission_classes
from django.core.mail import EmailMessage
from django.conf import settings
from  employees.models import Position
from django.contrib.auth import login as django_login, logout as django_logout




#this function does a registeration of manager and return manager's details.
# the position property should be generated automatically as Manager upon registration.

@api_view(['POST'])
def manager_register(request):
    position = Position.objects.filter(title='Manager').first()
    name = request.data.get('name')
    email = request.data.get('email')
    national_id = request.data.get('national_id')
    phone_number = request.data.get('phone_number')
    date_of_birth = request.data.get('date_of_birth')
    password = request.data.get('password')

    user = User(
        name=name,
        email=email,
        phone_number=phone_number,
        national_id=national_id,
        date_of_birth=date_of_birth,
        position=position,
        status='INACTIVE',
        is_active=False
    )

    user.set_password(password)
    user.save()

    verification_url = "{}/api/activate/{}".format(settings.HOST, user.id)

    if email:
        verify_user = EmailMessage('verify your email ', 'click on this link {} to verify your Account'.format(verification_url), to=[email,])
        verify_user.send()

    return Response(response, status=200)




#this function receive a confirmation with user_id from a user email and activete his/her account
@api_view(['GET', 'POST'])
def email_confirmation(request, user_id):
    user = User.objects.filter(id=user_id).first()
    if user:
        user.status = 'ACTIVE'
        user.is_active = True
        user.save()
    return Response('Account activated successful')


#manager login and receive token using OAUTH2
@api_view(['POST',])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    print('username: ', username)
    print('password: ',password)
    user = authenticate(request=request, username=username, password=password)

    if user:
        if user.status == "ACTIVE":
            token, _ = Token.objects.get_or_create(user=user)
            response = UserSerializer(user).data
            response['token'] = token.key
            return Response(response, status=200)
        else:
            return Response({'detail': "Your account seems to be Inactive..may be you need to verify your email"})
    return Response({"detail": "Invalid credentials"}, status=400)









#this function does a registeration of manager and return manager's details.
# the position property should be generated automatically as Manager upon registration.







#this function does a registeration of manager and return manager's details.
# the position property should be generated automatically as Manager upon registration.
@api_view(['POST'])
def manager_register(request):
    position = Position.objects.filter(title='Manager').first()
    name = request.data.get('name')
    email = request.data.get('email')
    national_id = request.data.get('national_id')
    phone_number = request.data.get('phone_number')
    date_of_birth = request.data.get('date_of_birth')
    password = request.data.get('password')

    user = User(
        name=name,
        email=email,
        phone_number=phone_number,
        national_id=national_id,
        date_of_birth=date_of_birth,
        position=position,
        status='INACTIVE',
        is_active=False
    )

    user.set_password(password)
    user.save()

    message = "Account has been created successfully."
    response = {
        "natianal_id":national_id,
        "phone_number":phone_number,
        "email":email,
        "name":name,
        "position": position.title,
        "status":"INACTIVE",
        "message":message
    }

    verification_url = "{}/api/activate/{}".format(settings.HOST, user.id)

    if email:
        verify_user = EmailMessage('verify your email ', 'click on this link {} to verify your Account'.format(verification_url), to=[email,])
        verify_user.send()

    return Response(response, status=200)


#login
#manager login and receive token using OAUTH2
class Loginview(APIView):

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data("user")
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)





class UserList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get(self,request,*args, **kwargs):
        return self.list(request,*args, **kwargs)

    def post(self,request,*args, **kwargs):
        return self.create(request, *args, **kwargs)

# get,update and delete user/manager's detail
class UserDetail(mixins.
                    RetrieveModelMixin,mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin, generics.GenericAPIView):

    queryset = User.objects.none()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)


    def get(self,request,*args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@api_view(['POST', 'PATCH'])
@permission_classes([IsAuthenticated])
def update_groups(request):
    user = request.user
    if user.is_superuser or user.is_staff:
        user = User.objects.filter(id=request.data.get('id')).last()
        if user:
            user.groups.clear()
            group = Group.objects.filter(name=request.data.get('groups')).last()
            user.groups.add(group)
            return Response({"detail": "Groups updated successfully"}, status=200)
        return Response({"detail": "Something went wrong"}, status=400)
    return Response({"detail": "You are not allowed to update user group "}, status=403)
