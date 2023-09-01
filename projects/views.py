from django.shortcuts import render
from rest_framework import viewsets, permissions

from projects.models import Profile, Project
from projects.serializers.profile_serializer import ProfileSerializer
from projects.serializers.project_serializer import ProjectSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if self.request.method == "GET":
            profile = Profile.objects.get(id=kwargs["pk"])
            context = {
                "profile": profile,
                "projects": profile.projects.all(),
            }

            return render(request, "profile_detail.html", context)

        return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
