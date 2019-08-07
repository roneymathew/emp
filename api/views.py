from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status,filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, EmpSerializer,TreeSerializer
from employee.models import emp
from django_filters.rest_framework import DjangoFilterBackend
import django_filters.rest_framework
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize
class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, YourCustomType):
            return str(obj)
        return super().default(obj)


class AuthentView(APIView):
    authentication_classes = (SessionAuthentication,BasicAuthentication )
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'user': unicode(request.user),  # `django.contrib.auth.User` instance.
            'auth': unicode(request.auth),  # None
        }
        return Response(content)
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)

    
class EmpViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    #authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = IsAuthenticated,
    queryset = emp.objects.all().order_by('user')
    serializer_class = EmpSerializer
    filter_backends=(filters.SearchFilter,)
    search_fields=['user__first_name','user__last_name','user__email','housename','city']
    '''def update(self, request, *args, **kwargs):
        p, created = emp.objects.get_or_create(id=kwargs['pk'])
        q = User.objects.get(username=p.user)
        if not created:
            p.empid=request.POST['empid']
            q.first_name=request.POST['first_name']
            q.last_name=request.POST['last_name']
            p.housename=request.POST['housename']
            p.city=request.POST['city']
            p.state=request.POST['state']
            p.pincode=request.POST['pincode']
            p.mobile=request.POST['mobile']
            p.save()
            q.save()
        return p'''

    def destroy(self,request,pk):
        print("helloooooooo")
        emply=get_object_or_404(emp, pk=pk)
        user=get_object_or_404(User, id=emply.user_id)
        emply.delete()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''class EmpDetailView(APIView):
    def get(self,request,pk):
        queryset=get_object_or_404(emp, pk=pk)
        serializer_class=EmpSerializer
        return Response(serializers.data)

    def delete(self,request,pk):
        emply=get_object_or_404(emp, pk=pk)
        emply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''

class TreeViewSet(viewsets.ModelViewSet):
    serializer_class = TreeSerializer
    queryset = emp.objects.all().order_by('user')
    
    #def retrieve(self, request, *args, **kwargs):
     #   return Response({'something': 'my custom JSON'})

    def list(self, request, *args, **kwargs):
        dat=request.GET['boss']
        print(dat)
        user = get_object_or_404(emp,id=dat)
        rep = emp.objects.filter(boss=user.id)
        reporters = EmpSerializer(rep, many=True)
        if user.boss:
            query = get_object_or_404(emp,id=user.boss)
            print(query)
            boss = EmpSerializer(query)
            queryse = emp.objects.filter(boss=query.id)
            sameboss = EmpSerializer(queryse, many=True)
            dataa={'boss':boss.data,'sameBoss':sameboss.data,'reporters':reporters.data}
        else:
            user1 = emp.objects.filter(id=dat)
            sameboss = EmpSerializer(user1,many=True)
            dataa={'boss':None,'sameBoss':sameboss.data,'reporters':reporters.data}

        
        return Response(dataa)
