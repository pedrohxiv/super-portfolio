from rest_framework import serializers

from projects.models import Certificate


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = (
            "id",
            "name",
            "certifying_institution",
            "timestamp",
            "profiles",
        )
