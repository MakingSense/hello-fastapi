# Hello FastAPI

A basic template for a microservice API based on Python FastAPI with CI, CD, Code Formatting, Authentication, and other common practices in Doppler teams.

<!-- TODO: replace "_Yeoman_ or _dotnet new_ scaffolding template" for python equivalent -->

For the moment, it is only a kind of example. In the future, it could be converted into a _Yeoman_ or _dotnet new_ scaffolding template 🤷‍♂️.

## Context

We base our CI/CD process on Jenkins, Docker Hub, and Docker Swarm.

Jenkins generates the images based on [doppler-jenkins-ci.groovy](./doppler-jenkins-ci.groovy) (a renamed Jenkisfile). We refer to these generated images in a Docker Swarm using an _auto-redeploy_ approach. The [Doppler Swarm repository](https://github.com/MakingSense/doppler-swarm) stores the configuration of our Docker Swarm.

You can find a detailed description of our Git flow and the relation with Docker Hub in [Doppler-Forms repository](https://github.com/MakingSense/doppler-forms/blob/master/README.md#continuous-deployment-to-test-and-production-environments), but basically, it is the following:

-   Pull Requests generates images with tags like `pr-177` (`pr-{pull request id}`) and (`pr-{pull request id}-{commit id}`).

-   Merging in `main` (or `master` in some repositories) generates images with tags like `main` and `main-60737d6` (`main-{commit id}`). In general, these images are deployed automatically into the QA environment.

-   Resetting the branch `INT` generates images with tags like `INT` and `INT-60737d6` (`INT-{commit id}`). In general, these images are deployed automatically into the INT environment.

-   Tagging with the format `v#.#.#` generates images with tags like `v1`, `v1.3`, `v1.3.0`, `v1.3.0_982c388`. In general, our Production environment refers to images with tags like `v1` (only the mayor), so, depends on that, these images could be deployed automatically to the Production environment.

## Run validations in local environment

The source of truth related to the build process is [doppler-jenkins-ci.groovy](./doppler-jenkins-ci.groovy) (a renamed Jenkisfile). It basically runs docker build, so, you can reproduce jenkins' build process running `docker build .` or `sh ./verify-w-docker.sh`.

If you prefer to run these commands without docker, you can read [Dockerfile](./Dockerfile) and follow the steps manually.

## Features

-   [ ] Base conventions for a Python FastAPI project.

-   [x] Normalize to Linux line endings by default for all files (See [.editorconfig](./.editorconfig) and [.gitattributes](./.gitattributes)).

-   [x] Ignore from git and docker files with the convention that denotes secrets (See [.gitignore](./.gitignore) and [.dockerignore](./.dockerignore)).

-   [x] Prettier validation for all supported files.

-   [x] Editor Config validation using `eclint`.

-   [x] Launch and debug settings for VS Code ([.vscode](./.vscode)).

-   [x] Custom color (FastAPI based #009485) for VS Code (using [Peacock](https://marketplace.visualstudio.com/items?itemName=johnpapa.vscode-peacock&wt.mc_id=vscodepeacock-github-jopapa), see [settings.json](./.vscode/settings.json)).

-   [x] Python Format, Linting and Test validation

-   [x] Generation of the docker images following Doppler convention and publish them to Docker Hub (See [build-n-publish.sh](./build-n-publish.sh)).

-   [x] Generation of `version.txt` file with the image version and expose as a static file.

-   [x] [demo.http](./demo.http) to easily add manual tests for the exposed API with [VS Code REST Client](https://marketplace.visualstudio.com/items?itemName=humao.rest-client).

-   [x] Exposing only HTTP (not HTTPS) because that is the responsibility of our reverse proxy.

-   [x] Expose Swagger (`/openapi.json` / `/docs` / `redoc`).

-   [x] Including examples of self-hosting integration tests.

-   [ ] Including examples of unit tests.

-   [ ] Recommended FastAPI project structure

-   [ ] CORS ready

-   [ ] JWT and authorization following Doppler standards

-   [ ] Access to DB

## How to use this project

### Prepare the files

<!-- TODO: Complete it -->

### Push to GitHub

We are using the GitHub organizations [FromDoppler](https://github.com/FromDoppler) (for public code) and [MakingSense](https://github.com/MakingSense) (for private code).

Create a new empty project there, and create a PR to push the updated files. It should start a CI process in our Jenkins server.

### Configure GitHub branch protection rules

In [GitHub Branches Settings](https://github.com/FromDoppler/hello-fastapi/settings/branches) add a new protection rule for the `main` branch.

![github-settings-branches](./docs/github-settings-branches.png)

With the following configuration:

-   **Branch name pattern**: `main`
-   **Require status checks to pass before merging**: _checked_
-   **Require branches to be up to date before merging**: _checked_
-   **Status checks that are required**: `continuous-integration/jenkins/pr-head`
-   **Include administrators**: _checked_

![github-main-protection-rules](./docs/github-main-protection-rules.png)

### Configure Docker Hub Webhooks

At this point, the CI process already generated a Docker Hub repository and we should configure the WebHooks to enable the auto-redeploy in our environments.

**IMPORTANT:** You need the credentials of `dopplerdock` Docker Hub account. Ask for them.

Open the Webhooks configuration page of this new repository (this is the URL for hello-fastapi repository: <https://hub.docker.com/repository/docker/dopplerdock/hello-fastapi/webhooks>) and create the webhooks for production and test environments:

-   **cd-helper-production** `https://apis.fromdoppler.com/cd-helper/hooks/{{REEMPLACE-THE-SECRET-HERE}}/`
-   **cd-helper-test** `https://apisqa.fromdoppler.net/cd-helper/hooks/{{REEMPLACE-THE-SECRET-HERE}}/`

![dockerhub-webhooks](./docs/dockerhub-webhooks.png)

**IMPORTANT:** You can see the secrets in other Docker Hub repositories, for example in [_CD-Helper_'s one](https://hub.docker.com/repository/docker/dopplerdock/doppler-cd-helper/webhooks).

### Add the stack to Doppler Swarm repository

We should add the stack to [Doppler Swarm repository](https://github.com/MakingSense/doppler-swarm), it is possible using `hello-stack` as reference. Using _search in files_ is recommended to find all the places to update.
