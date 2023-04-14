from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from sqlalchemy import create_engine, text

def initial_view(request):
    return render(request, 'base.html', {'data': [1,2,3,4,5]})

def applications_view(request):
    return render(request, 'applications.html', {'data': [1,2,3,4,5]})

# lets start with workers first
def workers_view(request):
    from .models import Roles, Positions
    engine = create_engine('postgresql+psycopg2://postgres:root@localhost:5432/application_processing')
    con = engine.connect()
    q_request ="""
    select workers.id, workers.fio, positions.name as position_name, roles.name as role_name
    from application_processing_workers as workers
    inner join
    application_processing_roles as roles
    on workers.role_id = roles.id
    inner join
    application_processing_positions as positions
    on workers.position_id = positions.id
    """
    all_workers = con.execute(text(q_request))
    roles = Roles.objects.all().values()
    positions = Positions.objects.all().values()

    return render(request, 'workers.html', {'all_workers': all_workers, 'roles':roles, 'positions': positions})

def clients_view(request):
    from .models import Clients

    all_clients = Clients.objects.all().values()

    return render(request, 'clients.html', {'all_clients': all_clients})

def equipment_view(request):
    from .models import Equipment_types
    engine = create_engine('postgresql+psycopg2://postgres:root@localhost:5432/application_processing')
    con = engine.connect()
    q_request ="""
    select equipment.id, equipment.name, equipment.inv_number, equipment_types.name as type
    from application_processing_equipment as equipment
    inner join
    application_processing_equipment_types as equipment_types
    on equipment.type_id = equipment_types.id
    """
    all_equipment = con.execute(text(q_request))
    types = Equipment_types.objects.all().values()
    return render(request, 'equipment.html', {'all_equipment':all_equipment, 'types': types})
    
def reports_view(request):
    return render(request, 'reports.html', {'data': [1,2,3,4,5]})

@csrf_exempt
def save_application(request):
    import json

    request_body= json.loads(request.body)
    print(request_body)

    test_data = [
    {
        "id": "1",
        "theme": "test",
        "client": "test",
        "worker": "test",
        "status": "test",
        "manage": "test",
    },
    {
        "id": "2",
        "theme": "test",
        "client": "test",
        "worker": "test",
        "status": "test",
        "manage": "test",
    },
    {
        "id": "3",
        "theme": "test",
        "client": "test",
        "worker": "test",
        "status": "test",
        "manage": "test",
    },
    {
        "id": "4",
        "theme": "test",
        "client": "test",
        "worker": "test",
        "status": "test",
        "manage": "test",
    },
    ]

    return render(request, 'applications.html', {'data': test_data})

@csrf_exempt
def get_application(request):
    application_id = json.loads(request.body).get('application_id')

    if (application_id):
        # получаем с бд по id заявку в формате объекта
        application = None
        # передаем в render data
        return render(request, 'application_view.html', {'data': application})
    else:
        # если не получили id или с ошибкой, то вывести на вебсокетах toast с ошибкой
        return False

@csrf_exempt
def add_position(request):
    from .models import Positions
    
    try:
        name = json.loads(request.body).get('name')
        if (name):
            Positions.objects.create(name=name)
            return JsonResponse({'status':'ok', 'description': 'saving succes'})
        raise Exception
    except Exception as e:
        return JsonResponse({'status':'error', 'description': 'saving failed', 'error': e})

@csrf_exempt
def add_role(request):
    from .models import Roles
    
    try:
        name = json.loads(request.body).get('name')
        if (name):
            Roles.objects.create(name=name)
            return JsonResponse({'status':'ok', 'description': 'saving succes'})
        raise Exception
    except Exception as e:
        return JsonResponse({'status':'error', 'description': 'saving failed', 'error': e})

@csrf_exempt
def add_priority(request):
    from .models import Priority
    
    try:
        name = json.loads(request.body).get('name')
        if (name):
            Priority.objects.create(name=name)
            return JsonResponse({'status':'ok', 'description': 'saving succes'})
        raise Exception
    except Exception as e:
        return JsonResponse({'status':'error', 'description': 'saving failed', 'error': e})

@csrf_exempt
def add_status(request):
    from .models import Statuses
    
    try:
        name = json.loads(request.body).get('name')
        if (name):
            Statuses.objects.create(name=name)
            return JsonResponse({'status':'ok', 'description': 'saving succes'})
        raise Exception
    except Exception as e:
        return JsonResponse({'status':'error', 'description': 'saving failed', 'error': e})

@csrf_exempt
def add_service_object(request):
    from .models import Service_objects
    
    try:
        name = json.loads(request.body).get('name')
        if (name):
            Service_objects.objects.create(name=name)
            return JsonResponse({'status':'ok', 'description': 'saving succes'})
        raise Exception
    except Exception as e:
        return JsonResponse({'status':'error', 'description': 'saving failed', 'error': e})

