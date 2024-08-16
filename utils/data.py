class ApiResponses:
    USER_EXISTS = "User already exists"
    CREATE_USER_WITHOUT_PARAM = "Email, password and name are required fields"
    LOGIN_USER_INVALID_EMAIL_PASSWORD =  "email or password are incorrect"
    EDIT_FIELD_NO_AUTH = 'You should be authorised'
    CREATE_ORDER_NO_INGREDIENTS = 'Ingredient ids must be provided'
    INVALID_HASH = 'Internal Server Error'
    RECEIVE_ORDERS_NO_AUTH = 'You should be authorised'

class TestOrder:
    correct_ingredients = {"ingredients": ["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]}
    incorrect_ingredients = {"ingredients": ["60d3b41dfslk0026a733c6","609646e4dc916ejkdsh276b2870"]}
