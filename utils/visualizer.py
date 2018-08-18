import matplotlib.pyplot as plt

from chainercv.visualizations import vis_bbox
from chainercv.datasets import voc_bbox_label_names

class Visualize:
    def __init__(self, names):
        self.names = names
    
    def __call__(self, img, bbox, label, score, save=False, path=None):
        vis_bbox(
            img, bbox, label, score, label_names=self.names
        )
        plt.xticks([])
        plt.yticks([])

        if save:
            if path is None:
                raise ValueError('Path should be set')
            plt.savefig(path)
        else:
            plt.show()

    def bulk(self, samples):
        """ Visualize bulk of images
        """
        imgs, bboxs, labels, scores, paths = zip(*samples)
        for img, bbox, label, score, path in zip(
            imgs, bboxs, labels, scores, paths):
            self.__call__(
                img, bbox, label, score, save=True, path=path
                )

    def box_alignment(self, img, old_boxes, new_boxes, Spixels,
                      save=False, path=None
                      ):
        """ Visualize the change in the bboxes after box alignment

        TODO: Add superpixels belonging to each updated box
        Args:
            img      : Input image
            old_boxes: Old bboxes
            new_boxes: Updated bboxes
            Spixels  : set of superpixels
        """
        fig = plt.figure(figsize=(16, 7))
        ax1 = fig.add_subplot(121)
        plt.xticks([])
        plt.yticks([])
        plt.title('Original box')
        vis_bbox(img, old_boxes, ax=ax1)

        ax2 = fig.add_subplot(122)
        plt.xticks([])
        plt.yticks([])
        plt.title('After box-alignment')
        vis_bbox(img, new_boxes, ax=ax2)
        if save:
            if path is None:
                raise ValueError('Path should be set')
            plt.savefig(path)
        else:
            plt.show()
