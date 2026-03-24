from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import Staff, StaffRole, StaffAttendance, StaffLeave


     
# ROLE CRUD
     

@api_view(['POST'])
def add_role(request):
    name = request.data.get("name")

    if not name:
        return Response({"error": "Role name required"})

    role = StaffRole.objects.create(name=name)

    return Response({"message": "Role added", "id": role.id})


@api_view(['GET'])
def list_roles(request):
    roles = StaffRole.objects.all()
    data = [{"id": r.id, "name": r.name} for r in roles]
    return Response(data)


@api_view(['PUT'])
def update_role(request, id):
    try:
        role = StaffRole.objects.get(id=id)
    except StaffRole.DoesNotExist:
        return Response({"error": "Role not found"})

    role.name = request.data.get("name", role.name)
    role.save()

    return Response({"message": "Role updated"})


@api_view(['DELETE'])
def delete_role(request, id):
    try:
        role = StaffRole.objects.get(id=id)
    except StaffRole.DoesNotExist:
        return Response({"error": "Role not found"})

    role.delete()
    return Response({"message": "Role deleted"})


     
# STAFF CRUD


@api_view(['POST'])
def add_staff(request):
    staff = Staff.objects.create(
        name=request.data.get("name"),
        email=request.data.get("email"),
        phone=request.data.get("phone"),
        role_id=request.data.get("role_id"),
        salary=request.data.get("salary"),
        joining_date=request.data.get("joining_date"),
        photo=request.FILES.get("photo")
    )

    return Response({"message": "Staff added", "id": staff.id})


@api_view(['GET'])
def list_staff(request):
    staff = Staff.objects.all()

    data = []
    for s in staff:
        data.append({
            "id": s.id,
            "name": s.name,
            "email": s.email,
            "phone": s.phone,
            "role": s.role.name if s.role else None,
            "salary": s.salary,
            "joining_date": s.joining_date,
            "photo": s.photo.url if s.photo else None,
            "is_active": s.is_active
        })

    return Response(data)


@api_view(['GET'])
def get_staff(request, id):
    try:
        s = Staff.objects.get(id=id)
    except Staff.DoesNotExist:
        return Response({"error": "Staff not found"})

    return Response({
        "id": s.id,
        "name": s.name,
        "email": s.email,
        "phone": s.phone,
        "role": s.role.name if s.role else None,
        "salary": s.salary,
        "joining_date": s.joining_date,
        "photo": s.photo.url if s.photo else None,
        "is_active": s.is_active
    })


@api_view(['PUT'])
def update_staff(request, id):
    try:
        staff = Staff.objects.get(id=id)
    except Staff.DoesNotExist:
        return Response({"error": "Staff not found"})

    staff.name = request.data.get("name", staff.name)
    staff.email = request.data.get("email", staff.email)
    staff.phone = request.data.get("phone", staff.phone)
    staff.role_id = request.data.get("role_id", staff.role_id)
    staff.salary = request.data.get("salary", staff.salary)
    staff.joining_date = request.data.get("joining_date", staff.joining_date)

    if request.FILES.get("photo"):
        staff.photo = request.FILES.get("photo")

    staff.save()

    return Response({"message": "Staff updated"})


@api_view(['DELETE'])
def delete_staff(request, id):
    try:
        staff = Staff.objects.get(id=id)
    except Staff.DoesNotExist:
        return Response({"error": "Staff not found"})

    staff.delete()
    return Response({"message": "Staff deleted"})


@api_view(['PUT'])
def toggle_staff_status(request, id):
    try:
        staff = Staff.objects.get(id=id)
    except Staff.DoesNotExist:
        return Response({"error": "Staff not found"})

    staff.is_active = not staff.is_active
    staff.save()

    return Response({
        "message": "Status updated",
        "is_active": staff.is_active
    })


     
# ATTENDANCE
     

@api_view(['POST'])
def mark_attendance(request):

    staff_id = request.data.get("staff_id")
    date = request.data.get("date")
    status = request.data.get("status")

    obj, created = StaffAttendance.objects.update_or_create(
        staff_id=staff_id,
        date=date,
        defaults={"status": status}
    )

    return Response({
        "message": "Attendance marked",
        "created": created
    })


@api_view(['GET'])
def list_attendance(request):

    attendance = StaffAttendance.objects.select_related('staff')

    data = []
    for a in attendance:
        data.append({
            "staff": a.staff.name,
            "date": a.date,
            "status": a.status,
            "remark": a.remark
        })

    return Response(data)


@api_view(['GET'])
def staff_attendance(request, staff_id):

    attendance = StaffAttendance.objects.filter(staff_id=staff_id)

    data = []
    for a in attendance:
        data.append({
            "date": a.date,
            "status": a.status
        })

    return Response(data)


     
# LEAVE SYSTEM
     

@api_view(['POST'])
def apply_leave(request):

    leave = StaffLeave.objects.create(
        staff_id=request.data.get("staff_id"),
        from_date=request.data.get("from_date"),
        to_date=request.data.get("to_date"),
        reason=request.data.get("reason")
    )

    return Response({
        "message": "Leave applied",
        "id": leave.id
    })


@api_view(['GET'])
def list_leaves(request):

    leaves = StaffLeave.objects.select_related('staff')

    data = []
    for l in leaves:
        data.append({
            "id": l.id,
            "staff": l.staff.name,
            "from": l.from_date,
            "to": l.to_date,
            "status": l.status,
            "reason": l.reason
        })

    return Response(data)


@api_view(['PUT'])
def update_leave_status(request, id):

    try:
        leave = StaffLeave.objects.get(id=id)
    except StaffLeave.DoesNotExist:
        return Response({"error": "Leave not found"})

    leave.status = request.data.get("status")  # approved / rejected
    leave.save()

    return Response({"message": "Leave status updated"})