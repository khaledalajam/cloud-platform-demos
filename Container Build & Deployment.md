<img width="873" height="210" alt="image" src="https://github.com/user-attachments/assets/19ddd914-6642-422e-ae8d-62a4e2b8455d" />

<img width="1119" height="358" alt="image" src="https://github.com/user-attachments/assets/f7f40ad6-fde2-4546-ab8a-1758053c4703" />

I'm going to download some code and use the docker file to create a container image.

<img width="1112" height="505" alt="image" src="https://github.com/user-attachments/assets/07a5a821-4be6-47d2-9f3a-cd3c60b07bfa" />

To build the image, i'm going to do so by the docker commands. I'm going to give it a tag of primamaculaweb, and I need to pick the docker file in current directory.

<img width="633" height="143" alt="image" src="https://github.com/user-attachments/assets/0efab015-b600-4ac1-91f7-9052de6ec6df" />

We can see right there, we've got the primamaculaweb image that we just created. 


Now that we've got our docker image ready to go, we can get started and push this up to our GitHub Container Registry (GHCR).

<img width="811" height="252" alt="image" src="https://github.com/user-attachments/assets/856dbee4-2e9d-4ecd-858e-838b3262ee5e" />

The image has now been pushed to the container registry. 

<img width="811" height="153" alt="image" src="https://github.com/user-attachments/assets/35fe8b34-63c8-4dd0-8869-efebbd04aad1" />

If I do docker image list, you'll see that I've got the image listed there twice, once as I created it earlier, and a second time with the tag including the container registry.

<img width="1307" height="579" alt="image" src="https://github.com/user-attachments/assets/4bdba0c3-27a4-4dd1-baa1-62d1a074a21a" />

Jumping back to the repository, you'll now see we've got the package with the latest version

<img width="957" height="206" alt="image" src="https://github.com/user-attachments/assets/3dfb16b9-7e24-4bcd-8d3c-7fa86fc75683" />

Pulled the image from GHCR, now the container is running locally and the service responds on port 3000

<img width="865" height="201" alt="image" src="https://github.com/user-attachments/assets/8761f44e-9f24-4504-805a-4cbc4f6d6273" />
Docker's built-in health checker polling the health endpoint every 30s; if it fails three times in a row, the container gets marked unhealthy. 

In a production setup, this is what Kubernetes or a load balancer would be doing instead.
