# -*- coding: utf-8 -*-


def test_add_project(app):
    app.session.login("administrator", "root")
    old_count = len(app.soap.project_lists("administrator", "root"))
    app.project.create()
    new_count = len(app.soap.project_lists("administrator", "root"))
    assert old_count + 1 == new_count