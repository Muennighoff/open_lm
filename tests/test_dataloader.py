import torch

from open_lm.data import get_wds_dataset
from open_lm.train import sample_chunk
from tests.shared import MockDataArgs


def test_dataloader_no_crash():
    # basic test to make sure the datalaoder does not crash
    args = MockDataArgs()
    di = get_wds_dataset(args, True)

    for _ in di.dataloader:
        pass

    assert True


def test_dataloader_shape():
    # basic test to make sure the datalaoder does not crash
    args = MockDataArgs()
    di = get_wds_dataset(args, True)

    batch = next(iter(di.dataloader))
    (texts,) = batch
    inputs, targets = sample_chunk(torch.LongTensor(texts), args.seq_len, args.target_mask_left)
    assert inputs.shape[-1] == args.seq_len
    assert targets.shape[-1] == args.seq_len
