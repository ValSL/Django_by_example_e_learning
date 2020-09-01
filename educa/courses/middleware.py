from django.urls import reverse
from django.shortcuts import get_object_or_404, redirect
from .models import Course


def subdomain_courses_middleware(get_response):
    def middleware(request):
        host_parts = request.get_host().split(".")

        if len(host_parts) > 2 and host_parts[0] != "www":
            course = get_object_or_404(Course, slug=host_parts[0])
            course_url = reverse("course_detail", args=[course.slug])
            return redirect(course_url)

        response = get_response(request)
        return response

    return middleware
