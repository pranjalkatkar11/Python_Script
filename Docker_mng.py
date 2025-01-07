import docker

client = docker.from_env()
container = client.containers.run("nginx", detach=True, ports={'80/tcp': 8080})
print(f"Started container: {container.name}")

# Stop container
container.stop()