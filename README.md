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

Download pretrained models `pretrained_model.tgz` (link to be added).
Extract files:
```
tar -xzf pretrained_model.tgz
```

Download the test dataset `jpegai.tgz` (link to be added).
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
