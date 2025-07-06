def test_create_user_2_letter_in_first_name_get_success_response():
    # 1. Crear cuerpo de la solicitud con nombre "Aa"
    user_body = get_user_body("Aa")

    # 2. Enviar la solicitud POST para crear usuario
    user_response = sender_stand_request.post_new_user(user_body)

    # 3. Comprobar código de respuesta 201
    assert user_response.status_code == 201

    # 4. Comprobar que el campo authToken está presente y no vacío
    assert user_response.json()["authToken"] != ""

    # 5. Verificar que el nuevo usuario esté en la tabla "users"
    users_list = sender_stand_request.get_users_table()  # suponiendo que tienes esta función
    new_user = {
        "firstName": "Aa",
        "phone": user_body["phone"],
        "address": user_body["address"]
    }

    # Comprobar que el nuevo usuario esté en la lista
    assert new_user in users_list