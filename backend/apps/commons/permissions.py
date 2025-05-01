from typing import Any
from urllib.request import Request

from django.conf import settings
from rest_framework.permissions import BasePermission


class ApiKeyPermission(BasePermission):
    def has_permission(self, request: Request, view: Any) -> bool:
        api_key = request.headers.get('X-Api-Key')
        return api_key == settings.X_API_KEY
