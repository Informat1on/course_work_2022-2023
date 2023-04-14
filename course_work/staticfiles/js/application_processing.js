function saveApplicationToDb() {
    const application_type = $('#application-select option[selected]').text();
    const priority = $('#priority option[selected]').text();
    const description = '';
    const client = $('#client option[selected]').text();
    const service_obj = $('#service-obj option[selected]').text();
    const hardware = $('#hardware option[selected]').text();
    const worker = $('#worker option[selected]').text();

    const data_to_send = {
        "application_type":application_type,
        "priority":priority,
        "description":description,
        "client":client,
        "service_obj":service_obj,
        "hardware":hardware,
        "worker":worker,
    };
    // $.ajax({
    //     url: '/save_application',         /* Куда отправить запрос */
    //     method: 'post',             /* Метод запроса (post или get) */
    //     dataType: 'json',          /* Тип данных в ответе (xml, json, script, html). */
    //     data: JSON.stringify(data_to_send),     /* Данные передаваемые в массиве */
    //     success: function(data){   /* функция которая будет выполнена после успешного запроса.  */
    //         // $(`#container-${pageName}`).html(data);
    //         console.log(data);
    //         // alert(data); /* В переменной data содержится ответ от index.php. */
    //     }
    // });
    $.post('/save_application', JSON.stringify(data_to_send), function(data){
        // возвращается html который отрисовывается
        $('#container-applications').html(data);
    });
}

function getApplicationFromDb(application_id) {
    $.post('/get_application', JSON.stringify({application_id}), function(data){
        // открываем модальное окно с заполнением как полноценная страница html

    });
    
}

// Workers logic

// сброс меню выбора роли и должности при добавлении нового сотрудника
function resetSelects() {
    $('#input-fio').val('');
    $("#role-select option:first").prop("selected", "selected");
    $("#position-select option:first").prop("selected", "selected");
}

// сохранение работника в бд
function saveWorkerToDb() {
    const fio = $('#input-fio').val();
    const selected_role = $("#role-select option:selected").val();
    const selected_position = $("#position-select option:selected").val();
    
    const data_to_send = {
        'fio':fio,
        'position': selected_position,
        'role': selected_role
    };

    $.ajax({
        url: 'api/add_worker',         /* Куда отправить запрос */
        method: 'post',             /* Метод запроса (post или get) */
        dataType: 'json',          /* Тип данных в ответе (xml, json, script, html). */
        data: JSON.stringify(data_to_send),     /* Данные передаваемые в массиве */
        success: function(data){   /* функция которая будет выполнена после успешного запроса.  */
        // отрисовываю сразу после добавления    
        $.get('/workers', function(data){
                // возвращается html который отрисовывается
                $('#container-workers').html(data);
            });
        }
    });
}

//удаление работника
function deleteWorker(worker_id) {
    $.ajax({
        url: 'api/delete_worker',         /* Куда отправить запрос */
        method: 'post',             /* Метод запроса (post или get) */
        dataType: 'json',          /* Тип данных в ответе (xml, json, script, html). */
        data: JSON.stringify({'id':worker_id}),     /* Данные передаваемые в массиве */
        success: function(data){   /* функция которая будет выполнена после успешного запроса.  */
        // отрисовываю сразу после добавления    
        $.get('/workers', function(data){
                // возвращается html который отрисовывается
                $('#container-workers').html(data);
            });
        }
    });
}

// сохранение клиента в бд
function saveClientToDb() {
    const isCompany = $('#flexSwitchCheck').prop("checked");
    const name = $('#input-fio').val();
    const telephone = $('#input-telephone').val();
    
    const data_to_send = {
        'name':name,
        'is_company': isCompany,
        'telephone': telephone
    };

    $.ajax({
        url: 'api/add_client',         /* Куда отправить запрос */
        method: 'post',             /* Метод запроса (post или get) */
        dataType: 'json',          /* Тип данных в ответе (xml, json, script, html). */
        data: JSON.stringify(data_to_send),     /* Данные передаваемые в массиве */
        success: function(data){   /* функция которая будет выполнена после успешного запроса.  */
        // отрисовываю сразу после добавления    
        $.get('/clients', function(data){
                // возвращается html который отрисовывается
                $('#container-clients').html(data);
            });
        }
    });
}

//удаление клиента
function deleteClient(client_id) {
    $.ajax({
        url: 'api/delete_client',         /* Куда отправить запрос */
        method: 'post',             /* Метод запроса (post или get) */
        dataType: 'json',          /* Тип данных в ответе (xml, json, script, html). */
        data: JSON.stringify({'id':client_id}),     /* Данные передаваемые в массиве */
        success: function(data){   /* функция которая будет выполнена после успешного запроса.  */
        // отрисовываю сразу после добавления    
        $.get('/clients', function(data){
                // возвращается html который отрисовывается
                $('#container-clients').html(data);
            });
        }
    });
}

// сохранение оборудования в бд
function saveEquipmentToDb() {
    const name = $('#input-name').val();
    const inv = $('#input-inv').val();
    const type = $('#type-select :selected').val();
    
    const data_to_send = {
        'name':name,
        'inv_number': inv,
        'type': type
    };

    $.ajax({
        url: 'api/add_equipment',         /* Куда отправить запрос */
        method: 'post',             /* Метод запроса (post или get) */
        dataType: 'json',          /* Тип данных в ответе (xml, json, script, html). */
        data: JSON.stringify(data_to_send),     /* Данные передаваемые в массиве */
        success: function(data){   /* функция которая будет выполнена после успешного запроса.  */
        // отрисовываю сразу после добавления    
        $.get('/equipment', function(data){
                // возвращается html который отрисовывается
                $('#container-equipment').html(data);
            });
        }
    });
}

//удаление клиента
function deleteEquipment(equipment_id) {
    $.ajax({
        url: 'api/delete_equipment',         /* Куда отправить запрос */
        method: 'post',             /* Метод запроса (post или get) */
        dataType: 'json',          /* Тип данных в ответе (xml, json, script, html). */
        data: JSON.stringify({'id':equipment_id}),     /* Данные передаваемые в массиве */
        success: function(data){   /* функция которая будет выполнена после успешного запроса.  */
        // отрисовываю сразу после добавления    
        $.get('/equipment', function(data){
            // возвращается html который отрисовывается
            $('#container-equipment').html(data);
            });
        }
    });
}