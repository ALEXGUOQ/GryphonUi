#coding:utf-8
from django.http import HttpResponse

# 美女
def girls(request,pageIndex):
	return HttpResponse('美女')