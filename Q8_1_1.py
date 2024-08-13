import os

def prepare_dir():
    save_dir = "save_dir"
    
    if os.path.exists(save_dir):
        print(f"'{save_dir}' は既に存在します。")
    else:
        os.makedirs(save_dir)
        print(f"'{save_dir}' を作成しました。")

