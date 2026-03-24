from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import SchoolMap, ContactMessage



# ADD SCHOOL CONTACT INFO


@api_view(['POST'])
def add_school_contact(request):

    school = SchoolMap.objects.create(
        address=request.data.get("address"),
        phone=request.data.get("phone"),
        email=request.data.get("email"),
        map_embed=request.data.get("map_embed")
    )

    return Response({
        "message": "School contact saved"
    })

# GET SCHOOL CONTACT INFO


@api_view(['GET'])
def contact_info(request):

    school = SchoolMap.objects.first()

    if not school:
        return Response({"error": "No contact info found"})

    return Response({
        "id": school.id,
        "address": school.address,
        "phone": school.phone,
        "email": school.email,
        "map_embed": school.map_embed
    })

# UPDATE SCHOOL CONTACT


@api_view(['PUT'])
def update_school_contact(request, id):

    try:
        school = SchoolMap.objects.get(id=id)
    except SchoolMap.DoesNotExist:
        return Response({"error": "Contact info not found"})

    school.address = request.data.get("address", school.address)
    school.phone = request.data.get("phone", school.phone)
    school.email = request.data.get("email", school.email)
    school.map_embed = request.data.get("map_embed", school.map_embed)

    school.save()

    return Response({
        "message": "School contact updated successfully"
    })

# DELETE SCHOOL CONTACT


@api_view(['DELETE'])
def delete_school_contact(request, id):

    try:
        school = SchoolMap.objects.get(id=id)
    except SchoolMap.DoesNotExist:
        return Response({"error": "Contact info not found"})

    school.delete()

    return Response({
        "message": "School contact deleted successfully"
    })


# =============================
# CONTACT FORM SUBMIT
# =============================

@api_view(['POST'])
def contact_submit(request):

    name = request.data.get("name")
    email = request.data.get("email")
    phone = request.data.get("phone")
    message = request.data.get("message")

    ContactMessage.objects.create(
        name=name,
        email=email,
        phone=phone,
        message=message
    )

    return Response({
        "message": "Message sent successfully"
    })


# =============================
# CONTACT MESSAGES LIST
# =============================

@api_view(['GET'])
def contact_messages(request):

    messages = ContactMessage.objects.all().order_by("-created_at")

    data = []

    for m in messages:
        data.append({
            "id": m.id,
            "name": m.name,
            "email": m.email,
            "phone": m.phone,
            "message": m.message,
            "is_read": m.is_read,
            "created_at": m.created_at
        })

    return Response(data)


# =============================
# MARK MESSAGE AS READ
# =============================

@api_view(['POST'])
def mark_message_read(request, id):

    try:
        message = ContactMessage.objects.get(id=id)
    except ContactMessage.DoesNotExist:
        return Response({"error": "Message not found"})

    message.is_read = True
    message.save()

    return Response({
        "message": "Message marked as read"
    })


# =============================
# DELETE MESSAGE


@api_view(['DELETE'])
def delete_contact_message(request, id):

    try:
        message = ContactMessage.objects.get(id=id)
    except ContactMessage.DoesNotExist:
        return Response({"error": "Message not found"})

    message.delete()

    return Response({
        "message": "Contact message deleted successfully"
    })