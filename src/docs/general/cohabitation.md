This page aims to present how to work with two different versions of OpenFLUID on the same computer. Warning: it can not be done directly by installing both versions in the same fashion, this would break both installations.

Solution below relies on virtualization of one of the versions, we will consider in this example that we want to **keep OpenFLUID 2.1.x on system and use a container to run OpenFLUID 2.2.x**.

# Pros and cons
## Interest
This approach will allow to use both versions without interaction. Every app should work, CLI and UI. Daily use should be transparent if setup is done correctly.

## Limits
Cohabitation requires to be careful to strict compartimentation of installations.

This solution will become less suitable if the host system is different than the docker system (Ubuntu 22.04 for our docker image): the day you want to stop using OpenFLUID 2.1 on your system to work solely with OpenFLUID 2.2, the code of your wares will be available but the compiled objects will not be compatible with the system, meaning **you will have to rebuild them all**.

Other issue: the interaction with external tools will not work (opening a pdf or a file explorer), you will have to open them directly from the host OS

# Setup
Here we will use Docker, which requires root access to be run. If not applicable, you can use *singularity* container system (cf [this page](../start/install.md/#singularity))

## Install Docker

If you don't have docker on your system, follow [these steps](https://docs.docker.com/engine/install/), and [post-install instructions](https://docs.docker.com/engine/install/linux-postinstall/) to give non-root rights

## Install OpenFLUID Docker image

Run following command to install OpenFLUID 2.2.0 image
``` sh
docker pull openfluid/openfluid:2.2.0
```

# Run
Before doing following step, copy your `.openfluid` folder in an other location to back-up it and avoid any data loss.

Once installed you can run it with (can be put in a shell script to use it easier):
```sh
xhost +local: # to redirect X11 display for Builder and DevStudio

docker run --net=host -i --rm \
    -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
    -e DISPLAY=$DISPLAY \
    -v $HOME/.openfluid_2-2:/home/openfluid/.openfluid \
    -t openfluid/openfluid:2.2.0
```
!!! warning
    It is advised to link in-docker `$HOME/.openfluid` to a repository on host to keep data between executions as shown above, **any data not shared with host through `-v` will be lost as soon as container is closed**, eg newly installed packages on docker, setting files changes, ware code or simulation results.

The line `-v $HOME/.openfluid_2-2:$HOME/.openfluid` means that projects and ware development done in the container will be visible and saved on host in a `.openfluid_2-2` folder.