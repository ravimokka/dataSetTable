from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import datetime
from django.views import View
from .models import *
import json
import requests
from django.core import serializers


class LoadHomePage(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, 'home_page.html')


class FetchTableData(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        # api_data = requests.get('http://devtest.hlx.mk/api/developer_example?template_id=100&api_key=3e272064-f4a0'
        #                         '-sumit-4deb39a03c5c')
        # json_data = api_data.json()
        # CompanyInfo.objects.all().delete()
        # for i in json_data:
        #     Amazon = i.get('AmazonShipmentID')
        #     Company = i.get('CompanyName')
        #     Date = i.get('CreatedDate')
        #     PNumber = i.get('PRONumber')
        #     ShipS = i.get('ShipStatus')
        #     ShipSN = i.get('ShipStatusNum')
        #     TotalC = i.get('TotalCartons')
        #
        #     company_data = CompanyInfo.objects.create(AmazonShipmentID=Amazon, CompanyName=Company, CreatedDate=Date,
        #                                PRONumber=PNumber, ShipStatus=ShipS, ShipStatusNum=ShipSN, TotalCartons=TotalC)
        #     company_data.save()

        orm_data = CompanyInfo.objects.all()
        table_data = []

        if orm_data:
            for i in orm_data:
                table_data.append({'id': i.pk, 'AmazonShipmentID': i.AmazonShipmentID, 'CompanyName': i.CompanyName,
                                   'CreatedDate': i.CreatedDate, 'PRONumber': i.PRONumber,
                                   'ShipStatus': i.ShipStatus, 'ShipStatusNum': i.ShipStatusNum,
                                   'TotalCartons': i.TotalCartons, 'input_type': 'False'})
            return JsonResponse({'data': table_data})
        else:
            return JsonResponse({'massage': 'empty'})


class UpdateTableData(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        req_data = request.body
        request_data = json.loads(req_data)
        row_id = request_data['row_id']
        pro_num = request_data['pro_num']
        c_name = request_data['c_name']
        c_data = request_data['c_data']
        a_ship = request_data['a_ship']
        total_car = request_data['total_car']
        ship_s = request_data['ship_s']
        ss_num = request_data['ss_num']
        company_data = CompanyInfo.objects.filter(pk=row_id).update(AmazonShipmentID=a_ship, CompanyName=c_name,
                                                  CreatedDate=c_data, PRONumber=pro_num, ShipStatus=ship_s,
                                                  ShipStatusNum=ss_num,  TotalCartons=total_car)
        orm_data = CompanyInfo.objects.all()
        table_data = []
        if orm_data:
            for i in orm_data:
                table_data.append({'id': i.pk, 'AmazonShipmentID': i.AmazonShipmentID, 'CompanyName': i.CompanyName,
                                   'CreatedDate': i.CreatedDate, 'PRONumber': i.PRONumber,
                                   'ShipStatus': i.ShipStatus, 'ShipStatusNum': i.ShipStatusNum,
                                   'TotalCartons': i.TotalCartons, 'input_type': 'False'})
            return JsonResponse({'data': table_data})
        else:
            return JsonResponse({'massage': 'empty'})


class DeleteTableData(View):
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        req_data = request.body
        request_data = json.loads(req_data)
        row_id = request_data['row_id']
        company_data = CompanyInfo.objects.filter(pk=row_id).delete()
        orm_data = CompanyInfo.objects.all()
        table_data = []
        if orm_data:
            for i in orm_data:
                table_data.append({'id': i.pk, 'AmazonShipmentID': i.AmazonShipmentID, 'CompanyName': i.CompanyName,
                                   'CreatedDate': i.CreatedDate, 'PRONumber': i.PRONumber,
                                   'ShipStatus': i.ShipStatus, 'ShipStatusNum': i.ShipStatusNum,
                                   'TotalCartons': i.TotalCartons, 'input_type': 'False'})
            return JsonResponse({'data': table_data})
        else:
            return JsonResponse({'massage': 'empty'})