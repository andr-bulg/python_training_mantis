"""
Создаём класс Project, в котором через инициализатор будут задаваться свойства
создаваемых объектов, чтобы затем в качестве параметров в другие методы
достаточно было передать ссылку на объект класса (параметр self).
"""
from sys import maxsize

class Project:

    def __init__(self, project_name=None, status=None, view_status=None, description=None,
                 id_project=None):
        self.project_name = project_name
        self.status = status
        self.view_status = view_status
        self.description = description
        self.id_project = id_project

    def __repr__(self):
        return f"{self.id_project}:{self.project_name}"

    def id_or_max(self):
        if self.id_project:
            return int(self.id_project)
        else:
            return maxsize

    def __eq__(self, other):
        return (self.id_project is None or other.id_project is None or self.id_project == other.id_project) \
            and self.project_name == other.project_name

