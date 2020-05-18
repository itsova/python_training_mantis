
def test_signup_new_account(app):
    username = "user55"
    password = "test"
    app.james.ensure_user_exists(username, password)