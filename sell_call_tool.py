import os
import pickle
import streamlit as st
import urllib.request

# 取得當前目錄
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "sell_call_model.pkl")

# 如果模型不存在，則從 GitHub 下載
if not os.path.exists(model_path):
    model_url = "https://raw.githubusercontent.com/vettelwow/sell-call-predictor/main/sell_call_model.pkl"
    try:
        urllib.request.urlretrieve(model_url, model_path)
        st.success("✅ 成功下載模型檔案！")
    except Exception as e:
        st.error(f"❌ 錯誤：無法下載模型檔案！\n{e}")
        st.stop()

# 載入模型
with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

# 應用介面
st.title('SELL CALL 成功率預測工具')
st.write("請輸入市場數據，系統將預測 SELL CALL 的成功率，並給出建議。")
