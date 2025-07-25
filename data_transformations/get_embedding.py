from sentence_transformers import SentenceTransformer
import torch

if torch.backends.mps.is_available():
    device = "mps"
    print("Using Apple Silicon")
else:
    device = "cpu"
    print("MPS not available, using CPU")

model = SentenceTransformer(
    "Qwen/Qwen3-Embedding-0.6B",
    model_kwargs={"attn_implementation": "sdpa"},
    device=device,
)


def compute_embedding(text, prompt=None):
    return model.encode(text, prompt=prompt)


