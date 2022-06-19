from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from reports.models import Agents, Reports
from reports.serializers import AgentsSerializer, ReportsSerializer
from reports.utils import response_get_ok, bad_response


@csrf_exempt
def get_reports(request, id=None):
    """
    Get all reports from all agents or of 
    a specific agent
    """
    if request.method == "GET":
        if id == None:
            reports = Reports.objects.all()
        else:
            reports = Reports.objects.filter(AgentId=id)
        reports_serializer = ReportsSerializer(reports, many=True)
        return JsonResponse(response_get_ok(reports_serializer.data), safe=False)
    return JsonResponse(bad_response("Not an allowed method"), safe=False)
