import docker
import time
import os

class StartContainer:

    def start_postgres_container(self, 
        container_name="my-postgres",
        postgres_password="mysecretpassword",
        port=5432,
        volume_name="pgdata"
    ):
        client = docker.from_env()

        # Check if container already exists and remove it (optional)
        try:
            container = client.containers.get(container_name)
            print(f"Container '{container_name}' already exists. Removing it...")
            container.stop()
            container.remove()
        except docker.errors.NotFound:
            pass  # Container doesn't exist yet

        # Create/start a new PostgreSQL container
        print("Starting new PostgreSQL container...")
        container = client.containers.run(
            "postgres",
            name=container_name,
            environment={"POSTGRES_PASSWORD": postgres_password},
            ports={'5432/tcp': port},
            volumes={volume_name: {'bind': '/var/lib/postgresql/data', 'mode': 'rw'}},
            detach=True,
        )

        # Wait for PostgreSQL to be ready (simple wait, can be improved)
        print("Waiting for PostgreSQL to initialize...")
        time.sleep(10)

        print(f"PostgreSQL container '{container_name}' is running.")
        return container
