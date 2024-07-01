# Action Recognition demo

In this demo, we provide the AR model with an input video amd its output is a class label from the NTU RGB+D 120 dataset. The repository runs on top of the <a href='https://github.com/open-mmlab/mmaction2'>mmaction2</a> framework.

## How to run the demo

### Docker
Due to the requirement complications of the mmaction package it is suggested to pull our docker image and run it right away:

```bash
docker pull michkase/ardemo:0.0.3

# Run the demo on the CPU
docker run michkase/ardemo:0.0.3
# If there's a GPU available 
docker run --gpus all michkase/ardemo:0.0.3
```

You can also pass the model your own videos to test its performance on new data:
```bash
docker run --gpus all -v /full/path/to/video/folder:/mmaction2/data michkase/ardemo:0.0.3 --input_video data/[VIDEO_NAME]
```

Alternatively, you can build the docker image yourself:
```bash
# replace the [IMAGE_NAME] with a name of your choice
docker build -t [IMAGE_NAME] .
# Run the image
docker run [IMAGE_NAME]
```

### pip (Not reccommended)
Make sure you are using a Python version >=3.10 and you have created a new `venv` environment:

```bash
python3 -m venv [ENVIRONMENT_NAME]
source [ENVIRONMENT_NAME]/bin/activate 
```

Then install the following packages in this order:

```bash
pip install -U pip
git clone https://github.com/open-mmlab/mmaction2.git
cd mmaction2
pip3 install numpy
pip3 install torch==2.0.1 torchvision==0.15.2 torchaudio==2.0.2 --index-url https://download.pytorch.org/whl/cu118
pip3 install openmim
mim install mmengine
mim install mmcv==2.0.0
mim install mmdet
mim install mmpose
pip3 install -v -e .
```