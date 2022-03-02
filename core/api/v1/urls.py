from django.urls import path

from core.api.v1.views import SocialMediaCreateView, SocialMediaVariationListView, SocialMediaVerifyView, \
    SocialMediaDeleteView, SocialMediaUpdateView

urlpatterns = [
    path('social-media-variation/list/', SocialMediaVariationListView.as_view(),
         name="social-media-variation-list"),
    path('social-media/create/', SocialMediaCreateView.as_view(),
         name="social-media-create"),
    path('social-media/update/', SocialMediaUpdateView.as_view(),
         name="social-media-update"),
    path('social-media/check-verification/', SocialMediaVerifyView.as_view(),
         name="social-media-check-verification"),
    path('social-media/delete/', SocialMediaDeleteView.as_view(),
         name="social-media-delete")
]
