# mlmath

For now, it include linear regression, logistic regression, generalized linear model and momentum.


### use docker

1. upload to github
```
docker login -u LaoLiulaoliu -p PERSONAL_TOKEN docker.pkg.github.com
docker tag IMAGEID docker.pkg.github.com/laoliulaoliu/mlmath/IMAGE_NAME:VERSION
docker push docker.pkg.github.com/laoliulaoliu/mlmath/IMAGE_NAME:VERSION
```

2. use docker to launch
```
docker run -p 8888:8888 mlmath jupyter notebook --allow-root
```
