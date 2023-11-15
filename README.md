<h1 align="center">
  Web application for identifying completed forms
  <br>
</h1>

<h4 align="center">
    Test task for python developer role at LeadHit
    <br>
</h4>

<div align="center">

[![Conventional Commits](https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white)](https://conventionalcommits.org)

</div>
<hr>

<p align="center">
  <a href="#tech-stack">Tech stack</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#additional-material">Additional material</a>
</p>


## Tech stack
- [Python 3.11](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/)
- [FastApi](https://fastapi.tiangolo.com/)
- [MongoDB](https://www.mongodb.com/)
- [docker](https://docs.docker.com/get-docker/)
- [docker-compose](https://docs.docker.com/compose/install/)


## How To Use
To clone and run this project, you'll need:
* [Git](https://git-scm.com)
* [Poetry](https://python-poetry.org/docs/#installation) (Optional)
* [Postman](https://www.postman.com/downloads/) (Optional)
* [Make](https://www.gnu.org/software/make/#download) (Optional)


<details>

<summary><strong>Local run use Docker</strong></summary>

1. Firstly clone repo
   ```bash
   git clone git@github.com:mrKazzila/test_task_7.git
   ```

2. Run docker compose with make
   ```bash
   make docker_up
   ```
   or by cli
   ```bash
   docker-compose --env-file env/.env -p kazakov-test_task -f docker-compose.yaml up -d --build
   ```

3. Open [OpenAPi](http://localhost:8000/docs) for testing or use [Postman collection]()

4. Stop docker compose with make
   ```bash
   make docker_down
   ```
   or by cli
   ```bash
   docker-compose --env-file env/.env -p kazakov-test_task -f docker-compose.yaml down
   ```

</details>



## Additional material

- [Test assignment file](readme/Test_assignment_Python_Junior+.pdf)
- [Simple docs](backend/README.md)
