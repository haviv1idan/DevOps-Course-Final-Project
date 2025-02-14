terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "3.0.2"
    }
  }
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

resource "docker_network" "test_network" {
  name = "test_network_999"
}

# Pulls the image
resource "docker_image" "flask-image" {
  name = "flask_app:latest"
}

# Create a container
resource "docker_container" "flask-app" {
  image = docker_image.flask-image.image_id
  name  = "flask-app"
  
networks_advanced {
    name = docker_network.test_network.name
  }

  ports {
    internal = "59000"
    external = "59000"
  }
}

# Pulls the image
resource "docker_image" "python-server-image" {
  name = "py_server:latest"
}

# Create a container
resource "docker_container" "python_server" {
  image = docker_image.python-server-image.image_id
  name  = "python_server"
  
  networks_advanced {
    name = docker_network.test_network.name
  }

    ports {
    internal = "8000"
    external = "8000"
  }
}