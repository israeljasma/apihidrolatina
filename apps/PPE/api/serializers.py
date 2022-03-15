from apps.PPE.models import detectionPPE

from rest_framework import serializers

from apps.users.api.serializers import UserPPESerializer

class detectionPPESerializers(serializers.ModelSerializer):

    class Meta:
        model = detectionPPE
        exclude = ('state',)

class detectionPPERepresentationSerializers(serializers.ModelSerializer):

    user = UserPPESerializer(read_only=True)

    class Meta:
        model = detectionPPE
        fields = ('id', 'helmet', 'headphones', 'goggles', 'gloves', 'boots', 'date', 'created_date', 'modified_date', 'user')
        # exclude = ('state',)