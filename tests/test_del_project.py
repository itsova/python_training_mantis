# -*- coding: utf-8 -*-


def test_delete_project(app):
    if len(app.project.get_project()) == 2:
        app.project.create()
    old_count = len(app.project.get_project())
    name = app.project.get_project_name()
    app.project.delete_project(name)
    new_count = len(app.project.get_project())
    assert old_count - 1 == new_count
