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

resource "docker_network" "proj_network" {
  name = "proj_network"
}

# Pulls the image
resource "docker_image" "flask_app_image" {
  name = "trivia_flask_app:latest"
}

# Create a container
resource "docker_container" "flask_app" {
  image = docker_image.flask_app_image.image_id
  name  = "trivia_app"
  
networks_advanced {
    name = docker_network.proj_network.name
  }

  ports {
    internal = "59000"
    external = "59000"
  }
}

# Pulls the image
resource "docker_image" "server_image" {
  name = "trivia_server:latest"
}

# Create a container
resource "docker_container" "trivia_server" {
  image = docker_image.server_image.image_id
  name  = "trivia_server"
  
  networks_advanced {
    name = docker_network.proj_network.name
  }

    ports {
      internal = "8000"
      external = "8000"
  }
}
