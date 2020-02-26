# dockerD: Docker Demo
Docker Demo with Flask

### Clone the repo
```
git clone https://www.github.com/shivampip/dockerD
cd dockerD
```

### Build the docker image
```
docker build . -t myflask
```
* `.` means source code is in current dir
* `myflask` is name, we want to give to our image
* Verify the image created by
```
docker images
```

### Run the image
```
docker run -d --name greenflask -p 1000:5000 -e BG_COL=green myflask
```
* `d`: run in detached mode
* container-name: greenflask
* Host machine port: 1000
* Environment variable: `BG_COL` with value `green`
  

