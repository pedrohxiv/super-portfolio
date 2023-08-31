from rest_framework import viewsets

from projects.models import Profile, Project
from projects.serializers.profile_serializer import ProfileSerializer
from projects.serializers.project_serializer import ProjectSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
