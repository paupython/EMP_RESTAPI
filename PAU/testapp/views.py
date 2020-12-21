from django.shortcuts import render
from django.views.generic import View
from testapp.models import Employee
import json
from django.http import HttpResponse
from django.core.serializers import serialize
# Create your views here.


class EmployeeCBV(View):

    def get(self,request,*args,**kwargs):
        emp=Employee.objects.all()
        sdata=serialize('json',emp)
        pydata=json.loads(sdata)
        temp_pydata=[]
        for value in pydata:
            temp_pydata.append(value.get('fields'))
        return HttpResponse(json.dumps(temp_pydata),status=200)
