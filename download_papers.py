import numpy as np
from download import download_papers

titles = [
    "Self-Supervised Object Detection from Egocentric Videos",
    "STEPs: Self-Supervised Key Step Extraction and Localization from Unlabeled Procedural Videos",
    "Masked Spatio-Temporal Structure Prediction for Self-supervised Learning on Point Cloud Videos",
    "Learning Trajectory-Word Alignments for Video-Language Tasks",
    "Spatio-Temporal Crop Aggregation for Video Representation Learning",
    "Progressive Spatio-Temporal Prototype Matching for Text-Video Retrieval",
    "Long-range Multimodal Pretraining for Movie Understanding",
    "MGMAE: Motion Guided Masking for Video Masked Autoencoding",
    "Learning to Ground Instructional Articles in Videos through Narrations",
    "Accurate and Fast Compressed Video Captioning",
    "Few-Shot Video Classification via Representation Fusion and Promotion Learning"
]

if __name__ == "__main__":
  download_papers(titles)