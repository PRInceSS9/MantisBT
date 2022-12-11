from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    old_projects = app.project.get_projects_list()
    app.project.create(Project(name='77700888', status='в разработке', view_state='приватный',
                                    description='Project_description', inherit_global=True))
    new_projects = app.project.get_projects_list()
    assert len(old_projects) + 1 == len(new_projects)