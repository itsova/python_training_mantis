# -*- coding: utf-8 -*-


def test_add_project(app):
    old_count = len(app.project.get_project())
    app.project.create()
    new_count = len(app.project.get_project())
    assert old_count + 1 == new_count