import sender_stand_request
import data
def get_user_body(first_name):
    current_body:data.user_body.copy()
    current_body["first_name"] = first_name
    return current_body

def test_create_user_2_letter_in_first_name_get_success_response():
    # La versión actualizada del cuerpo de solicitud con el nombre "Aa" se guarda en la variable "user_body"
    user_body = get_user_body("Aa")
    # El resultado dela solicitud relevante se guarda en la variable "user_response"
    user_response = sender_stand_request.post_new_user(user_body)

    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert user_response.json()["authToken"] != ""

    def test_create_user_2_letter_in_first_name_get_success_response():
        # 1. Crear cuerpo de la solicitud con nombre "Aa"
        user_body = get_user_body("Aa")

        # 2. Enviar la solicitud POST para crear usuario
        user_response = sender_stand_request.post_new_user(user_body)

        # 3. Comprobar código de respuesta 201
        assert user_response.status_code == 201

        # 5. Verificar que el nuevo usuario esté en la tabla "users"
        users_list = sender_stand_request.get_users_table()  # suponiendo que tienes esta función
        new_user = {
            "firstName": "Aa",
            "phone": user_body["phone"],
            "address": user_body["address"]
        }

        # Comprobar que el nuevo usuario esté en la lista
        assert new_user in users_list