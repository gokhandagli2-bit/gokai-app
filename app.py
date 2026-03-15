import streamlit as st
import google.generativeai as genai
import os

# --- TASARIM AYARLARI ---
st.set_page_config(page_title="GÖKAI Prompt Studio", page_icon="🚀", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0E1117; }
    .stButton>button {
        background-color: #2E7D32; 
        color: white;
        border-radius: 12px;
        font-weight: bold;
        width: 100%;
        height: 3.5em;
        box-shadow: 0px 4px 15px rgba(0, 229, 255, 0.2);
    }
    h1 { color: #00E5FF; text-align: center; }
    .logo-img { display: block; margin-left: auto; margin-right: auto; width: 180px; }
    </style>
    """, unsafe_allow_html=True)

# Logo Yükleme
if os.path.exists("logo.png"):
    st.image("logo.png", width=180)

st.title("GÖKAI Prompt Studio")
st.markdown("<p style='text-align: center; color: #E0E0E0;'>Yapay Zeka İçerik Asistanı</p>", unsafe_allow_html=True)
st.markdown("---")

# --- YAN MENÜ ---
with st.sidebar:
    st.header("⚙️ Kontrol Paneli")
    # Eğer Secrets içinde anahtar varsa otomatik kullanır, yoksa kutu gösterir
    if "GEMINI_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_KEY"]
        st.success("✅ GÖKAI Bağlantısı Aktif")
    else:
        api_key = st.text_input("Gemini API Anahtarınızı Girin:", type="password")
    
    st.markdown("---")
    st.write("📺 **Kanallarımız:**")
    st.write("👉 [Telef10 Yemek](https://youtube.com/@telef10.?si=p_BFSFCmg6085Gzz)")
    st.write("👉 [Gökhan Müzik](https://youtube.com/@gokhan_official?si=5UsToNsEXCaCcxhh)")
    st.write("👉 [GÖKAI YouTube](https://youtube.com/@g-ok-ai?si=Pf_gxUCPBn9YAcWd)")

# --- ANA SİSTEM ---
if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        mod = st.selectbox("Ne oluşturmak istersiniz?", ["🖼️ Görsel Prompt (Resim)", "🎵 Müzik Prompt (Suno/Eita)"])
        user_input = st.text_area("Hayalinizdeki detayı yazın:")

        if st.button("GÖKAI SİHRİNİ BAŞLAT"):
            if user_input:
                with st.spinner('GÖKAI hesaplıyor...'):
                    if "Görsel" in mod:
                        prompt = f"Sen usta bir görsel sanatçısın. {user_input} isteğini; 8k, photorealistic, cinematic lighting içeren bir prompta dönüştür."
                    else:
                        prompt = f"Sen bir müzik prodüktörüsün. {user_input} isteğini Suno AI için teknik terimlerle ve 'Gökhan Keser Style' vokal tanımıyla bir prompta dönüştür."
                    
                    response = model.generate_content(prompt)
                    st.success("✅ Profesyonel Prompt Hazır!")
                    st.code(response.text, language='text')
    except Exception as e:
        st.error(f"Hata oluştu: {e}")
else:
    st.info("👋 Hoş geldin! Başlamak için lütfen ayarları kontrol et.")
