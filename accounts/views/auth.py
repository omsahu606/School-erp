from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


# ================= ADMIN LOGIN =================
@api_view(['POST'])
def admin_login(request):

    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None and user.is_staff:

        refresh = RefreshToken.for_user(user)

        return Response({
            "message": "Admin Login Successful",
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })

    return Response({"error": "Invalid Admin Credentials"})

# ================= LOGOUT =================
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def admin_logout(request):

    try:
        refresh_token = request.data.get("refresh")
        token = RefreshToken(refresh_token)
        token.blacklist()

        return Response({"message": "Logout successful"})

    except Exception:
        return Response(
            {"error": "Invalid token"},
            status=status.HTTP_400_BAD_REQUEST
        )

# ================= DASHBOARD =================
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def admin_dashboard(request):

    return Response({
        "message": "Welcome Admin Dashboard",
        "user": request.user.username
    })

