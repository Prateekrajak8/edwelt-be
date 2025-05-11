from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
import random

from user.models import UserRegistration

class RegisterUserAPIView(APIView):
    def post(self, request, *args, **kwargs):
        # Extract fields from request data
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        phone_number = request.data.get('phone_number')
        role = request.data.get('role')  # e.g., '12th Pass', 'Graduate', etc.
        neet_rank = request.data.get('neet_rank')

        # Basic validation
        errors = {}
        if not first_name:
            errors['first_name'] = "First name is required."
        if not phone_number:
            errors['phone_number'] = "Phone number is required."
        if not role:
            errors['role'] = "Role selection is required."

        if errors:
            return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)
        user = UserRegistration.objects.filter(phone_number=phone_number)
        if not user.exists():
            UserRegistration.objects.create(
                first_name=first_name,
                last_name=last_name,
                phone_number=phone_number,
                role=role,
                neet_rank=neet_rank
            )
        # Generate OTP
        otp = str(random.randint(100000, 999999))

        # Store OTP in cache for 5 minutes
        cache.set(f"otp_{phone_number}", otp, timeout=300)

        # TODO: Send OTP via SMS here (integrate SMS gateway)

        return Response({
            "message": "OTP sent successfully to your phone number.",
            # For testing purposes only; in production don't send OTP in response
            "otp": otp
        }, status=status.HTTP_200_OK)