import streamlit as st
import google.generativeai as genai

# --- TASARIM AYARLARI ---
st.set_page_config(page_title="GÖKAI Prompt Studio", page_icon="🚀", layout="centered")

# Tasarımı Güzelleştiren CSS
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; }
    .stButton>button {
        background-color: #2E7D32; 
        color: white;
        border-radius: 12px;
        font-weight: bold;
        border: none;
        width: 100%;
        height: 3.5em;
        box-shadow: 0px 4px 15px rgba(0, 229, 255, 0.2);
    }
    h1 { color: #00E5FF; text-align: center; font-family: 'Courier New', Courier, monospace; }
    .logo-img { display: block; margin-left: auto; margin-right: auto; width: 180px; border-radius: 50%; border: 2px solid #00E5FF; }
    </style>
    """, unsafe_allow_html=True)

# --- LOGO EKLEME (GitHub'daki logo.png dosyasını çeker) ---
# Not: Eğer logonun uzantısı .jpg ise aşağıdaki satırı logo.jpg olarak düzeltmelisin.
st.image("20260314_043409.png", width=180) 

st.title("GÖKAI Prompt Studio")
st.markdown("<p style='text-align: center; color: #E0E0E0;'>Yapay Zeka İçerik ve Prompt Asistanı</p>", unsafe_allow_html=True)
st.markdown("---")

# --- YAN MENÜ (GÜNCEL LİNKLER) ---
with st.sidebar:
    st.header("⚙️ Kontrol Paneli")
    api_key = st.text_input("Gemini API Anahtarınızı Girin:", type="password")
    st.markdown("---")
    st.write("📺 **Resmi Kanallarımız:**")
    st.write("👉 [Telef10 Yemek](https://youtube.com/@telef10.?si=p_BFSFCmg6085Gzz)")
    st.write("👉 [Gökhan Müzik](https://youtube.com/@gokhan_official?si=5UsToNsEXCaCcxhh)")
    st.write("👉 [GÖKAI YouTube](https://youtube.com/@gok-ai?si=Pf_gxUCPBn9YAcWd)")
    st.markdown("---")
    st.caption("GÖKAI Studio v1.2")

# --- ANA SİSTEM ---
if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')

        mod = st.selectbox("Ne oluşturmak istersiniz?", ["🖼️ Görsel Prompt (Resim)", "🎵 Müzik Prompt (Suno/Eita)"])
        user_input = st.text_area("Hayalinizdeki detayı yazın:", placeholder="Örn: Anadolu rock tarzında, yüksek enerjili bir parça...")

        if st.button("GÖKAI SİHRİNİ BAŞLAT"):
            if user_input:
                with st.spinner('GÖKAI algoritması çalışıyor...'):
                    if "Görsel" in mod:
                        prompt = f"Sen usta bir görsel sanatçısın. {user_input} isteğini; 8k, photorealistic, cinematic lighting içeren profesyonel bir resim promptuna dönüştür."
                    else:
                        prompt = f"Sen bir müzik prodüktörüsün. {user_input} isteğini Suno AI için teknik terimlerle ve 'Gökhan Keser Style' vokal tanımıyla bir prompta dönüştür."
                    
                    response = model.generate_content(prompt)
                    st.success("✅ Profesyonel Prompt Hazır!")
                    st.code(response.text, language='text')
            else:
                st.warning("Lütfen bir fikir yazın.")
    except Exception as e:
        st.error(f"Bağlantı Hatası: {e}")
else:
    st.info("👋 Hoş geldin ortağım! Başlamak için sol menüye API anahtarını girmelisin.")

st.markdown("---")
st.caption("© 2026 GÖKAI Digital - Tüm Hakları Saklıdır.")
