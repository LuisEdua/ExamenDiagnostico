from flask import Flask
from flask_cors import CORS
from src.Gestion.Infrestructure.Routes.TutorsRoutes import tutors_routes
from src.Gestion.Infrestructure.Routes.StudentsRoutes import students_routes
from src.Gestion.Infrestructure.Routes.SubjectsRoutes import subjects_routes
from src.Gestion.Infrestructure.Routes.StudentsSubjectsRoutes import students_subjects_routes

app = Flask(__name__)
app.register_blueprint(tutors_routes, url_prefix='/tutors')
app.register_blueprint(students_routes, url_prefix='/students')
app.register_blueprint(subjects_routes, url_prefix='/subjects')
app.register_blueprint(students_subjects_routes, url_prefix='/students_subjects')
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
