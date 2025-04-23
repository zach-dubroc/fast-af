import os
import platform
import subprocess
import shutil
from typing import Optional
from .utils import create_directory, create_files_in_directory, copy_and_create_template

#color codes
GREEN = "\033[92m"
RED = "\033[91m"
BLUE = "\033[94m"
BOLD = "\033[1m"
RESET = "\033[0m"

BASE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIRECTORY = os.path.join(BASE_DIRECTORY, "conf")

BASE_TEMPLATE_DIRECTORY = os.path.join(TEMPLATE_DIRECTORY, "base_template")
DATABASE_TEMPLATE_DIRECTORY = os.path.join(TEMPLATE_DIRECTORY, "database_template")
JOB_MANAGER_TEMPLATE_DIRECTORY = os.path.join(TEMPLATE_DIRECTORY, "job_manager_template")
ROOT_TEMPLATE_DIRECTORY = os.path.join(TEMPLATE_DIRECTORY, "root_template")
ROUTERS_TEMPLATE_DIRECTORY = os.path.join(TEMPLATE_DIRECTORY, "routers_template")
SCHEMAS_TEMPLATE_DIRECTORY = os.path.join(TEMPLATE_DIRECTORY, "schemas_template")
SERVICES_TEMPLATE_DIRECTORY = os.path.join(TEMPLATE_DIRECTORY, "services_template")
python_cmd = "python3" if platform.system() != "Windows" else "python"

def create_venv_cross_platform(root_directory: str) -> bool:
    """
    Create a virtual environment and install dependencies in a cross-platform manner.

    Args:
        root_directory (str): Path to the project root directory.

    Returns:
        bool: True if successful, False otherwise.
    """
    venv_path = os.path.join(root_directory, ".venv")
    try:
        if not os.path.exists(venv_path):
            print(f"{GREEN}{BOLD}✓ Creating virtual environment in {venv_path}{RESET}")
            subprocess.run([python_cmd, "-m", "venv", venv_path], check=True)
        if platform.system() == "Windows":
            python_venv = os.path.join(venv_path, "Scripts", "python.exe")
            pip_venv = os.path.join(venv_path, "Scripts", "pip.exe")
        else:
            python_venv = os.path.join(venv_path, "bin", "python")
            pip_venv = os.path.join(venv_path, "bin", "pip") 

        print(f"{BLUE}updating pip virtual environment{RESET}")
        subprocess.run([python_venv, "-m", "pip", "install", "--upgrade", "pip"], check=True)
        requirements_path = os.path.join(root_directory, "requirements.txt")
        if os.path.exists(requirements_path):
            print(f"{BLUE}installing dependencies from {requirements_path}{RESET}")
            # subprocess.run([pip_venv, "install", "-r", requirements_path], check=True)
            # for installing deps but leaving commented until formatting is further along
        else:
            print(f"{RED}requirements.txt not found in {root_directory}{RESET}")

        return True
    except subprocess.CalledProcessError as e:
        print(f"{RED}{BOLD}✗ Failed to set up virtual environment: {e}{RESET}")
        return False

def create_database_template(project_name: str, destination_directory: str):
    """
    Create a database template.

    Args:
        project_name (str): Name of the project.
        destination_directory (str): Path to the destination directory.
    """
    print(f"{BLUE}\nCreating database files{RESET}")
    database_destination_directory = os.path.join(destination_directory, "database")

    create_directory(database_destination_directory)

    copy_and_create_template(
        src_dir=DATABASE_TEMPLATE_DIRECTORY,
        project_name=project_name,
        destination_dir=database_destination_directory,
    )

