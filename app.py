import streamlit as st

# ==== CONFIGURACIÓN GENERAL ====
st.set_page_config(page_title="Portafolio de Zuleika", layout="wide")

# ==== DATOS ====
info = {
   "Pronoun": "ella", 
   "Name": "Zuleika",
   "Full_Name": "Zuleika Maytte Napuri Chinga",
   "Intro": "✨ Comunicadora, publicista y apasionada por la creatividad, la tecnología y el impacto social ✨",
   "About": "💖 ¡Hola! Soy Zuleika y me interesa crear experiencias significativas a través de la comunicación, el diseño y las herramientas digitales. Creo en el poder de las ideas y la innovación para transformar realidades. Este portafolio es un espacio para mostrar lo que hago, cómo pienso y lo que quiero seguir construyendo. 💡✨",
   "City": "🇵🇪 Lima, Perú",
   "Photo": """<a href='https://www.linkedin.com/in/zuleika-maytte-napuri-chinga-227172363/'><img src='https://i.imgur.com/h1myKrJ.png' width='200' alt='Zuleika'></a>""",
   "Email": "zuleikanapuri8@gmail.com"
}

endorsements = {
    "img1": "https://i.imgur.com/Ijd7Kpf.jpeg",
    "img2": "https://i.imgur.com/RM31sfq.jpeg",
    "img3": "https://i.imgur.com/p1KQB0n.jpeg"
}

# ==== ESTILOS PERSONALIZADOS ====
st.markdown("""
    <style>
        body {
            background-color: #fff8f4;
        }
        h1, h2, h3, h4 {
            color: #9c27b0;
            font-family: 'Comic Sans MS', cursive, sans-serif;
        }
        .stSubheader, .stText {
            color: #6a1b9a;
        }
        a {
            color: #ba68c8;
            text-decoration: none;
        }
        .emoji {
            font-size: 24px;
        }
    </style>
""", unsafe_allow_html=True)

# ==== MENÚ DE NAVEGACIÓN EN BARRA LATERAL ====
with st.sidebar:
    st.image("https://i.imgur.com/h1myKrJ.png", width=150)
    st.markdown(f"### {info['Full_Name']}")
    st.markdown(info["Intro"])
    st.markdown("---")
    menu = ["Inicio", "Experiencia", "Habilidades", "Logros", "Galería", "Contacto"]
    choice = st.radio("📌 Navega por el portafolio:", menu)

# ==== INICIO ====
if choice == "Inicio":
    st.markdown(f"<h1 style='text-align: center;'>{info['Full_Name']} 👩‍🎨</h1>", unsafe_allow_html=True)
    st.markdown(f"<h4 style='text-align: center;'>{info['Intro']}</h4>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align:center'>{info['Photo']}</div>", unsafe_allow_html=True)

    with st.container():
        st.subheader("📖 Sobre mí")
        st.markdown(info["About"])

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"🌆 **Ciudad:** {info['City']}")
        with col2:
            st.markdown(f"📧 **Email:** [{info['Email']}](mailto:{info['Email']})")

# ==== EXPERIENCIA ====
elif choice == "Experiencia":
    with st.container():
        st.subheader("💼 Experiencia laboral")
        with st.expander("Ver detalles"):
            st.write("""
            🔹 Asistente de comunicaciones en iniciativas culturales y sociales  
            🔹 Voluntariados en proyectos comunitarios  
            🔹 Gestión de contenidos y diseño para redes sociales
            """)

        st.subheader("🎯 Objetivo profesional")
        st.write("""
        Aplicar la comunicación estratégica, el diseño y la tecnología para impulsar proyectos con sentido, propósito e impacto positivo en la sociedad.
        """)

# ==== HABILIDADES ====
elif choice == "Habilidades":
    with st.container():
        st.subheader("🧑‍💻 Habilidades")
        with st.expander("Ver habilidades técnicas y blandas"):
            st.write("""
            🔹 Comunicación estratégica  
            🔹 Creatividad publicitaria  
            🔹 Storytelling  
            🔹 Diseño gráfico, redacción y Canva  
            🔹 Herramientas digitales y redes sociales
            """)

        st.subheader("📚 Certificaciones")
        st.write("""
        🎓 Curso de Comunicación Digital en PUCP (2023)  
        🗓️ Certificación en Marketing y Comunicaciones con COREPUCP
        """)

# ==== LOGROS ====
elif choice == "Logros":
    with st.container():
        st.subheader("🏆 Logros")
        st.write("""
        🔹 Coordinó campañas universitarias con enfoque inclusivo y social  
        🔹 Participó en iniciativas estudiantiles que aumentaron el alcance cultural
        """)

        st.subheader("💡 Fortalezas")
        st.write("Zuleika destaca por su empatía, creatividad, sensibilidad social y uso de herramientas comunicativas con propósito.")

        st.subheader("⚠️ Debilidades")
        st.write("Es exigente consigo misma y revisa mucho antes de compartir, pero eso asegura calidad y coherencia.")

# ==== GALERÍA ====
elif choice == "Galería":
    with st.container():
        st.subheader("🖼️ Testimonios visuales")
        cols = st.columns(3)
        cols[0].image(endorsements["img1"], use_column_width=True)
        cols[1].image(endorsements["img2"], use_column_width=True)
        cols[2].image(endorsements["img3"], use_column_width=True)

# ==== CONTACTO ====
elif choice == "Contacto":
    with st.container():
        st.subheader("📬 Disponibilidad")
        st.write("Abierta a nuevas oportunidades creativas, sociales o culturales con visión innovadora.")

        st.subheader("📄 Referencias")
        st.write("Referencias disponibles a solicitud. 😊")
