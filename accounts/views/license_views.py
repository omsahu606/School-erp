import requests
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from accounts.models import License
from datetime import timedelta
from django.utils import timezone


# ACTIVATE LICENSE

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def activate_license(request):

    code = request.data.get("activation_code")
    email = request.data.get("email")

    if not code or not email:
        return Response(
            {"error": "Activation code and email required"},
            status=400
        )

    try:
        response = requests.post(
            "http://127.0.0.1:9000/api/license/verify/",
            json={
                "activation_code": code,
                "email": email
            },
            timeout=5
        )

        data = response.json()

    except Exception:
        return Response(
            {"error": "License server not reachable"},
            status=500
        )

    # invalid code
    if "error" in data:
        return Response(
            {"error": "Invalid activation code"},
            status=400
        )

    # save license locally
    License.objects.update_or_create(
        id=1,
        defaults={
            "activation_code": code,
            "plan_name": data["plan"],
            "expiry_date": timezone.now() + timedelta(days=data["duration_days"]),
            "is_active": True
        }
    )

    return Response({
        "message": "ERP Activated",
        "plan": data["plan"]
    })



# CHECK LICENSE STATUS

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def check_license_status(request):

    license = License.objects.filter(is_active=True).first()

    # license nahi hai
    if not license:
        return Response({
            "active": False
        })

    # expiry check
    if license.expiry_date < timezone.now():

        license.is_active = False
        license.save()

        return Response({
            "active": False
        })

    return Response({
        "active": True,
        "plan": license.plan_name,
        "expiry_date": license.expiry_date
    })
    
    
#deactivate_license
@api_view(['POST'])
def deactivate_license(request):

    email = request.data.get("email")

    license = License.objects.first()

    if not license:
        return Response({"error": "No license found"})

    license.is_active = False
    license.save()

    return Response({
        "message": "ERP Deactivated"
    })