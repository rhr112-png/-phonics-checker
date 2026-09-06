import streamlit as st
from difflib import SequenceMatcher

# إعدادات الصفحة
st.set_page_config(page_title="Phonics Checker", page_icon="🎓", layout="centered")

# تنسيق الواجهة
st.markdown("""
    <style>
    .main { background-color: #F9FAFB; }
    .stButton>button { width: 100%; background-color: #4F46E5; color: white; border-radius: 10px; height: 3em; font-size: 18px; }
    .score-card { background-color: #EEF2FF; border: 2px solid #6366F1; border-radius: 12px; padding: 20px; text-align: center; }
    </style>
""", unsafe_allow_html=True)

st.title("🎓 Phonics Pronunciation Checker")
st.write("استمع للكلمة، اقرأها بصوتك، واحصل على تقييم نطقك فوراً!")

# الكلمة المستهدفة
target_word = st.text_input("الكلمة المطلوب نطقها (Target Word):", "cat").strip().lower()

# إدخال الصوت/النص
st.subheader("🎤 اقرأ الكلمة:")
user_input = st.text_input("اكتب الكلمة المنطوقة لتحديد نسبة المطابقة:").strip().lower()

if st.button("تقييم النطق 🎯"):
    if user_input:
        ratio = SequenceMatcher(None, target_word, user_input).ratio()
        score = int(ratio * 100)
        
        st.markdown(f"""
            <div class="score-card">
                <h2>درجة دقة النطق</h2>
                <h1 style="color: #4F46E5; font-size: 50px;">{score}%</h1>
            </div>
        """, unsafe_allow_html=True)
        
        if score == 100:
            st.success("🌟 ممتاز جداً! نطق صحيح 100%")
        elif score >= 70:
            st.info("👍 جيد جداً! نطقك قريب جداً من الصحيح.")
        else:
            st.warning("🔄 حاول مرة أخرى بوضوح أكثر.")
    else:
        st.error("الرجاء إدخال الكلمة أولاً.")
