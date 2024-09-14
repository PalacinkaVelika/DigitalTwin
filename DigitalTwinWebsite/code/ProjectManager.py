import os
import shutil   

class ProjectManager:
    
    projects_root = os.path.join(os.path.dirname(__file__), 'projects')

    @staticmethod
    def create_new_project(name):
        """Create a new project and return the Project instance."""
        project = Project(name)
        return project
    
    @staticmethod
    def delete_project(name):
        """Delete the project directory and its contents."""
        project_path = os.path.join(ProjectManager.projects_root, name)
        if os.path.exists(project_path):
            shutil.rmtree(project_path)  # Deletes the directory and its contents
            return True
        else:
            raise FileNotFoundError(f"Project {name} not found")

    @staticmethod
    def edit_project_name(old_name, new_name):
        """Rename a project by changing the directory name."""
        old_path = os.path.join(ProjectManager.projects_root, old_name)
        new_path = os.path.join(ProjectManager.projects_root, new_name)
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            return Project(new_name)
        else:
            raise FileNotFoundError(f"Project {old_name} not found")

    @staticmethod
    def get_project_editor_data(name):
        """Return the save data for a given project."""
        project = Project(name)
        save_data_path = project.get_save_data_path()
        if os.path.exists(save_data_path):
            with open(save_data_path, 'r') as file:
                return file.read()
        else:
            raise FileNotFoundError(f"Save data for project {name} not found")


class Project:
    def __init__(self, name):
        self.name = name
        self.project_dir = os.path.join(os.path.dirname(__file__), 'projects', name)
        self.models_dir = os.path.join(self.project_dir, 'models')
        self.setup_project_directories()

    def setup_project_directories(self):
        """Create the project directory and models directory if they don't exist."""
        if not os.path.exists(self.project_dir):
            os.makedirs(self.project_dir)
        if not os.path.exists(self.models_dir):
            os.makedirs(self.models_dir)

    def get_save_data_path(self):
        """Return the path for the saveData.txt file."""
        return os.path.join(self.project_dir, 'saveData.txt')

    def get_model_path(self, model_name):
        """Return the path for a specific model file."""
        return os.path.join(self.models_dir, model_name)