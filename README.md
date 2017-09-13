# Technical exercise: Dancing with Death

## RESUME

**Part 1:**​ You will have to create a REST API for scheduling
appointments to have a dance with Death. The API has to be
implemented as a CRUD that keeps appointments, which will
be used in part 2 by a web client.

-   The system should not allow to book more than 1
appointment per hour.
-   The schedule must be set for office hours (9 am to 6
pm Monday to Friday) all year long
-   Death is very picky with its agenda, so every
appointment must contain date, start time and contact
information (like e-mail).
-   You can only appointment of 1 hour long with Death,
more would be pointless. Less would be too
traumatic.


**Part 2:​** Create a web client for the API you just created.

-   The first layout will display a date selector showcasing the current month.
-   If you click on any date, the available hour spaces will be displayed on screen to be
selected.

## DEPLOY

### Technical description

The project consists of two applications  <u>endpoint</u> and <u>frontend</u>.

**The endpoint** is a Python API builded with the Django Framework, the most important strengths of this application were the implementation of the JSON-API specifications and the social login with the services provider Auth0.

<u>TODO list: </u>

- To Implement a Logger services like Sentry or Logstash. (added in 0.2.0)

- Create a documentation with mocks using ApiBlueprint

**The FrontEnd** was my first application with Vue and many things were new for me, however I consider that some strengths in this applications was that I use Eslint to make a javascript legible code in other hand I use some things from ES6 specifications like the promise implementations, obviusly the implementation from npm paclage to included a lot of plugins.

<u>TODO lis:t</u>

- Create a service packages to centralize all the config and functions about API requests.

- To Add some unit test from some modules with es2

**Extra** I consider that other very important strength in this project was the docker implementation, maybe the Dockerfiles of this project can be improved, but I try to optimize and comply with good practices in most cases

## Settings

You need add two files to setting the enviroments in this project one for any application,
to deploy the <u>FrontEnd</u> you need create the **config.js** file into the folder:


```
frontend/src
```

You can use the ```config.js.example``` that you find in the same path

Later to set the <u>Endpoint</u> you need create **conf.json** file in ```endpoint``` folder like the other application you can use one file template ```conf.json.example```


###The Deployment

**Prerequisites**

-   [Docker 17.04.0+](https://docs.docker.com/engine/installation/)

-   [Docker-Compose 1.14.0+](https://docs.docker.com/compose/install/)

I used LinuxMint 18.2 x64 to deploy in my personal computer the project and ggenerally I need run all the docker-compose scripts with root permissions to build the images but in OSx enviroment I think that maybe this permissions are not necessary, finally execute the next scripts to deploy all the applications.


``` 
$ sudo docker-compose -f local.yml build

$ sudo docker-compose -f local.yml up
```

To show the containers status you can run th scripts without root permissions

```
$ docker-compose -f local.yml ps
```

Finally I deploy this application in local enviroments and this is the main reason that i do not use any web server image like apache or nginx, to show the app go to [http://localhost:8080](http://localhost:8080) and I added to compose script the Adminer image to show the database in the url [http://localhost:8081](http://localhost:8081)

