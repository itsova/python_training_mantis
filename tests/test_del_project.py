# -*- coding: utf-8 -*-


def test_delete_project(app):
    app.session.login("administrator", "root")
    if len(app.soap.project_lists("administrator", "root")) == 0:
        app.project.create()
    old_count = len(app.soap.project_lists("administrator", "root"))
    name = app.project.get_project_name()
    app.project.delete_project(name)
    new_count = len(app.soap.project_lists("administrator", "root"))
    assert old_count - 1 == new_count
