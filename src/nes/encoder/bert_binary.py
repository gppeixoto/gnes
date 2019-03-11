from .bert import BertEncoder
from .lopq import LOPQEncoder


class BertBinaryEncoder(LOPQEncoder):
    def __init__(self, num_bytes: int = 8,
                 cluster_per_byte: int = 255,
                 pca_output_dim: int = 256,
                 *args, **kwargs):
        super().__init__(num_bytes, pca_output_dim, cluster_per_byte)
        self.pipeline = [BertEncoder(*args, **kwargs)]
