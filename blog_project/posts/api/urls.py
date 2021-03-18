from django.urls import include, path
from rest_framework import routers
from posts.api import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
# router.register(r"groups", views.GroupViewSet)
router.register(r"posts", views.PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls",
                              namespace="rest_framework")),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(
        template_name="posts/swagger-ui.html", url_name="schema"
    ),
        name="swagger-ui",
    ),
]
