""" OmegaNeo model configuration"""

from transformers import PretrainedConfig
from transformers.utils import logging


logger = logging.get_logger(__name__)


# from transformers.deprecated._archive_maps import OMEGANEO_PRETRAINED_CONFIG_ARCHIVE_MAP  # noqa: F401, E402


class OmegaNeoConfig(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`OmegaNeoModel`]. It is used to instantiate a
    OmegaNeo model according to the specified arguments, defining the model architecture. Instantiating a configuration
    with the defaults will yield a similar configuration.
    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.
    """

    model_type = "omeganeo"
    keys_to_ignore_at_inference = ["past_key_values"]

    def __init__(
        self,
        vocab_size=151936,
        hidden_size=4096,
        intermediate_size=22016,
        num_hidden_layers=32,
        num_attention_heads=32,
        num_key_value_heads=32,
        hidden_act="silu",
        max_position_embeddings=32768,
        initializer_range=0.02,
        rms_norm_eps=1e-6,
        use_cache=True,
        tie_word_embeddings=False,
        rope_theta=10000.0,
        use_sliding_window=False,
        sliding_window=4096,
        max_window_layers=28,
        attention_dropout=0.0,
        **kwargs,
    ):
        self.vocab_size = vocab_size
        self.max_position_embeddings = max_position_embeddings
        self.hidden_size = hidden_size
        self.intermediate_size = intermediate_size
        self.num_hidden_layers = num_hidden_layers
        self.num_attention_heads = num_attention_heads
        self.use_sliding_window = use_sliding_window
        self.sliding_window = sliding_window
        self.max_window_layers = max_window_layers

        # for backward compatibility
        if num_key_value_heads is None:
            num_key_value_heads = num_attention_heads

        self.num_key_value_heads = num_key_value_heads
        self.hidden_act = hidden_act
        self.initializer_range = initializer_range
        self.rms_norm_eps = rms_norm_eps
        self.use_cache = use_cache
        self.rope_theta = rope_theta
        self.attention_dropout = attention_dropout

        super().__init__(
            tie_word_embeddings=tie_word_embeddings,
            **kwargs,
        )