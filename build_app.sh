git add .
git commit -m "$1"
git push origin -u main:main
docker build -t palondomus/caesaraigcp:latest .
docker push palondomus/caesaraigcp:latest
docker run -it -p 8080:8080 palondomus/caesaraigcp:latest