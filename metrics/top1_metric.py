from metrics.utils import AverageMeter, accuracy
from metrics.metric import Metric


class Top1Metric(Metric):
    def __init__(self):
        self.am = AverageMeter()

    def update(self, prediction, target):
        prec1, = accuracy(prediction, target, topk=(1,))
        self.am.update(prec1.item())

    def __repr__(self):
        return 'Prec@1 {am.val:.3f} ({am.avg:.3f})'.format(am=self.am)

    def compute(self):
        return ('top1', self.am.avg)
