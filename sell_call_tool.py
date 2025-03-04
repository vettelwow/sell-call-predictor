import os
import pickle
import streamlit as st
import numpy as np

# 取得目前 Python 檔案所在的目錄
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, "sell_call_model.pkl")

# 確保檔案存在後再載入
if os.path.exists(model_path):
    with open(model_path, 'rb') as model_file:
        model = pickle.load(model_file)
else:
    st.error(f"❌ 錯誤：找不到模型檔案 {model_path}，請確認 `sell_call_model.pkl` 是否已正確上傳！")
    st.stop()

# 應用介面
st.title('SELL CALL 成功率預測工具')
st.write("請輸入市場數據，系統將預測 SELL CALL 的成功率，並給出建議。")

# 輸入市場數據
emva = st.number_input('市場動能 (EMVA)', value=0.0)
rsi1 = st.number_input('RSI1 (短期 RSI)', value=50.0)
vix = st.number_input('VIX 指數 (市場波動率)', value=20.0)
foreign_oi = st.number_input('外資未平倉口數', value=0)
volatility = st.number_input('市場波動率 (5日標準差)', value=5.0)

# 預測成功率
if st.button('計算 SELL CALL 成功率'):
    input_data = np.array([[rsi1, vix, emva, volatility, foreign_oi]])
    success_prob = model.predict_proba(input_data)[0][1] * 100  # 成功機率
    
    st.write(f"### SELL CALL 成功率: {success_prob:.2f}%")
    
    # 提供建議
    if success_prob > 85:
        st.success("✅ 高成功率！可以執行 SELL CALL 策略，選擇較近的履約價（300-400 點價外）。")
    elif success_prob > 70:
        st.warning("⚠️ 中等成功率！可以考慮 SELL CALL，但建議選擇較遠的履約價（400-500 點價外）。")
    else:
        st.error("❌ 成功率較低！目前市場波動較大，不建議執行 SELL CALL，請考慮等待更穩定的市場條件。")

# 提示用戶如何運行此應用
st.write("### 本地執行指南")
st.write("1. 安裝 Streamlit：`pip install streamlit`")
st.write("2. 執行應用程式：`streamlit run sell_call_tool.py`")
