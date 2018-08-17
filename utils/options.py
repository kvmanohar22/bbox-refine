import argparse
import os

class options(object):
	""" Holds the different hyper-parameters """

	def __init__(self):
		self.parser = argparse.ArgumentParser()
		self.initialized = False
		self.user = os.environ.get('USER')

	def initialize(self):
		# Training
		self.parser.add_argument('--batch_size', type=int, default=64, help='batch size')
		self.parser.add_argument('--project_root', type=str, default='', help='Path to root of the project')
		self.parser.add_argument('--data_root', type=str, default='',help='Path to the root of dataset')
		self.parser.add_argument('--train', action='store_true', help='Train / test')
		self.parser.add_argument('--max_epochs', type=int, default=1000, help='Number of epochs to train the model')
		self.parser.add_argument('--img_h', type=int, default=224, help='Image hieght')
		self.parser.add_argument('--img_w', type=int, default=224, help='Image width')
		self.parser.add_argument('--gpu_id', type=int, default=-1, help='GPU id')
		self.parser.add_argument('--dataset', type=str, default='voc', help='Dataset to use')
		self.parser.add_argument('--n_classes', type=int, default=21, help='Number of classes (including background)')
		self.parser.add_argument('--ckpt_frq', type=int, default=10, help='Checkpoint frequency (in epochs)')
		self.parser.add_argument('--sample_frq', type=int, default=1, help='Sample images frequency (in epochs)')
		self.parser.add_argument('--display_frq', type=int, default=200, help='Display log after')
		self.parser.add_argument('--base_lr', type=float, default=3e-4, help='Initial learning rate')
		self.parser.add_argument('--gamma', type=float, default=0.1, help='Drop lr by this factor after `lr_decay_frq`')
		self.parser.add_argument('--lr_start_epoch', type=int, default=400, help='No. of epochs to train with starting learning rate')
		self.parser.add_argument('--lr_decay_frq', type=int, default=200, help='Decay the learning rate after these many epochs linearly')

	def parse(self, train_mode=False):
		if not self.initialized:
			self.initialize()
		args = self.parser.parse_args()
		args.train = train_mode

		self.opts = vars(args)
		return self.opts