def create_job_manager_template(project_name: str, destination_directory: str):
    """
    Create a job manager template.

    Args:
        project_name (str): Name of the project.
        destination_directory (str): Path to the destination directory.
    """
    print(f"{BLUE}\nCreating job manager{RESET}")
    job_manager_destination_directory = os.path.join(destination_directory, "job_manager")

    create_directory(job_manager_destination_directory)

    copy_and_create_template(
        src_dir=JOB_MANAGER_TEMPLATE_DIRECTORY,
        project_name=project_name,
        destination_dir=job_manager_destination_directory,
    )

def create_root_template(project_name: str, destination_directory: str):
    """
    Create a root template.

    Args:
        project_name (str): Name of the project.
        destination_directory (str): Path to the destination directory.
    """
    print(f"{BLUE}\nCreating root content{RESET}")
    root_destination_directory = os.path.join(destination_directory, "root")

    create_directory(root_destination_directory)

    copy_and_create_template(
        src_dir=ROOT_TEMPLATE_DIRECTORY,
        project_name=project_name,
        destination_dir=root_destination_directory,
    )

def create_routers_template(project_name: str, destination_directory: str):
    """
    Create a routers template.

    Args:
        project_name (str): Name of the project.
        destination_directory (str): Path to the destination directory.
    """
    print(f"{BLUE}\nCreating routers{RESET}")
    router_destination_directory = os.path.join(destination_directory, "routers")

    create_directory(router_destination_directory)

    copy_and_create_template(
        src_dir=ROUTERS_TEMPLATE_DIRECTORY,
        project_name=project_name,
        destination_dir=router_destination_directory,
    )

def create_schemas_template(project_name: str, destination_directory: str):
    """
    Create a schemas template.

    Args:
        project_name (str): Name of the project.
        destination_directory (str): Path to the destination directory.
    """
    print(f"{BLUE}\nCreating schemas{RESET}")
    schemas_destination_directory = os.path.join(destination_directory, "schemas")

    create_directory(schemas_destination_directory)

    copy_and_create_template(
        src_dir=SCHEMAS_TEMPLATE_DIRECTORY,
        project_name=project_name,
        destination_dir=schemas_destination_directory,
    )

def create_services_template(project_name: str, destination_directory: str):
    """
    Create a services template.

    Args:
        project_name (str): Name of the project.
        destination_directory (str): Path to the destination directory.
    """
    print(f"{BLUE}\nCreating services{RESET}")
    services_destination_directory = os.path.join(destination_directory, "services")

    create_directory(services_destination_directory)

    copy_and_create_template(
        src_dir=SERVICES_TEMPLATE_DIRECTORY,
        project_name=project_name,
        destination_dir=services_destination_directory,
    )

def create_base_template(project_name: str, destination_directory: str):
    print(f"{BLUE}\nCreating base template{RESET}")
    copy_and_create_template(
        src_dir=BASE_TEMPLATE_DIRECTORY,
        project_name=project_name,
        destination_dir=destination_directory,
    )

