from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import Facility



# CREATE FACILITY


@api_view(['POST'])
def add_facility(request):

    facility = Facility.objects.create(
        name=request.data.get("name"),
        features=request.data.get("features"),
        image=request.FILES.get("image")
    )

    return Response({
        "message": "Facility added successfully",
        "id": facility.id
    })


# GET FACILITIES


@api_view(['GET'])
def list_facilities(request):

    facilities = Facility.objects.all()

    data = []

    for f in facilities:
        data.append({
            "id": f.id,
            "name": f.name,
            "features": f.features,
            "image": f.image.url if f.image else None
        })

    return Response(data)



# UPDATE FACILITY


@api_view(['PUT'])
def update_facility(request, id):

    try:
        facility = Facility.objects.get(id=id)
    except Facility.DoesNotExist:
        return Response({"error": "Facility not found"})

    facility.name = request.data.get("name", facility.name)
    facility.features = request.data.get("features", facility.features)

    new_image = request.FILES.get("image")

    if new_image:
        facility.image = new_image

    facility.save()

    return Response({
        "message": "Facility updated successfully"
    })


# =========================
# DELETE FACILITY
# =========================

@api_view(['DELETE'])
def delete_facility(request, id):

    try:
        facility = Facility.objects.get(id=id)
    except Facility.DoesNotExist:
        return Response({"error": "Facility not found"})

    facility.delete()

    return Response({
        "message": "Facility deleted"
    })