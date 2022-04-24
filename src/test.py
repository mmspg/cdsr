import os.path as osp
import logging
import time
import argparse
from collections import OrderedDict
import os
import options.options as option
import utils.util as util
from data.util import bgr2ycbcr
from data import create_dataset, create_dataloader
from models import create_model
from preprocess.utils import imresize
import torch

if __name__ == '__main__':
    #### options
    torch.multiprocessing.freeze_support()
    #### options
    parser = argparse.ArgumentParser()
    parser.add_argument('-opt', type=str, required=True, help='Path to options YMAL file.')
    opt = option.parse(parser.parse_args().opt, is_train=False)
    opt = option.dict_to_nonedict(opt)

    logger = logging.getLogger('base')
    logger.info(option.dict2str(opt))

    dataset_opt = opt['datasets']['test']

    # print(opt['datasets']['test'])
    # print(dataset_opt['mode'])
    # exit()

    #### Create test dataset and dataloader
    test_set = create_dataset(dataset_opt)
    test_loader = create_dataloader(test_set, dataset_opt)
    logger.info('Number of test images in [{:s}]: {:d}'.format(dataset_opt['name'], len(test_set)))

    model = create_model(opt)

    test_set_name = test_loader.dataset.opt['name']
    logger.info('\nTesting [{:s}]...'.format(test_set_name))
    test_start_time = time.time()
    dataset_dir = opt['path']['out_path']
    util.mkdir(dataset_dir)

    for data in test_loader:
        img_path = data['LQ_path'][0]
        img_name = osp.splitext(osp.basename(img_path))[0]

        data['LQ'] = torch.stack([imresize(data['LQ'][0], 1.0 / 4, True)])
        model.feed_data(data, is_val=True)
        model.test()

        visuals = model.get_current_visuals(need_GT=False)
        reconstructed = util.tensor2img(visuals['SR'])  # uint8

        # Save SR images for reference
        save_img_path = os.path.join(dataset_dir, img_name + '.png')
        print(img_name)
        util.save_img(reconstructed, save_img_path)

        #save_lr_img_path = os.path.join("../datasets/va-x-compare/", img_name + '.png')
        #util.save_img(util.tensor2img(data['LQ'].detach()), save_lr_img_path)

    test_run_time = time.time()-test_start_time
    print('Runtime {} (s) per image'.format(test_run_time / len(test_loader)))
