from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from reports.models import Agents
from reports.serializers import AgentsSerializer
from reports.utils import response_get_ok, bad_response


@csrf_exempt
def get_agents(request):
    """
    Get all available agents
    """
    if request.method == "GET":
        agents = Agents.objects.all()
        agents_serializer = AgentsSerializer(agents, many=True)
        return JsonResponse(response_get_ok(agents_serializer.data), safe=False)
    return JsonResponse(bad_response("Not an allowed method"), safe=False)
