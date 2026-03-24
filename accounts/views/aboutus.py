from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import AboutUs


# GET About Us

@api_view(['GET'])
def about_us_get(request):

    about = AboutUs.objects.first()

    if not about:
        return Response({
            "id": None,
            "about_text": "",
            "location": "",
            "email": "",

            "management_name": "",
            "management_title": "",
            "management_message": "",
            "management_photo": "",

            "principal_name": "",
            "principal_title": "",
            "principal_message": "",
            "principal_photo": "",
        })

    return Response({
        "id": about.id,
        "about_text": about.about_text,
        "location": about.location,
        "email": about.email,

        "management_name": about.management_name,
        "management_title": about.management_title,
        "management_message": about.management_message,
        "management_photo": about.management_photo.url if about.management_photo else "",

        "principal_name": about.principal_name,
        "principal_title": about.principal_title,
        "principal_message": about.principal_message,
        "principal_photo": about.principal_photo.url if about.principal_photo else "",
    })

# CREATE About Us

@api_view(['POST'])
def about_us_create(request):

    # check if already exists
    if AboutUs.objects.exists():
        return Response({
            "error": "About Us already exists. Use Update ."
        })
        
    about = AboutUs.objects.create(
        about_text=request.data.get('about_text'),
        location=request.data.get('location'),
        email=request.data.get('email'),

        management_name=request.data.get('management_name'),
        management_title=request.data.get('management_title'),
        management_message=request.data.get('management_message'),
        management_photo=request.FILES.get('management_photo'),

        principal_name=request.data.get('principal_name'),
        principal_title=request.data.get('principal_title'),
        principal_message=request.data.get('principal_message'),
        principal_photo=request.FILES.get('principal_photo'),
    )

    return Response({
        "message": "Created Successfully",
        "id": about.id
    })

# UPDATE About Us

@api_view(['PUT'])
def about_us_update(request, id):
    try:
        about = AboutUs.objects.get(id=id)
    except AboutUs.DoesNotExist:
        return Response({"error": "Not found"}, status=404)
    about.about_text = request.data.get('about_text', about.about_text)
    about.location = request.data.get('location', about.location)
    about.email = request.data.get('email', about.email)
    about.management_name = request.data.get('management_name', about.management_name)
    about.management_title = request.data.get('management_title', about.management_title)
    about.management_message = request.data.get('management_message', about.management_message)
    if request.FILES.get('management_photo'):
        about.management_photo = request.FILES.get('management_photo')
    about.principal_name = request.data.get('principal_name', about.principal_name)
    about.principal_title = request.data.get('principal_title', about.principal_title)
    about.principal_message = request.data.get('principal_message', about.principal_message)
    if request.FILES.get('principal_photo'):
        about.principal_photo = request.FILES.get('principal_photo')
    about.save()
    return Response({"message": "Updated Successfully"})

# DELETE About Us

@api_view(['DELETE'])
def about_us_delete(request):

    about = AboutUs.objects.first()

    if not about:
        return Response({
            "message": "Nothing to delete"
        })

    about.delete()

    return Response({
        "message": "Deleted Successfully"
    })