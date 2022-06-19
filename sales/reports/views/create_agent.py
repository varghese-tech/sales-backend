from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from reports.serializers import AgentsSerializer
from reports.utils import response_create_ok, bad_response


@csrf_exempt
def create_agent(request):
    """
    Creates a new agent
    """
    if request.method == "POST":
        agent_data = JSONParser().parse(request)
        agent_serializer = AgentsSerializer(data=agent_data)
        if agent_serializer.is_valid():
            agent_serializer.save()
            return JsonResponse(
                response_create_ok("Created Successfully!!!!!!"), safe=False
            )
        return JsonResponse(
            bad_response("Failed to create agent.", agent_serializer.errors), safe=False
        )
    return JsonResponse(bad_response("Not an allowed method"), safe=False)
