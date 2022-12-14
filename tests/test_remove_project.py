from model.project import Project
import random


def test_add_project(app):
    if len(app.project.get_projects_list()) == 0:
        app.project.create(Project(name='Project_name901', status='в разработке', view_state='приватный',
                                   description='Project_description', inherit_global=True))
    # old_projects = app.project.get_projects_list()
    old_projects = app.soap.get_project_list()
    project = random.choice(old_projects)
    app.project.delete_project(project)
    # new_projects = app.project.get_projects_list()
    new_projects = app.soap.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)