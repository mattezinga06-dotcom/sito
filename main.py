import base64
import datetime
import streamlit as st


# Funzione per convertire l'immagine in un formato sicuro per lo sfondo
def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


# Prova a caricare lo sfondo, se non lo trova usa il rosa di riserva
try:
    bin_str = get_base64_of_bin_file("sfondo.jpg")
    bg_css = f"""
    .stApp {{
        background-image: linear-gradient(rgba(255, 240, 245, 0.85), rgba(255, 240, 245, 0.85)), url("data:image/jpg;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    """
except:
    bg_css = ".stApp { background-color: #fff0f5; }"

# Configurazione della pagina
st.set_page_config(page_title="tana di matte&clo", layout="centered")

# --- STILE E SFONDO ---
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

    {bg_css}

    h1, h2, h3 {{
        color: #d63384 !important;
        font-family: 'Poppins', sans-serif;
    }}
    p, label, .stRadio, .stTextInput {{
        font-family: 'Poppins', sans-serif;
    }}
    .stButton>button {{
        background-color: #ff4b4b;
        color: white;
        border-radius: 20px;
        border: none;
        padding: 10px 24px;
        font-weight: bold;
        font-family: 'Poppins', sans-serif;
    }}
    .stButton>button:hover {{
        background-color: #e03e3e;
        color: white;
    }}
    
    .counter-box {{
        background: linear-gradient(135deg, #ff758c 0%, #ff7eb3 100%);
        padding: 22px;
        border-radius: 18px;
        text-align: center;
        box-shadow: 0 6px 15px rgba(255, 117, 140, 0.3);
        margin-top: 10px;
        margin-bottom: 20px;
    }}
    .counter-text {{
        font-family: 'Poppins', sans-serif;
        font-size: 22px;
        font-weight: 600;
        color: white;
        letter-spacing: 0.5px;
        text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# --- 1. SEGRETO / PASSWORD DI ACCESSO ---
PASSWORD_CORRETTA = "MOLLY"


def check_password():
    if "autenticato" not in st.session_state:
        st.session_state["autenticato"] = False

    if not st.session_state["autenticato"]:
        st.title("Area Riservata, accesso negato a tutti tranne il mio pulcino")
        st.write(
            "Inserisci la password per entrare (indizio: la nostra gallinella preferita)"
        )
        pwd = st.text_input("Password", type="password")

        if st.button("Entra"):
            # Controllo rigoroso senza .lower(), serve esattamente MOLLY
            if pwd == PASSWORD_CORRETTA:
                st.session_state["autenticato"] = True
                st.rerun()
            else:
                st.error(
                    "suca l'ho fatto apposta a farti sbagliare solo per darti fastidio 😛, prova con: MOLLY"
                )
                st.image("IMG_5808.jpg", width=400)
                st.write("tu ora")
        return False
    return True


if check_password():

    # --- INTESTAZIONE ---
    st.title("per la mia tatina")
    st.write(
        "ciao pulce, ho creato (io e il signor gemini) questo piccolo spazio solo per noi, per ricordarti quanto ti amo."
        " Per ora ho messo un po di cosine che riguardano noi più qualche giochino"
        ". Ho preferito fare una cosina così tata perchè sono sicuro che mi venga molto meglio di qualcosa di fisico"
    )

    st.divider()

    # --- 2. CONTATORE DEL TEMPO INSIEME AL SECONDO ---
    st.header("⏳ Da quanto tempo ci amiamo?")

    anno, mese, giorno, ora, minuto = 2025, 1, 26, 14, 30

    js_code = f"""
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap" rel="stylesheet">
    <style>
        .counter-box {{
            background: linear-gradient(135deg, #ff758c 0%, #ff7eb3 100%);
            padding: 22px;
            border-radius: 18px;
            text-align: center;
            box-shadow: 0 6px 15px rgba(255, 117, 140, 0.3);
            margin-top: 10px;
            margin-bottom: 20px;
        }}
        .counter-text {{
            font-family: 'Poppins', sans-serif;
            font-size: 22px;
            font-weight: 600;
            color: white;
            letter-spacing: 0.5px;
            text-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
    </style>

    <div class="counter-box">
        <div class="counter-text" id="timer">Caricamento...</div>
    </div>

    <script>
    var startDate = new Date({anno}, {mese - 1}, {giorno}, {ora}, {minuto}, 0).getTime();

    function updateTimer() {{
        var now = new Date().getTime();
        var distance = now - startDate;

        var days = Math.floor(distance / (1000 * 60 * 60 * 24));
        var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        var seconds = Math.floor((distance % (1000 * 60)) / 1000);

        document.getElementById("timer").innerHTML = 
            days + "g , " + hours + "h, " + minutes + "min, " + seconds + "s";
    }}

    setInterval(updateTimer, 1000);
    updateTimer();
    </script>
    """

    st.components.v1.html(js_code, height=95)

    st.write("(in realtà ci amavamo anche da prima di renderlo ufficiale)<br>in teoria il timer doveva essere circa messo verso le tre ma sto coso di merda sta facendo tutto di testa sua", unsafe_allow_html=True)

    st.divider()

# --- FOTO DA SCOPRIRE CON UN PULSANTE SOTTO ---
    st.header("In tutto questo tempo siamo anche diventati genitoriiii!!!!")
    st.markdown("<br>", unsafe_allow_html=True)

    if "foto_svelata" not in st.session_state:
        st.session_state["foto_svelata"] = False

    # Mostra l'immagine corretta in base allo stato
    if not st.session_state["foto_svelata"]:
        st.image(
            "d597291c-df62-4386-a47a-a45ef554f1f1.JPG",
            use_container_width=True,
        )
        if st.button("Clicca per vedere i nostri figli!", use_container_width=True):
            st.session_state["foto_svelata"] = True
            st.rerun()
    else:
        st.image(
            "8b41fd8b-1631-44b6-bda2-8e6e5f3aa7c9.JPG",
            use_container_width=True,
        )
        st.write("CHE BELLINI SONOOOOOOOOO")
        if st.button("Copri di nuovo", use_container_width=True):
            st.session_state["foto_svelata"] = False
            st.rerun()

    st.divider()

    st.header("Un'ultima sorpresa...")
    if st.button("Clicca per un bacio virtuale"):
        st.success("Muuuuaaaah! Ti amo bimbaaaaa! ❤️❤️")

    st.divider()

    st.write("ultima modifica 24/08/2026, e sicuramente non l'ultima...")

# --- GIOCO: I 25 MOTIVI DA SVELARE UNO A UNO ---
    st.header("25 cose che amo di te")

    # Lista dei 25 motivi (le tue frasi originali)
    motivi_25 = [
        "1. il sorrisone.",
        "2. sei dolcissima (solo con me).",
        "3. a entrambi piacciono le macchine!!! (godo la 6h).",
        "4. hai un fisico della madonna.",
        "5. ti prendi cura di me visto che sono un pasticcione.",
        "6. mi manchi subito come ci allontaniamo.",
        "7. sei una topazza incredibile.",
        "8. amo il tuo profumo (tranne quando puzzi di kebab con la cipolla).",
        "9. sei intelligentissima.",
        "10. quando facciamo cose che non mi piacciono sono comunque felice perchè sono con te.",
        "11. i tuoi capelli sono bellissimi (soprattutto lisci).",
        "12. siamo complici in crimini.",
        "13. mi diverto troppo con te.",
        "14. eh vabbè le big scopate.",
        "15. amo dormire con te tutti appiccicati (tranne nel mio letto).",
        "16. la tua creatività.",
        "17. tutte le cose che fai con quelle manine.",
        "18. mi piace un sacco come ti vesti anche se nessuno batterà mai QUEI pantaloncini.",
        "19. sei la terza figlia dei miei.",
        "20. insieme mangiamo come due obesoni.",
        "21. sei tutta schiacciabile.",
        "22. culo.",
        "23. tette.",
        "24. scusa le voci hanno preso il sopravvento.",
        "25. gli occhioni",
    ]

    # Inizializza il contatore dei motivi svelati (parte da 0, quindi tutti coperti)
    if "svelati_count" not in st.session_state:
        st.session_state["svelati_count"] = 0

    # Pulsante per svelare il prossimo
    if st.session_state["svelati_count"] < len(motivi_25):
        if st.button("clicca quiii", width="stretch"):
            st.session_state["svelati_count"] += 1
            st.rerun()
    else:
        st.success("Li hai svelati tutti! Sei ufficialmente la mia pulce. SIUUUUUUU")

    # Mostra la lista aggiornata: i svelati colorati, i bloccati con il lucchetto
    for i, motivo in enumerate(motivi_25):
        if i < st.session_state["svelati_count"]:
            # Motivo svelato (con il gradiente rosa)
            st.markdown(
                f"""
            <div style="background: linear-gradient(135deg, #ff758c 0%, #ff7eb3 100%); padding: 14px 18px; border-radius: 12px; margin-bottom: 10px; box-shadow: 0 3px 8px rgba(255, 117, 140, 0.2);">
                <p style="font-family: 'Poppins', sans-serif; font-size: 16px; font-weight: 600; color: white; margin: 0;">
                    {motivo}
                </p>
            </div>
            """,
                unsafe_allow_html=True,
            )
        else:
            # Motivo ancora bloccato (grigio/misterioso)
            st.markdown(
                f"""
            <div style="background-color: #fce4ec; padding: 12px 18px; border-radius: 12px; margin-bottom: 10px; border: 2px dashed #f8bbd0;">
                <p style="font-family: 'Poppins', sans-serif; font-size: 15px; color: #ad1457; margin: 0;">
                    🔒 Motivo n. {i + 1} — <i>Ancora da svelare...</i>
                </p>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.divider()


    # --- GIF ANIMATA FINALE (METODO SICURO BASE64) ---
    st.write("ultima modifica 30/08/2026, e sicuramente non l'ultima...")
    import base64

    def gif_to_base64(file_path):
        try:
            with open(file_path, "rb") as f:
                return base64.b64encode(f.read()).decode()
        except Exception:
            return ""

    gif_b64 = gif_to_base64("kOnzy.gif")

    st.markdown(
        f"""
    <div style="text-align: center; margin-top: 20px;">
        <img src="data:image/gif;base64,{gif_b64}" width="180" style="border-radius: 10px;">
    </div>
    """,
        unsafe_allow_html=True,
    )

##DA AGGIUNGERE: VIAGGI ASSIEME e esperienze, COSE CHE MI PIACCIONO DI TE, ALTRI GIOCHI
