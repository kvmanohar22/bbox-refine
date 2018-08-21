import numpy as np
import pandas as pd
import os

from chainercv.datasets.voc.voc_bbox_dataset import VOCBboxDataset
from chainercv.datasets.voc.voc_utils import voc_bbox_label_names

from utils.common import get_tightest_bboxes

class voc_loader:
    def __init__(self, data_dir, split='val', super_root=None):
        self.loader = VOCBboxDataset(data_dir=data_dir, split=split)
        self.ids = self.loader.ids
        self.super_root = super_root
    
    def len(self):
        return len(self.ids)

    def fix_superpixels(self, contours):
        """ This is just a temporary fix
            Currently the superpixels have one less row
        """
        H, W = contours.shape
        new_contours = np.empty((H+1, W), dtype=contours.dtype)
        new_contours[:-1, :] = contours
        new_contours[-1, :] = contours[-1]
        return new_contours

    def get_superpixels(self, idx):
        contours = pd.read_csv(os.path.join(self.super_root, self.ids[idx]+'.csv')).values
        contours = self.fix_superpixels(contours)
        min_region = contours.min()
        max_region = contours.max()
        masks = np.array([contours == idx for idx in range(min_region, max_region+1, 1)])
        boxes = get_tightest_bboxes(masks)

        return masks, boxes

    def load_single(self, idx):
        img, bbox, labels = self.loader.get_example(idx)
        masks, boxes = self.get_superpixels(idx)
        return (img, bbox, labels, masks, boxes)

    def load_batch(self, start_idx, end_idx):
        pass
