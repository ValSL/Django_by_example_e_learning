from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required


@login_required
def course_chat_room(request, course_id):
    """
    Возвращает конкретный курс из списка курсов
    на которые подписан текущий пользователь
    """
    try:
        course = request.user.courses_joined.get(id=course_id)
    except:
        # любо курса нет, либо студент не подписан
        return HttpResponseForbidden()
    return render(request, 'chat/room.html', {'course': course})
