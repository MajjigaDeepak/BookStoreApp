from urllib import request

from django.shortcuts import render
from rest_framework import viewsets
from .serializers import authorSerializer,bookSerializer,orderSerializer
from .models import authors,books,orders
from django.db.models import Count
from django.views import View
from django.http import HttpResponse
# Create your views here.


class authorViewset(viewsets.ModelViewSet):

    queryset = authors.objects.all()
    serializer_class = authorSerializer

class bookViewset(viewsets.ModelViewSet):

    queryset = books.objects.all()
    serializer_class = bookSerializer

class orderViewset(viewsets.ModelViewSet):

    queryset = orders.objects.all()
    serializer_class = orderSerializer

class successfulAuthors(View):
    def get(self, request):
        v=orders.objects.all().values('bought').annotate(total=Count('bought')).order_by('total')[3:]
        i=list(v.values('bought'))
        k=i[0]['bought']
        b=books.objects.all().values('authorName').filter(pk=k)
        j=list(b.values('authorName'))
        l=j[0]['authorName']
        a=authors.objects.all().values('name').filter(pk=l)
        m=list(a.values('name'))
        n=m[0]['name']
        return HttpResponse("Successful Author is :"+ n)



