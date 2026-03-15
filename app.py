import streamlit as st
import google.generativeai as genai

# --- TASARIM AYARLARI ---
st.set_page_config(page_title="GÖKAI Prompt Studio", page_icon="🚀", layout="centered")

# Özel CSS: Arka plan siyah, butonlar Telef10 yeşili, başlıklar GÖKAI mavisi
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
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #1B5E20; border: 1px solid #00E5FF; }
    h1 { color: #00E5FF; text-align: center; text-shadow: 0px 0px 10px #00E5FF; }
    div[data-testid="stMarkdownContainer"] > p { color: #E0E0E0; }
    </style>
    """, unsafe_allow_html=True)

# --- BAŞLIK ---
st.title("🚀 GÖKAI Prompt Studio")
st.markdown("<p style='text-align: center;'>Yapay Zeka İçerik ve Prompt Asistanı</p>", unsafe_allow_html=True)
st.markdown("---")

# --- YAN MENÜ ---
with st.sidebar:
    st.header("⚙️ Kontrol Paneli")
    api_key = st.text_input("Gemini API Anahtarınızı Girin:", type="password")
    st.markdown("---")
    st.write("📺 **Kanallarımız:**")
    st.write("👉 [Telef10 YouTube](https://youtube.com/@Telef10)")
    st.write("👉 [Gökhan Müzik](https://youtube.com/@GokhanMuzik)")

# --- ANA EKRAN ---
if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')

        mod = st.selectbox("Ne oluşturmak istersiniz?", ["🖼️ Görsel Prompt (Resim)", "🎵 Müzik Prompt (Suno/Eita)"])
        user_input = st.text_area("Hayalinizdeki detayı yazın:", placeholder="Örn: Anadolu rock tarzında hüzünlü bir parça...")

        if st.button("GÖKAI SİHRİNİ BAŞLAT"):
            if user_input:
                with st.spinner('GÖKAI sizin için en iyi parametreleri hazırlıyor...'):
                    if "Görsel" in mod:
                        prompt = f"Sen usta bir görsel sanatçısın. {user_input} isteğini; 8k, photorealistic, cinematic lighting ve Unreal Engine 5 kalitesinde bir resim promptuna dönüştür."
                    else:
                        prompt = f"Sen bir müzik prodüktörüsün. {user_input} isteğini Suno AI için; BPM, tür, enstrümanlar ve 'Gökhan Keser Style' vokal tanımıyla teknik bir prompta dönüştür."
                    
                    response = model.generate_content(prompt)
                    st.success("✅ Profesyonel Prompt Hazır!")
                    st.code(response.text, language='text')
            else:
                st.warning("Lütfen bir açıklama yazın.")
    except Exception as e:
        st.error(f"Bir bağlantı hatası oldu: {e}")
else:
    st.info("👋 Hoş geldin ortağım! Başlamak için sol menüye API anahtarını girmelisin.")

st.markdown("---")
st.caption("© 2026 GÖKAI Digital - Tüm Hakları Saklıdır.")
