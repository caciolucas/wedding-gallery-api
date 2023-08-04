from authentication.views import SingleTokenView
from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('token/', SingleTokenView.as_view(), name='token_obtain_pair'),
    # Since each session shouldn't take too long, we don't need to add a refresh token view
    path('token/verify', TokenVerifyView.as_view(), name='token_verify'),
]
