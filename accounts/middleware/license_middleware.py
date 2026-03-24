from django.shortcuts import redirect
from django.utils import timezone
from accounts.models import License

class LicenseMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        allowed_urls = [

            "/api/erp/activate-license/",
            "/api/admin/login/",
            "/activate-license/",

        ]

        # allow activation & login
        if request.path in allowed_urls:
            return self.get_response(request)

        # skip static & admin files
        if request.path.startswith("/static/") or request.path.startswith("/media/"):
            return self.get_response(request)

        license = License.objects.first()

        # license missing
        if not license:
            return redirect("/activate-license/")

        # license inactive
        if not license.is_active:
            return redirect("/activate-license/")

        # expiry check
        if license.expiry_date < timezone.now():
            return redirect("/activate-license/")

        return self.get_response(request)