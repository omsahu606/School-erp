from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import SchoolSettingsinfo


# ADD SCHOOL SETTINGS

@api_view(['POST'])
def add_school_settings(request):

    school = SchoolSettingsinfo.objects.first()

    if school:
        return Response({
            "message": "School settings already exist"
        })

    school = SchoolSettingsinfo.objects.create(
        school_name=request.data.get("school_name"),
        email=request.data.get("email"),
        phone_number=request.data.get("phone_number"),
        address=request.data.get("address"),
        description=request.data.get("description"),
        logo=request.FILES.get("logo")
    )

    return Response({
        "message": "School settings created",
        "id": school.id
    })


# GET SCHOOL SETTINGS


@api_view(['GET'])
def get_school_settings(request):

    school = SchoolSettingsinfo.objects.first()

    if not school:
        return Response({"error": "Settings not found"})

    return Response({
        "id": school.id,
        "school_name": school.school_name,
        "email": school.email,
        "phone_number": school.phone_number,
        "address": school.address,
        "description": school.description,
        "logo": school.logo.url if school.logo else None
    })


# UPDATE SCHOOL SETTINGS

@api_view(['PUT'])
def update_school_settings(request):

    school = SchoolSettingsinfo.objects.first()

    if not school:
        return Response({"error": "Settings not found"})

    school.school_name = request.data.get("school_name", school.school_name)
    school.email = request.data.get("email", school.email)
    school.phone_number = request.data.get("phone_number", school.phone_number)
    school.address = request.data.get("address", school.address)
    school.description = request.data.get("description", school.description)

    if request.FILES.get("logo"):
        school.logo = request.FILES.get("logo")

    school.save()

    return Response({
        "message": "School settings updated successfully"
    })



# DELETE SCHOOL SETTINGS

@api_view(['DELETE'])
def delete_school_settings(request):

    school = SchoolSettingsinfo.objects.first()

    if not school:
        return Response({"error": "Settings not found"})

    school.delete()

    return Response({
        "message": "School settings deleted successfully"
    })