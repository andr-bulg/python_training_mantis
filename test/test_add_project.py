# -*- coding: utf-8 -*-
from model.project import Project

def test_add_project(app, db):
    app.session.login("administrator", "root")
    old_projects = db.get_project_list()
    some_project = Project(project_name=app.project.random_name(10),
                               view_status="public",
                               status="release",
                               description="Some text about project")
    app.project.create(some_project)
    new_projects = db.get_project_list()
    old_projects.append(some_project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