def create_fast_template(
    project_name: str,
    root_directory: Optional[str] = None,
    create_venv: bool = True,
    template_type: str = "md"
):
    """
    Create a FastAPI template.
    Args:
        project_name (str): Name of the project.
        root_directory (str, optional): Path to the destination directory.
        create_venv (bool): Create a virtual environment and install dependencies.
        template_type (str): Type of template Handled differently depending on template type.
    """
    if root_directory is None:
        root_directory = os.path.join(os.getcwd(), project_name)

    if root_directory != ".":
        print(f"{GREEN}{BOLD}✓ Creating template in {root_directory}{RESET}")
        create_directory(root_directory)

    destination_directory = os.path.join(root_directory, project_name)
    create_directory(destination_directory)
    if template_type == "sm":
        print(f"{BLUE}Lightweight template (sm){RESET}")
        create_base_template(project_name, root_directory)
        create_database_template(project_name, destination_directory)
        create_job_manager_template(project_name, destination_directory)
        create_root_template(project_name, destination_directory)
        create_routers_template(project_name, destination_directory)
        create_schemas_template(project_name, destination_directory)
        create_services_template(project_name, destination_directory)
    elif template_type == "md":
        print(f"{BLUE}Standard template (md){RESET}")
        # create_base_template(project_name, root_directory)
        # create_database_template(project_name, destination_directory)
        # create_job_manager_template(project_name, destination_directory)
        # create_root_template(project_name, destination_directory)
        # create_routers_template(project_name, destination_directory)
        # create_schemas_template(project_name, destination_directory)
        # create_services_template(project_name, destination_directory)
    elif template_type == "lg":
        print(f"{BLUE}Full template with React frontend (lg){RESET}")
        # create_base_template(project_name, root_directory)
        # create_database_template(project_name, destination_directory)
        # create_job_manager_template(project_name, destination_directory)
        # create_root_template(project_name, destination_directory)
        # create_routers_template(project_name, destination_directory)
        # create_schemas_template(project_name, destination_directory)
        # create_services_template(project_name, destination_directory)
        # sm template should just give base api with easily customizable crud routes, db has to be setup seperately
        # md should spin up database as well 
        # lg will spin up db and generate boilerplate react frontend with basic crud functionality
    if create_venv:
        print(f"{BLUE}{BOLD}Setting up virtual environment{RESET}")
        if create_venv_cross_platform(root_directory):
            print(f"{GREEN}{BOLD}✓ virtual environment created\n✓ dependencies installed successfully{RESET}")
            border = f"{BLUE}{BOLD}{'=' * 50}{RESET}"
            print(border)
            print(f"{BLUE}{BOLD}To activate the virtual environment:{RESET}")
            if platform.system() == "Windows":
                print(f"{BLUE}in the project root\ndepending on which terminal you use, run:{RESET}")
                print(f"- {GREEN}.venv\\Scripts\\activate.bat{RESET}  # for command prompt")
                print(f"- {GREEN}.venv/scripts/activate{RESET}  # for powershell")
                print(f"- {GREEN}source .venv/scripts/activate{RESET}  # for bash")
            else:
                print(f"{GREEN}cd {root_directory}{RESET}")
                print(f"{GREEN}source .venv/bin/activate{RESET}  # for bash")
            print(border)
        else:
            border = f"{BLUE}{BOLD}{'=' * 50}{RESET}"
            print(border)
            print(f"{RED}{BOLD}✗ WHAT WE HAVE HERE IS A FAILURE TO COMMUNICATE. set it up manually:{RESET}")
            print(f"{BLUE}get to the root directory:{RESET}")
            print(f"{GREEN}cd {root_directory}{RESET}")
            print(f"{BLUE}create the virtual environment:{RESET}")
            print(f"{GREEN}{python_cmd} -m venv .venv{RESET}")
            print(f"{BLUE}{BOLD}then activate it with:{RESET}")
            if platform.system() == "Windows":
                print(f"{GREEN}.venv/scripts/activate{RESET}  # for powershell")
                print(f"{GREEN}.venv\\Scripts\\activate.bat{RESET}  # for command prompt")
                print(f"{GREEN}source .venv/bin/activate{RESET}  # for bash/zsh")
            else:
                print(f"{GREEN}source .venv/bin/activate{RESET}  # for bash/zsh")
            print(border)
            print(f"{BLUE}then install dependencies:{RESET}")
            print(f"{GREEN}pip install -r requirements.txt{RESET}")
    else:
        try:
            with open(os.path.join(root_directory, "requirements.txt"), "w") as f:
                subprocess.run(["pip", "freeze"], stdout=f, check=True)
                print(f"{GREEN}{BOLD}✓ Dependencies installed successfully{RESET}")
        except subprocess.CalledProcessError as e:
            print(f"{RED}{BOLD}✗ FAILURE: {e}{RESET}")

if __name__ == "__main__":
    create_fast_template(
        root_directory="/Users/akandepeter/DevProjects/Backend/cloned/test2",
        project_name="test2",
    )
