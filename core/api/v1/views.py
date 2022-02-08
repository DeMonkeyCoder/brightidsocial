import requests as requests
from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.utils.translation import gettext as _

from core.api.v1.serializers import SocialMediaCreateOrUpdateSerializer, SocialMediaVariationSerializer
from core.consts import SocialMediaBrightVerificationStatus
from core.models import SocialMediaVariation, SocialMedia
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class SocialMediaVariationListView(generics.ListAPIView):
    serializer_class = SocialMediaVariationSerializer
    queryset = SocialMediaVariation.objects.all()


class SocialMediaCreateOrUpdateView(generics.GenericAPIView):
    """
        Create or Update social media profile
    """
    serializer_class = SocialMediaCreateOrUpdateSerializer

    def post(self, request, *args, **kwargs):

        # so the user is updating social media profile
        if request.user.is_authenticated:
            social_media = request.user.social_media
            serializer = self.get_serializer(instance=social_media, data=request.data)
            serializer.is_valid(raise_exception=True)
            instance = serializer.save()

        else:
            social_media_variation = get_object_or_404(SocialMediaVariation, pk=request.data.get('variation'))

            with transaction.atomic():
                social_media_qs = SocialMedia.objects.select_for_update().filter(
                    profile=request.data.get('profile'),
                    network=request.data.get('network'),
                    variation=social_media_variation,
                    bright_verification_status=SocialMediaBrightVerificationStatus.VERIFIED
                )
                if social_media_qs.exists():
                    return Response({'status': _("Social media already exists")}, status=400)
                else:
                    serializer = self.get_serializer(data=request.data)
                    serializer.is_valid(raise_exception=True)

                instance = serializer.save()

        return Response(self.get_serializer(instance=instance).data, status=200)


class SocialMediaVerifyView(APIView):
    """
        Check if BrightID app linked the social media profile
    """
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        with transaction.atomic():
            social_media = SocialMedia.objects.select_for_update().get(
                django_user=request.user
            )
            if social_media.bright_verification_status == SocialMediaBrightVerificationStatus.VERIFIED:
                return Response(status=204)
            network = social_media.network
            app_name = social_media.variation.bright_id_app_name
            if app_name:
                response = requests.get(
                    f'http://{network}.brightid.org/brightid/v6/verifications/{app_name}/{social_media.id}'
                ).json()
                if 'error' in response:
                    return Response(response, 400)
                social_media.bright_verification_status = SocialMediaBrightVerificationStatus.VERIFIED
                return Response(status=204)
            else:
                return Response({'error': True, 'errorMessage': _('Verification not available for this social media '
                                                                  'variation')}, 400)
