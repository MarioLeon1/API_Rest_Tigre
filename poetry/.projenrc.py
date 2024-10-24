from projen.python import PythonProject

project = PythonProject(
    author_email="user@domain.com",
    author_name="user",
    module_name="API_Rest_Tigre",
    name="API_Rest_Tigre",
    version="0.1.0",
)

project.synth()