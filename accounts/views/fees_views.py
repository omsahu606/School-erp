from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import SchoolClass, Term, FeeHeader, FeeStructure


# SCHOOL CLASS CRUD
@api_view(['POST'])
def create_class(request):
    name = request.data.get('name')
    obj = SchoolClass.objects.create(name=name)
    return Response({"message": "Class created", "id": obj.id})


@api_view(['GET'])
def list_classes(request):
    classes = SchoolClass.objects.all()
    data = [{"id": c.id, "name": c.name} for c in classes]
    return Response(data)


@api_view(['PUT'])
def update_class(request, id):
    obj = SchoolClass.objects.get(id=id)
    obj.name = request.data.get('name', obj.name)
    obj.save()
    return Response({"message": "Class updated"})


@api_view(['DELETE'])
def delete_class(request, id):
    obj = SchoolClass.objects.get(id=id)
    obj.delete()
    return Response({"message": "Class deleted"})


# TERM CRUD

@api_view(['POST'])
def create_term(request):

    name = request.data.get('name')

    obj = Term.objects.create(name=name)

    return Response({
        "message": "Term created",
        "id": obj.id
    })

@api_view(['GET'])
def list_terms(request):
    terms = Term.objects.all()
    data = [{"id": t.id, "name": t.name} for t in terms]
    return Response(data)


@api_view(['PUT'])
def update_term(request, id):
    obj = Term.objects.get(id=id)
    obj.name = request.data.get('name', obj.name)
    obj.save()
    return Response({"message": "Term updated"})


@api_view(['DELETE'])
def delete_term(request, id):
    obj = Term.objects.get(id=id)
    obj.delete()
    return Response({"message": "Term deleted"})



# FEE HEADER CRUD

@api_view(['POST'])
def create_fee_header(request):
    name = request.data.get('name')
    obj = FeeHeader.objects.create(name=name)
    return Response({"message": "Header created", "id": obj.id})


@api_view(['GET'])
def list_fee_headers(request):
    headers = FeeHeader.objects.all()
    data = [{"id": h.id, "name": h.name} for h in headers]
    return Response(data)


@api_view(['PUT'])
def update_fee_header(request, id):
    obj = FeeHeader.objects.get(id=id)
    obj.name = request.data.get('name', obj.name)
    obj.save()
    return Response({"message": "Header updated"})


@api_view(['DELETE'])
def delete_fee_header(request, id):
    obj = FeeHeader.objects.get(id=id)
    obj.delete()
    return Response({"message": "Header deleted"})


# FEE STRUCTURE (BULK CREATE / UPDATE)

@api_view(['POST'])
def create_fee_structure(request):

    class_id = request.data.get('class_id')
    term_id = request.data.get('term_id')
    fees = request.data.get('fees')

    school_class = SchoolClass.objects.get(id=class_id)
    term = Term.objects.get(id=term_id)

    for fee in fees:
        FeeStructure.objects.update_or_create(
            school_class=school_class,
            term=term,
            fee_header_id=fee['header_id'],
            defaults={'amount': fee['amount']}
        )

    return Response({"message": "Fee structure saved"})



# GET FEE STRUCTURE BY CLASS + TERM

@api_view(['GET'])
def get_fee_structure(request):

    class_id = request.GET.get('class_id')
    term_id = request.GET.get('term_id')

    data = FeeStructure.objects.filter(
        school_class_id=class_id,
        term_id=term_id
    )

    result = []

    total = 0

    for d in data:
        result.append({
            "header": d.fee_header.name,
            "amount": d.amount
        })
        total += float(d.amount)

    return Response({
        "class_id": class_id,
        "term_id": term_id,
        "fees": result,
        "total": total
    })