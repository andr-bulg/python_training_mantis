def test_login(app):
    app.session.logout()
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")

def test_login_soap(app):
    app.session.logout()
    app.session.login("user_GTqtKHTSRx", "test")
    assert app.soap.can_login("user_GTqtKHTSRx", "test8")

