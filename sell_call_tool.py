import os
import pickle

# 取得目前 Python 檔案所在的目錄
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "sell_call_model.pkl")

# 確保檔案存在後再載入
if os.path.exists(model_path):
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
else:
    raise FileNotFoundError(f"❌ 錯誤：找不到模型檔案 {model_path}，請確認 `sell_call_model.pkl` 是否已正確上傳！")
