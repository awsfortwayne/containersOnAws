## Build Image

```docker build -t sample-flask-app .```
```docker build -t second-sample-flask-app .```

## Run Container

```docker run -it -p 80:80 -v ${pwd}/sample-app/:/app sample-flask-app bash```



## Tag Container

```docker tag sample-flask-app 368218548347.dkr.ecr.us-east-1.amazonaws.com/aschu/sample-flask-app:latest```
```docker tag second-sample-flask-app 368218548347.dkr.ecr.us-east-1.amazonaws.com/aschu/second-sample-flask-app:latest```


## ECR Login

```aws ecr get-login  --no-include-email```


## Push Images
```docker push 368218548347.dkr.ecr.us-east-1.amazonaws.com/aschu/sample-flask-app:latest```
```docker push 368218548347.dkr.ecr.us-east-1.amazonaws.com/aschu/second-sample-flask-app:latest```

