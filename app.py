import streamlit as st
import google.generativeai as genai

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="GÖKAI Prompt Studio", page_icon="🚀", layout="centered")

# --- GÖKAI LOGO VE BAŞLIK ---
st.title("🚀 GÖKAI Prompt Studio")
st.subheader("Yapay Zeka İçerik Asistanı")
st.markdown("---")

# --- API ANAHTARI GİRİŞİ (Sol Menü) ---
with st.sidebar:
    st.header("⚙️ Ayarlar")
    api_key = st.text_input("Gemini API Anahtarınızı Buraya Yapıştırın:", type="password")
    st.info("API anahtarınızı 'Google AI Studio' sitesinden ücretsiz alabilirsiniz.")

# --- ANA PROGRAM MANTIĞI ---
if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')

        # Seçenek Menüsü
        mod = st.radio("Hangi türde prompt istersiniz?", ["🖼️ Resim (Midjourney/DALL-E)", "🎵 Müzik (Suno/Eita)"])
        
        user_input = st.text_input("Hayalinizdeki içeriği kısaca tarif edin:", placeholder="Örn: Modern bir mutfakta sağlıklı salata tabağı...")

        if st.button("GÖKAI Sihrini Başlat"):
            if user_input:
                with st.spinner('GÖKAI sizin için en iyi parametreleri hesaplıyor...'):
                    # Prompt Mühendisliği Talimatları
                    if "Resim" in mod:
                        master_prompt = f"Sen profesyonel bir görsel tasarımcısın. Şu isteği 8k, ultra-realistic, cinematic lighting ve detaylı dokular içeren profesyonel bir Midjourney/DALL-E promptuna dönüştür: {user_input}"
                    else:
                        master_prompt = f"Sen bir müzik prodüktörüsün. Şu isteği Suno AI için teknik terimler (BPM, tür, enstrüman) içeren bir prompta dönüştür. Vokal tarzı olarak 'Gökhan Keser Style Male Vocals' ve 'Professional Mix' ibarelerini mutlaka ekle: {user_input}"
                    
                    response = model.generate_content(master_prompt)
                    
                    st.success("İşte profesyonel promptunuz hazır!")
                    st.code(response.text, language='text')
                    st.caption("Yukarıdaki kodu kopyalayıp ilgili yapay zeka aracında kullanabilirsiniz.")
            else:
                st.warning("Lütfen bir fikir yazın.")
    except Exception as e:
        st.error(f"Bir hata oluştu: {e}")
else:
    st.warning("⚠️ Devam etmek için lütfen sol menüye API anahtarınızı girin.")

st.markdown("---")
st.write("© 2026 GÖKAI Dijital Projeler - Telef10 İşbirliği ile")
