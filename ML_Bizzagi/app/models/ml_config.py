import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# 1. Muat Model dan Tokenizer dari Direktori Lokal
model_dir = "/path/ke/model/anda"  # Ganti dengan path direktori model Anda
tokenizer = AutoTokenizer.from_pretrained(model_dir)
model = AutoModelForSequenceClassification.from_pretrained(model_dir)