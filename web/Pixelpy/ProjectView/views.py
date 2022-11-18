from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from ProjectView.models import Project
from ProjectView.serializers import ProjectSerializer
# Create your views here.

@csrf_exempt
def projectApi(request,id=0):
    if request.method=='GET':
        project=Project.objects.all()
        project_serializer = ProjectSerializer(project,many=True)
        return JsonResponse(project_serializer.data,safe=False)
    elif request.method == 'POST':
        project_data=JSONParser().parse(request)
        project_serializer= ProjectSerializer(data=project_data)
        if project_serializer.is_valid():
            project_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        project_data = JSONParser().parse(request)
        project=Project.objects.get(Sim_ID= project_data['Sim_ID'])
        project_serializer = ProjectSerializer(project,data=project_data)
        if project_serializer.is_valid():
            project_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        project = Project.objects.get(Sim_ID=id)
        project.delete()
        return JsonResponse("Delete Successfully",safe=False)
