import sender_stand_request
import data
import copy

def get_kit_body(name):
    new_body = copy.deepcopy(data.kit_body)
    new_body["name"] = name
    return new_body

def positive_assert(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    auth_token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert response.status_code == 400

def test_kit_name_1_character():
    positive_assert(get_kit_body("a"))

def test_kit_name_511_characters():
    name = "Abcd" * 127 + "C"
    positive_assert(get_kit_body(name))

def test_kit_name_0_characters():
    negative_assert_code_400(get_kit_body(""))

def test_kit_name_512_characters():
    name = "Abcd" * 128 + "D"
    negative_assert_code_400(get_kit_body(name))

def test_kit_name_special_chars():
    positive_assert(get_kit_body("№%@,."))

def test_kit_name_with_spaces():
    positive_assert(get_kit_body(" A Aaa "))

def test_kit_name_with_numbers():
    positive_assert(get_kit_body("123"))

def test_kit_name_missing_param():
    invalid_body = copy.deepcopy(data.kit_body)
    invalid_body.pop("name")
    negative_assert_code_400(invalid_body)

def test_kit_name_number_type():
    invalid_body = copy.deepcopy(data.kit_body)
    invalid_body["name"] = 123
    negative_assert_code_400(invalid_body)
