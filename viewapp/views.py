from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from viewapp.models import Employee
from viewapp.serializers import EmployeeSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly

from viewapp.permission import IsReadOnly,IsGetOrPatch,PrasanPermission
# Create your views here.
class EmployeeCURDCVB(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class=EmployeeSerializer
    authentication_classes=[TokenAuthentication]
    # permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes=[IsReadOnly]
    # permission_classes=[IsGetOrPatch]
    permission_classes=[PrasanPermission]

