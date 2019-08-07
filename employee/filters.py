import django_filters
from .models import emp
from django.contrib.auth.models import User

class EmpFilter(django_filters.FilterSet):
	class Meta:
		model=emp
		fields=['empid']