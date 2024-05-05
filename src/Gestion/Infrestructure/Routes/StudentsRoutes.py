from flask import request, Blueprint

from src.Gestion.Infrestructure.Controllers.Students.Get import GetController
from src.Gestion.Infrestructure.Controllers.Students.ListByTutor import ListByTutorController
from src.Gestion.Infrestructure.Controllers.Students.Update import UpdateController
from src.Gestion.Infrestructure.Controllers.Tutors.Create import CreateController
from src.Gestion.Infrestructure.Repositories.MySQLRepositories.StudentsRepository import StudentsRepository

repo = StudentsRepository()
get_controller = GetController(repo)
list_by_tutor_controller = ListByTutorController(repo)
create_controller = CreateController(repo)
update_controller = UpdateController(repo)

students_routes = Blueprint('students_routes', __name__)


@students_routes.route('/', methods=['GET'])
def get_students():
    return get_controller.run()


@students_routes.route('/<string:tutor_uuid>', methods=['GET'])
def get_student(tutor_uuid):
    return list_by_tutor_controller.run(tutor_uuid)


@students_routes.route('/', methods=['POST'])
def create_student():
    return create_controller.run(request)


@students_routes.route('/', methods=['PUT'])
def update_student():
    return update_controller.run(request)
