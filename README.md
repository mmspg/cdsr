# Super resolution in the compressed domain of learning-based image codecs


CDSR stands for Compressed Domain Super Resolution.


## Setting up

### Docker

Build a Docker container:

```sh
sudo docker build . -t cdsr
```

Run the container:

```sh
sudo docker run --ipc=host --gpus all --rm -it \
    -v ${PWD}:/workspace \
    -w /workspace \
    cdsr bash
```

Alternatively run a Docker container for development:

```sh
sudo docker run --ipc=host --gpus all --rm -it \
    -p 0.0.0.0:6006:6006 -p 0.0.0.0:8888:8888 \
    --hostname cdsr-dev --name cdsr-dev \
    -v ${PWD}:/workspace \
    -w /workspace \
    cdsr bash
```

## Testing

The pretrained models and test dataset can be downloaded from the following **FTP** by using dedicated FTP clients, such as FileZilla or FireFTP (we recommend to use [FileZilla](https://filezilla-project.org/)):

```
Protocol: FTP
FTP address: tremplin.epfl.ch
Username: datasets@mmspgdata.epfl.ch
Password: ohsh9jah4T
FTP port: 21
```

Download pretrained models `pretrained_model.tgz` from the cdsr folder in the FTP server.
Extract files:

```
tar -xzf pretrained_model.tgz
```

Download the test dataset `jpegai.tgz` from the cdsr folder in the FTP server.
Extract the files from `jpegai.tgz` to the `datasets` folder:
```
mkdir datasets
cd datasets
tar -xzf jpegai.tgz
```

Inside the Docker container, run the following command:
```
cd src
python test.py -opt options/jpegai/test_jpegai.yml
```

The upscaled images will be found in the `results` folder.
