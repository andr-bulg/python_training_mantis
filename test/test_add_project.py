# -*- coding: utf-8 -*-
from model.project import Project

def test_add_project(app, db):
    old_projects = db.get_project_list()
    some_project = Project(project_name=app.project.random_name(10),
                               view_status="public",
                               status="development",
                               description="Some text about project")
    app.project.create(some_project)
    new_projects = db.get_project_list()
    old_projects.append(some_project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

def test_add_project_check_by_soap(app):
    old_projects = app.soap.get_project_list_soap("administrator", "root")
    some_project = Project(project_name=app.project.random_name(10),
                            view_status="public",
                            status="development",
                            description="Some text about project")
    app.project.create(some_project)
    new_projects = app.soap.get_project_list_soap("administrator", "root")
    old_projects.append(some_project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