@csrf_exempt
def add_equipment_type(request):
    from .models import Equipment_types
    
    try:
        name = json.loads(request.body).get('name')
        if (name):
            Equipment_types.objects.create(name=name)
            return JsonResponse({'status':'ok', 'description': 'saving succes'})
        raise Exception
    except Exception as e:
        return JsonResponse({'status':'error', 'description': 'saving failed', 'error': e})

@csrf_exempt
def add_worker(request):
    from .models import Workers
    
    try:
        fio = json.loads(request.body).get('fio')
        position = json.loads(request.body).get('position')
        role = json.loads(request.body).get('role')
        if (fio and position and role):
            last_id = Workers.objects.last().id + 1
            Workers.objects.create(id=last_id, fio=fio, position_id=position, role_id=role)
            return JsonResponse({'status':'ok', 'description': 'saving succes'})
        raise Exception
    except Exception as e:
        return JsonResponse({'status':'error', 'description': 'saving failed', 'error': e})

@csrf_exempt
def delete_worker(request):
    from .models import Workers
    
    try:
        id = json.loads(request.body).get('id')
        Workers.objects.filter(id=id).delete()
        return JsonResponse({'status':'ok', 'description': 'delete succes'})
    except Exception as e:
        return JsonResponse({'status':'error', 'description': 'deleting failed', 'error': e})

@csrf_exempt
def add_equipment(request):
    from .models import Equipment
    
    try:
        name = json.loads(request.body).get('name')
        inv_number = json.loads(request.body).get('inv_number')
        type = json.loads(request.body).get('type')
        last_id = Equipment.objects.last().id + 1
        if (name and type and inv_number):
            Equipment.objects.create(id=last_id, name=name, type_id=type, inv_number=inv_number)
            return JsonResponse({'status':'ok', 'description': 'saving succes'})
        raise Exception
    except Exception as e:
        return JsonResponse({'status':'error', 'description': 'saving failed', 'error': e})

@csrf_exempt
def delete_equipment(request):
    from .models import Equipment
    
    try:
        id = json.loads(request.body).get('id')
        Equipment.objects.filter(id=id).delete()
        return JsonResponse({'status':'ok', 'description': 'delete succes'})
    except Exception as e:
        return JsonResponse({'status':'error', 'description': 'deleting failed', 'error': e})

@csrf_exempt
def add_client(request):
    from .models import Clients
    
    try:
        is_company = json.loads(request.body).get('is_company')
        name = json.loads(request.body).get('name')
        telephone = json.loads(request.body).get('telephone')
        last_id = Clients.objects.last().id + 1
        if (is_company and name and telephone):
            Clients.objects.create(id=last_id, is_company=is_company, name=name, telephone=telephone)
            return JsonResponse({'status':'ok', 'description': 'saving succes'})
        elif (not is_company and name and telephone):
            Clients.objects.create(id=last_id, is_company=is_company, fio=name, telephone=telephone)
            return JsonResponse({'status':'ok', 'description': 'saving succes'})
        raise Exception
    except Exception as e:
        return JsonResponse({'status':'error', 'description': 'saving failed', 'error': e})

@csrf_exempt
def delete_client(request):
    from .models import Clients
    
    try:
        id = json.loads(request.body).get('id')
        Clients.objects.filter(id=id).delete()
        return JsonResponse({'status':'ok', 'description': 'delete succes'})
    except Exception as e:
        return JsonResponse({'status':'error', 'description': 'deleting failed', 'error': e})

@csrf_exempt
def add_application(request):
    from .models import Workers
    
    try:
        type = json.loads(request.body).get('type')
        priority = json.loads(request.body).get('priority')
        description = json.loads(request.body).get('description')
        files = json.loads(request.body).get('files')
        client = json.loads(request.body).get('client')
        service_obj = json.loads(request.body).get('service_obj')
        equipment = json.loads(request.body).get('equipment')
        worker = json.loads(request.body).get('worker')
        status = json.loads(request.body).get('status')
        if (type and priority and description and client and worker):
            Workers.objects.create(is_company=is_company, name=name, telephone=telephone, fio=fio)
            return JsonResponse({'status':'ok', 'description': 'saving succes'})
        raise Exception
    except Exception as e:
        return JsonResponse({'status':'error', 'description': 'saving failed', 'error': e})
# добавить ручку для сохранения заявки в бд
# добавить ручку для загрузки заявки из бд --> одной
# добавить ручку для загрузки заявки из бд --> всех сразу

# Важное!
# нарисовать структуру БД по скриншотам, чтобы уже полноценно работать