
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    path('', csrf_exempt(LoadHomePage.as_view()), name="LoadHomePage"),
    path('api/tableData', csrf_exempt(FetchTableData.as_view()), name="FetchTableData"),
    path('api/update', csrf_exempt(UpdateTableData.as_view()), name="UpdateTableData"),
    path('api/delete', csrf_exempt(DeleteTableData.as_view()), name="DeleteTableData"),
]
