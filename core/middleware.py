from django.core.handlers.wsgi import WSGIRequest
import json
from core.models import User
from rest_framework import status
from django.utils import timezone
from django.http import JsonResponse

class LoginAttemptsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: WSGIRequest):
        body = request.body
        response = self.get_response(request)

        if request.path == "/api/token":
            content_type = request.headers.get("Content-Type", '').lower

            if 'application/json' in content_type:

                try:
                    email = json.loads(body.decode('utf-8')).get('email')
                except json.JSONDecodeError:
                    email = None

            elif 'application/x-www-form-urlencoded' in content_type:
                email = request.POST.get('email')

            else:
                email = None

            if email: 
                user = User.objects.get(email=email)

                if user and response.status_code == status.HTTP_401_UNAUTHORIZED:
                    user.login_attempts += 1
                    user.save()

                    if user.login_attempts == 3:
                        user.locked_at = timezone.now()
                        user.unlocked_at = timezone.now() + timezone.timedelta(minutes=15)
                        user.save()

                        return JsonResponse(
                            {'detail': 'Conta bloqueada, tente daqui 15 minutos'},
                            status.HTTP_401_UNAUTHORIZED
                        )

                if user.login_attempts >=3 and user.locked_at != None and user.unlocked_at != None and status.HTTP_200_OK:
                    if timezone.now() >= user.unlocked_at:
                        user.login_attempts = 0
                        user.locked_at = None
                        user.unlocked_at = None
                        user.save()
                    else:
                        return JsonResponse(
                            {'detail': 'Sua conta foi bloqueada tente mais tarde'},
                            status=status.HTTP_418_IM_A_TEAPOT
                        )
        return response
