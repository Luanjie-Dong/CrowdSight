import torch
import torch.nn as nn
import torch.nn.functional as F
import network
from .models import CMTL
import numpy as np

class CrowdCounter(nn.Module):
    def __init__(self, ce_weights=None):
        super(CrowdCounter, self).__init__()        
        self.CCN = CMTL()
        if ce_weights is not None:
            ce_weights = torch.Tensor(ce_weights)
            ce_weights = ce_weights.cuda()
        self.loss_mse_fn = nn.MSELoss()
        self.loss_bce_fn = nn.BCELoss(weight=ce_weights)
        
    @property
    def loss(self):
        return self.loss_mse + 0.0001*self.cross_entropy
    
    def forward(self, im_data, gt_data=None, gt_cls_label=None, ce_weights=None):
        # Convert numpy array to tensor if necessary and move to CUDA
        if isinstance(im_data, np.ndarray):
            im_data = torch.tensor(im_data, requires_grad=self.training).cuda()
        
        density_map, density_cls_score = self.CCN(im_data)
        density_cls_prob = F.softmax(density_cls_score, dim=1)
        
        if self.training:                        
            if isinstance(gt_data, np.ndarray):
                gt_data = torch.tensor(gt_data, requires_grad=self.training).cuda()
            if isinstance(gt_cls_label, np.ndarray):
                gt_cls_label = torch.tensor(gt_cls_label, dtype=torch.float32, requires_grad=self.training).cuda()
            self.loss_mse, self.cross_entropy = self.build_loss(density_map, density_cls_prob, gt_data, gt_cls_label, ce_weights)
            
        return density_map
    
    def build_loss(self, density_map, density_cls_score, gt_data, gt_cls_label, ce_weights):
        loss_mse = self.loss_mse_fn(density_map, gt_data)        
        ce_weights = torch.Tensor(ce_weights)
        ce_weights = ce_weights.cuda()
        cross_entropy = self.loss_bce_fn(density_cls_score, gt_cls_label)
        return loss_mse, cross_entropy

