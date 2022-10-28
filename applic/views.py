from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from applic.models import Bill,Details
from applic.serializer import DetailSerializer,BillSerializer


@csrf_exempt
def DetailsApi(request,Billno = 0):
    if request.method=='GET':
        Detail=Details.objects.all()
        Detail_Serializer=DetailSerializer(Detail,many=True)
        return JsonResponse(Detail_Serializer.data,safe=False)
    elif request.method=='POST':
        Detail_Data=JSONParser().parse(request)
        Detail_Serializer=DetailSerializer(data=Detail_Data)
        if Detail_Serializer.is_valid():
            Detail_Serializer.save()
            return JsonResponse("added successfully",safe=False)
        return JsonResponse("unable to add",safe=False)
    elif request.method=='PUT':
        Detail_Data=JSONParser().parse(request)
        Detail=Details.objects.get(billno=Detail_Data['billno'])
        Detail_Serializer=DetailSerializer(Detail,data=Detail_Data)
        if Detail_Serializer.is_valid():
            Detail_Serializer.save()
            return JsonResponse("the value is valid",safe=False)
        return JsonResponse("this input is not valid",safe=False)
    elif request.method=="DELETE":
        Detail=Details.objects.get(billno=Billno)
        Detail.delete()
        return JsonResponse("DELETED",safe=False)
              
@csrf_exempt
def BillApi(request,Billno = 0):
    if request.method=='GET':
        Bills=Bill.objects.all()
        Bill_Serializer=BillSerializer(Bills,many=True)
        return JsonResponse(Bill_Serializer.data,safe=False)
    elif request.method=='POST':
        Bill_Data=JSONParser().parse(request)
        Bill_Serializer=BillSerializer(data=Bill_Data)
        if Bill_Serializer.is_valid():
            Bill_Serializer.save()
            return JsonResponse("added successfully",safe=False)
        return JsonResponse("unable to add",safe=False)
    elif request.method=='PUT':
        Bill_Data=JSONParser().parse(request)
        Bills=Bill.objects.get(billno=Bill_Data['billno'])
        Bill_Serializer=DetailSerializer(Bills,data=Bill_Data)
        if Bill_Serializer.is_valid():
            Bill_Serializer.save()
            return JsonResponse("the value is valid",safe=False)
        return JsonResponse("this input is not valid",safe=False)
    elif request.method=="DELETE":
        Bills=Bill.objects.get(billno=Billno)
        Bills.delete()
        return JsonResponse("DELETED",safe=False)