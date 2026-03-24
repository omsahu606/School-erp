from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import GalleryCategory, Album, AlbumImage


# CATEGORY CRUD

@api_view(['GET', 'POST'])
def gallery_categories(request):

    # CREATE CATEGORY
    if request.method == 'POST':

        name = request.data.get('name')

        if not name:
            return Response({"error": "Name required"}, status=400)

        if GalleryCategory.objects.filter(name=name).exists():
            return Response({"error": "Category already exists"}, status=400)

        category = GalleryCategory.objects.create(name=name)

        return Response({
            "message": "Category created",
            "id": category.id,
            "name": category.name
        })

    # LIST CATEGORIES
    categories = GalleryCategory.objects.all()

    data = []

    for c in categories:
        data.append({
            "id": c.id,
            "name": c.name
        })

    return Response(data)

# UPDATE CATEGORY
@api_view(['PUT'])
def update_category(request, id):

    try:
        category = GalleryCategory.objects.get(id=id)
    except GalleryCategory.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    category.name = request.data.get('name', category.name)

    category.save()

    return Response({"message": "Category updated"})

# DELETE CATEGORY
@api_view(['DELETE'])
def delete_category(request, id):

    try:
        category = GalleryCategory.objects.get(id=id)
    except GalleryCategory.DoesNotExist:
        return Response({"error": "Not found"}, status=404)

    category.delete()

    return Response({"message": "Category deleted"})


# ALBUM CRUD

@api_view(['GET', 'POST'])
def albums(request):

    # CREATE ALBUM
    if request.method == 'POST':

        title = request.data.get('title')
        category_id = request.data.get('category_id')
        cover_image = request.FILES.get('cover_image')

        if not title or not category_id:
            return Response({"error": "title & category_id required"}, status=400)

        try:
            category = GalleryCategory.objects.get(id=category_id)
        except GalleryCategory.DoesNotExist:
            return Response({"error": "Category not found"}, status=404)

        album = Album.objects.create(
            title=title,
            category=category,
            cover_image=cover_image
        )

        return Response({
            "message": "Album created",
            "id": album.id
        })

    # LIST ALBUMS
    albums = Album.objects.all()

    data = []

    for a in albums:

        data.append({
            "id": a.id,
            "title": a.title,
            "category": a.category.name,
            "category_id": a.category.id,
            "cover_image": a.cover_image.url if a.cover_image else None
        })

    return Response(data)

# UPDATE ALBUM
@api_view(['PUT'])
def update_album(request, id):

    try:
        album = Album.objects.get(id=id)
    except Album.DoesNotExist:
        return Response({"error": "Album not found"}, status=404)

    album.title = request.data.get('title', album.title)

    new_cover = request.FILES.get('cover_image')

    if new_cover:
        album.cover_image = new_cover

    album.save()

    return Response({"message": "Album updated"})

# DELETE ALBUM
@api_view(['DELETE'])
def delete_album(request, id):

    try:
        album = Album.objects.get(id=id)
    except Album.DoesNotExist:
        return Response({"error": "Album not found"}, status=404)

    album.delete()

    return Response({"message": "Album deleted"})


# ALBUM IMAGES CRUD

# CREATE IMAGE
@api_view(['POST'])
def create_album_image(request):

    album_id = request.data.get('album_id')
    image = request.FILES.get('image')

    if not album_id or not image:
        return Response({"error": "album_id & image required"}, status=400)

    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        return Response({"error": "Album not found"}, status=404)

    album_image = AlbumImage.objects.create(
        album=album,
        image=image
    )

    return Response({
        "message": "Image uploaded",
        "id": album_image.id,
        "image": album_image.image.url
    })

# LIST IMAGES OF ALBUM
@api_view(['GET'])
def album_images(request, album_id):

    images = AlbumImage.objects.filter(album_id=album_id)

    data = []

    for img in images:

        data.append({
            "id": img.id,
            "image": img.image.url
        })

    return Response(data)

# UPDATE IMAGE
@api_view(['PUT'])
def update_album_image(request, id):

    try:
        album_image = AlbumImage.objects.get(id=id)
    except AlbumImage.DoesNotExist:
        return Response({"error": "Image not found"}, status=404)

    new_image = request.FILES.get('image')

    if new_image:
        album_image.image = new_image

    album_image.save()

    return Response({
        "message": "Image updated",
        "image": album_image.image.url
    })

# DELETE IMAGE
@api_view(['DELETE'])
def delete_album_image(request, id):

    try:
        image = AlbumImage.objects.get(id=id)
    except AlbumImage.DoesNotExist:
        return Response({"error": "Image not found"}, status=404)

    image.delete()

    return Response({"message": "Image deleted"})