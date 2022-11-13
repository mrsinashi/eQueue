from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

@login_required
#@group_required('Оператор электронной очереди')
def equeues(request):
    return JsonResponse({"ok": "ok"})