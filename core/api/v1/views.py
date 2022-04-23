from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.api.v1.serializers import SocialMediaVariationSerializer, \
    SocialMediaVerifySerializer, SocialMediaCreateSerializer, SocialMediaUpdateSerializer, \
    SocialMediaQueryAPISerializer
from core.bright_utils import is_user_app_id_linked
from core.consts import SocialMediaBrightVerificationStatus
from core.models import SocialMediaVariation, SocialMedia, ProfileHash


class SocialMediaVariationListView(generics.ListAPIView):
    """
        List social media variations
    """
    serializer_class = SocialMediaVariationSerializer
    queryset = SocialMediaVariation.objects.all()


class SocialMediaCreateView(generics.CreateAPIView):
    """
        Create or Update social media profile
    """
    serializer_class = SocialMediaCreateSerializer


class SocialMediaUpdateView(generics.UpdateAPIView):
    """
        Update social profile of user
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = SocialMediaUpdateSerializer

    def get_object(self):
        return self.request.user.social_media


class SocialMediaVerifyView(generics.GenericAPIView):
    """
        Check if BrightID app linked the social media profile
    """
    serializer_class = SocialMediaVerifySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        network = serializer.validated_data.get('network')
        context_id = serializer.validated_data.get('context_id')
        social_media = get_object_or_404(SocialMedia,
                                         id=context_id,
                                         network=network
                                         )
        result, response = social_media.get_and_save_verification_status(is_user_app_id_linked)
        if result:
            return Response(status=204)
        return Response(response, status=400)


class SocialMediaDeleteView(generics.DestroyAPIView):
    """
        Remove social profile of user from search queries
    """
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user.social_media

    def perform_destroy(self, instance):
        instance.profile_hashes.all().delete()


class SocialMediaQueryView(generics.GenericAPIView):
    """
        Find social profiles that are registered in the app
    """
    serializer_class = SocialMediaQueryAPISerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        serializer.is_valid(raise_exception=True)

        network = serializer.validated_data.get('network')
        profile_hashes = serializer.validated_data.get('profile_hashes')

        filtered_profile_hashes = ProfileHash.objects.filter(
            value__in=profile_hashes,
            social_media__network=network,
            social_media__bright_verification_status=SocialMediaBrightVerificationStatus.VERIFIED,
        ).values_list('value', flat=True).distinct()

        return Response(list(filtered_profile_hashes), status=200)
