from django.urls import path

from core.api.v1.views import SocialMediaCreateOrUpdateView, SocialMediaVariationListView, SocialMediaVerifyView, \
    SocialMediaDeleteView

urlpatterns = [
    path('social-media-variation/list/', SocialMediaVariationListView.as_view(),
         name="social-media-variation-list"),
    path('social-media/set/', SocialMediaCreateOrUpdateView.as_view(),
         name="social-media-set"),
    path('social-media/check-verification/', SocialMediaVerifyView.as_view(),
         name="social-media-check-verification"),
    path('social-media/delete/', SocialMediaDeleteView.as_view(),
         name="social-media-delete")
]
