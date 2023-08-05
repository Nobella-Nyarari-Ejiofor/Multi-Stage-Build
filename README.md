# Docker Multi-Stage Build 

Docker's multi-stage capability is critical for creating leaner container images, which optimizes image sizes and resource efficiency. Developers can use this capability to isolate their build environments from their runtime environments, copying only the necessary artifacts to the final runtime image.

Multi-stage builds substantially reduce size by reducing build-time dependencies, resulting in faster downloads, fewer storage requirements, and increased security.

Let's get into a practical example.

## Getting Started
To do this practically on your CLI :

```bash
git clone https://github.com/Nobella-Nyarari-Ejiofor/Multi-Stage-Build.git
```

## Usage
In the master branch you can see 2 folders : [multi-stage-build](https://github.com/Nobella-Nyarari-Ejiofor/Multi-Stage-Build/tree/master/multi-stage-build) and [without-multi-stage-build](https://github.com/Nobella-Nyarari-Ejiofor/Multi-Stage-Build/tree/master/without-multi-stage-build) . The folders contain a docker file and a small application called rock-paper-scissors for the image creation.

## Contributing


## License

[MIT](https://choosealicense.com/licenses/mit/)
