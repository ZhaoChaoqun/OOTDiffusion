from huggingface_hub import snapshot_download

# 指定模型的路径
repo_id = "levihsu/OOTDiffusion"

# 下载模型文件夹到本地
local_dir = snapshot_download(repo_id, allow_patterns=["checkpoints/ootd/*"])
print(f'Model files downloaded to: {local_dir}')
