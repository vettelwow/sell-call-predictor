import streamlit as st
import numpy as np
import pickle

# 加載機器學習模型
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "sell_call_model.pkl")

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)


# 應用介面
st.title('SELL CALL 成功率預測工具')
st.write("請輸入市場數據，系統將預測 SELL CALL 的成功率，並給出建議。")
