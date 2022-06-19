from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from reports.serializers import ReportsSerializer
from reports.utils import response_create_ok, bad_response


@csrf_exempt
def create_report(request):
    """
    Create a new sales report
    """
    if request.method == "POST":
        report_data = JSONParser().parse(request)
        report_serializer = ReportsSerializer(data=report_data)
        if report_serializer.is_valid():
            report_serializer.save()
            return JsonResponse(
                response_create_ok("Created Successfully!!!!!!"), safe=False
            )
        return JsonResponse(
            bad_response("Failed to create report.", report_serializer.errors),
            safe=False,
        )
    return JsonResponse(bad_response("Not an allowed method"), safe=False)
