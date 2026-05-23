from django.shortcuts import render
from django.db import transaction
from control_equipos.models import Equipo


def crud_test_dashboard(request):

    if request.GET.get("reset") == "1":
        Equipo.objects.filter(serial__startswith="TEST-").delete()

    result = {}

    with transaction.atomic():

        equipo = Equipo.objects.create(
            marca="TEST",
            tipo="COMPUTADOR",
            serial="TEST-001",
            estado="DISPONIBLE",
            fecha_solicitud="2026-01-01"
        )

        result["create_ok"] = True
        result["id"] = equipo.id

        total = Equipo.objects.count()
        result["read_ok"] = True
        result["total_read"] = total

        equipo.serial = f"UPDATED-{equipo.id}"
        equipo.save()

        result["update_ok"] = True
        result["serial"] = equipo.serial

        equipo.delete()

        result["delete_ok"] = True
        result["after_delete"] = Equipo.objects.count()

        transaction.set_rollback(True)

    result["status"] = "ok"

    return render(
        request,
        "control_equipos/crud_test_dashboard.html",
        result
    )