# -*- coding: utf-8 -*-
from model.project import Project
import random

def test_delete_some_project(app, db):
    if len(db.get_project_list()) == 0:
        app.project.create(Project(project_name=app.project.random_name(10),
                               view_status="public",
                               status="release",
                               description="Some text about project"))
    old_projects = db.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project_by_id(project)
    new_projects = db.get_project_list()
    old_projects.remove(project)
    assert old_projects == new_projects

def test_delete_first_project(app, db):
    """
    Метод удаляет первый проект (первый проект из таблицы mantis_project_table)
    """
    if len(db.get_project_list()) == 0:
        app.project.create(Project(project_name=app.project.random_name(10),
                               view_status="private",
                               status="obsolete",
                               description="Some text about project"))
    old_projects = db.get_project_list()
    app.project.delete_project(old_projects[0])
    new_projects = db.get_project_list()
    old_projects.remove(old_projects[0])
    assert old_projects == new_projects

