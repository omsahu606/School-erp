from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import AdmissionApplication


 
# CREATE ADMISSION
 

@api_view(['POST'])
def add_admission(request):

    admission = AdmissionApplication.objects.create(
        student_name=request.data.get("student_name"),
        dob=request.data.get("dob"),
        applying_class=request.data.get("applying_class"),
        parent_name=request.data.get("parent_name"),
        email=request.data.get("email"),
        phone=request.data.get("phone"),
        address=request.data.get("address")
    )

    return Response({
        "message": "Admission form submitted successfully",
        "id": admission.id
    })


 
# GET ALL ADMISSIONS
 

@api_view(['GET'])
def list_admissions(request):

    admissions = AdmissionApplication.objects.all().order_by("-created_at")

    data = []

    for a in admissions:
        data.append({
            "id": a.id,
            "student_name": a.student_name,
            "dob": a.dob,
            "applying_class": a.applying_class,
            "parent_name": a.parent_name,
            "email": a.email,
            "phone": a.phone,
            "address": a.address,
            "created_at": a.created_at
        })

    return Response(data)



 
# DELETE ADMISSION
 

@api_view(['DELETE'])
def delete_admission(request, id):

    try:
        admission = AdmissionApplication.objects.get(id=id)
    except AdmissionApplication.DoesNotExist:
        return Response({"error": "Admission not found"})

    admission.delete()

    return Response({
        "message": "Admission deleted successfully"
    })
    
# admission_status

@api_view(['PUT'])
def update_admission_status(request, id):

    try:
        admission = AdmissionApplication.objects.get(id=id)
    except AdmissionApplication.DoesNotExist:
        return Response({"error": "Admission not found"})

    status = request.data.get("status")

    if status not in ["accepted", "rejected"]:
        return Response({"error": "Invalid status"})

    admission.status = status
    admission.save()

    return Response({
        "message": f"Admission {status} successfully",
        "status": admission.status
    })