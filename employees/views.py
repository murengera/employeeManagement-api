from django.core.mail import EmailMessage
from django.shortcuts import render
from rest_framework import mixins, generics
from rest_framework.permissions import IsAuthenticated

from  employees.models import  Position,Employee
from employees.serializer import PositionSerializer,EmployeeSerializer


# view employee_list allows us to get and create employee
class EmployeeList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    #permission_classes = (IsAuthenticated,)
    search_fields = ['position', 'name', 'email', 'phone_number']
    filter_fields = ['position', 'name', 'email', 'phone_number']

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = request.data
        if user.get('email'):
            print('employee email',user.get('email'))
            response = self.create(request, *args, **kwargs)
            send_message = EmailMessage("Account created successful:","You joined the Company with Comany_name", to=[user.get('email'),])
            send_message.send()

            return response


# view employee_details allows us to get,update and delete Employee detail
class EmployeeDetail(mixins.
                     RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, *kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class PositionList(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    #permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PositionDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)