from rest_framework import serializers

from projects.models import CertifyingInstitution, Certificate
from projects.serializers.certificate_serializer import CertificateSerializer


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = CertificateSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = ("id", "name", "url", "certificates")

    def create(self, validated_data):
        certificates_data = validated_data.pop("certificates")
        institution = CertifyingInstitution.objects.create(**validated_data)

        for certificate_data in certificates_data:
            Certificate.objects.create(
                certifying_institution=institution,
                **certificate_data
            )

        return institution
