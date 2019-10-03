This demonstrates running multiple Python Servers behind Nginx in Docker.

We use Nginx to proxy the python servers under different paths.
We use supervisord to ensure all parts start and restart correctly.

## To build:
```docker build -f DOCKERFILE -t testnginxproxy .```
## To run:
```docker run -d -it -p 8000:8000 --name=nginxtest testnginxproxy```

## To remove:
```
docker stop nginxtest
docker rm nginxtest
```
