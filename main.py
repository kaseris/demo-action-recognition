import argparse
import time

import torch
import numpy as np
from PIL import Image

from mmaction.apis import inference_recognizer, init_recognizer

from kinetic_annotation import annotations

def main(in_fname):
    config_path = 'configs/recognition/tsn/tsn_imagenet-pretrained-r50_8xb32-1x1x8-100e_kinetics400-rgb.py'
    checkpoint_path = 'tsn_imagenet-pretrained-r50_8xb32-1x1x8-100e_kinetics400-rgb_20220906-2692d16c.pth'
    input_fname = in_fname

    t0 = time.time()
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print(f'Using device: {device}')
    model = init_recognizer(config_path, checkpoint_path, device=device)  # build the model from a config file and a checkpoint file 
    print(f'Time to load: {(time.time() - t0):.4f}s')

    t0 = time.time()
    result = inference_recognizer(model, input_fname)  # test a single image
    print(f'Time to run: {(time.time() - t0):.4f}s')

    print(f'The predicted label: {result.pred_label.item()+1}')
    print(f"label: {annotations[result.pred_label.item()+1]}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_video', default='h2YqqUhnR34.mp4', type=str, required=False)
    args = parser.parse_args()

    print(f'input_video: {args.input_video}')
    main(in_fname=args.input_video)