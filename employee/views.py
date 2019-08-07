from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import View ,UpdateView,CreateView
from .models import emp
from .forms import empForm,UserForm
from .filters import EmpFilter
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#f0r api





# default django






class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
class IndexPage(View):
	template_name='employee/index.html'
	def get(self,request, *args, **kwargs):
		return render(request,self.template_name,{})
	def post(self, request, *args, **kwargs):
		return render(request,self.template_name,{})


class CreatePage(LoginRequiredMixin,View):
	template_name='employee/create.html'
	form=empForm()
	form1=UserForm()
	def get(self, request, *args, **kwargs):
		form=empForm(request.POST, instance=request.user)
		form1=UserForm(request.POST, instance=request.user)
		return render(request, self.template_name, {'form': self.form,'form1':self.form1})
	
	def post(self, request, *args, **kwargs):
		p=emp.objects.filter(user=request.user).first()
		form =empForm(request.POST, instance=p)
		form1=UserForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			if form1.is_valid():
				form1.save()
			else:
				print("error1")
		else:
			print("error")
		return render(request, self.template_name, {'form': self.form,'form1':self.form1})

class SearchPage(View):
	template_name='employee/search.html'
	model=emp

	def get(self, request, *args, **kwargs):
		emp_list=emp.objects.all()
		emp_filter=EmpFilter(request.GET,queryset=emp_list)
		return render(request,self.template_name,{'filter':emp_filter})

	'''def post(self, request, *args, **kwargs):
		emp_list=emp.objects.all()
		emp_filter=EmpFilter(request.GET,queryset=emp_list)
		return render(request,self.template_name,{'filter':emp_filter})'''

class UpdatePage(LoginRequiredMixin,View):
	template_name='employee/update.html'
	'''form=updateForm()

	def get(self, request, *args, **kwargs):
		p, created = MyModel.objects.get_or_create(id=self.kwargs['id'])'''

	def get(self, request, *args, **kwargs):
		emp1=emp.objects.filter(id=kwargs['ab'])
		return render(request, self.template_name, {'emp1': emp1})
	
	def post(self, request, *args, **kwargs):
		p, created = emp.objects.get_or_create(id=kwargs['ab'])
		q = User.objects.get(username=p.user)
		if not created:
			p.empid=request.POST['eid']
			q.first_name=request.POST['fname']
			q.last_name=request.POST['lname']
			p.housename=request.POST['housename']
			p.city=request.POST['city']
			p.state=request.POST['state']
			p.pincode=request.POST['pincode']
			p.mobile=request.POST['mobile']
			if request.POST['user1'] == "superuser":
				q.is_superuser = True
				q.is_staff=False
			elif request.POST['user1'] == "staff":
				q.is_superuser =False
				q.is_staff = True
			else:
				q.is_superuser = False
				q.is_staff=False
			p.save()
			q.save()
		return redirect('search')



