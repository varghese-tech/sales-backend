from django.urls import path
from reports.views import create_agent, get_agents, create_report, get_reports

urlpatterns = [
    path("create_agent", create_agent.create_agent, name="create_agent"),
    path("get_agents", get_agents.get_agents, name="get_agents"),
    path("create_report", create_report.create_report, name="create_report"),
    path("get_reports", get_reports.get_reports, name="get_reports"),
    path("get_reports/<id>", get_reports.get_reports, name="get_reports"),
]
