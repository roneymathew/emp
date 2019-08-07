from django.contrib.auth.models import User, Group
from rest_framework import serializers, status
from employee.models import emp

from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'is_superuser','first_name','last_name','is_staff','last_login')
        
class EmpSerializer(serializers.ModelSerializer):
	user=UserSerializer(required=True)
	class Meta:
		model = emp
		fields = ('id','housename','city','state','pincode','mobile','empid','user','user_id','boss')
	
	def create(self, validated_data):
		user_data = validated_data.pop('user')
		user = User.objects.create(**user_data)
		emply, created= emp.objects.get_or_create(user=user)
		emply.housename= validated_data.pop('housename')
		emply.city=  validated_data.pop('city')
		emply.state=  validated_data.pop('state')
		emply.pincode= validated_data.pop('pincode')
		emply.mobile= validated_data.pop('mobile')
		emply.empid=validated_data.pop('empid')
		emply.save()
		
	
	def update(self, instance, validated_data,**kwargs):
		print("yes")
		print(instance.id)
		print(instance)
		print(validated_data)
		c=validated_data.pop('user')
		print(c['email'])
		eid = instance.id
		emply, created= emp.objects.get_or_create(id=eid)
		uid = emply.user_id
		user = User.objects.get(id=uid)
		print(user)
		'''user_serializer = UserSerializer(data=user_data)
		if user_serializer.is_valid():
			user_serializer.update(user, user_data)
		instance.save()
		return instance'''
		user.first_name=c['first_name']
		user.last_name=c['last_name']
		user.email=c['email']
		emply, created= emp.objects.get_or_create(user=user)
		emply.housename= validated_data.pop('housename')
		emply.boss= validated_data.pop('boss')
		emply.city=  validated_data.pop('city')
		emply.state=  validated_data.pop('state')
		emply.pincode= validated_data.pop('pincode')
		emply.mobile= validated_data.pop('mobile')
		emply.empid=validated_data.pop('empid')
		emply.save()
		user.save()
		return emply


	def destroy(self,request,pk):
		print("helloooooooo")
		emply=get_object_or_404(emp, pk=pk)
		user=get_object_or_404(User, pk=emply.user_id)
		emply.delete()
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
class TreeSerializer(serializers.ModelSerializer):
	user=UserSerializer(required=True)
	class Meta:
		model = emp
		fields = ('id','housename','city','state','pincode','mobile','empid','user','user_id','boss')

	
	