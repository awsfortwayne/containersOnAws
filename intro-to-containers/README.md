## Build Image
```docker build -t sample-flask-app .```
```docker build -t second-sample-flask-app .```

## Run Container
```docker run -it -p 80:80 -v ${pwd}/sample-app/:/app sample-flask-app bash```



## Tag Container

```docker tag sample-flask-app aschu/sample-flask-app:latest```
```docker tag second-sample-flask-app aschu/second-sample-flask-app:latest```

