from rest_framework import serializers
from reports.models import Agents, Reports

class AgentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agents
        fields = ('AgentId', 
        'Name', 
        'Hired', 
        'Birthday', 
        'City')

class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = ('ReportId', 
        'AgentId', 
        'Period', 
        'Volume')
