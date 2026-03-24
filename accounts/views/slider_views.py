from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import Slider


# ADD SLIDER

@api_view(['POST'])
def add_slider(request):

    slider = Slider.objects.create(
        title=request.data.get("title"),
        subtitle=request.data.get("subtitle"),
        image=request.FILES.get("image"),
        order=request.data.get("order")
    )

    return Response({
        "message": "Slider added",
        "id": slider.id
    })


# GET SLIDERS

@api_view(['GET'])
def list_sliders(request):

    sliders = Slider.objects.filter(is_active=True).order_by('order')

    data = []

    for s in sliders:
        data.append({
            "id": s.id,
            "title": s.title,
            "subtitle": s.subtitle,
            "image": s.image.url if s.image else None,
            "order": s.order
        })

    return Response(data)


# =========================
# UPDATE SLIDER
# =========================

@api_view(['PUT'])
def update_slider(request, id):

    try:
        slider = Slider.objects.get(id=id)
    except Slider.DoesNotExist:
        return Response({"error": "Slider not found"})

    slider.title = request.data.get("title", slider.title)
    slider.subtitle = request.data.get("subtitle", slider.subtitle)
    slider.order = request.data.get("order", slider.order)

    new_image = request.FILES.get("image")

    if new_image:
        slider.image = new_image

    slider.save()

    return Response({
        "message": "Slider updated"
    })


# DELETE SLIDER

@api_view(['DELETE'])
def delete_slider(request, id):

    try:
        slider = Slider.objects.get(id=id)
    except Slider.DoesNotExist:
        return Response({"error": "Slider not found"})

    slider.delete()

    return Response({
        "message": "Slider deleted"
    })