import streamlit as st
import swisseph as swe
import datetime
import time
from PIL import Image
import numpy as np

# പേജ് സെറ്റിംഗ്സ്
st.set_page_config(page_title="UTA Astrology & Wellness", layout="centered")

# പാസ്‌വേഡ് സെക്ഷൻ
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state.password_correct = False
    
    if st.session_state.password_correct:
        return True
    
    col_l1, col_l2, col_l3 = st.columns([1, 2, 1])
    with col_l2:
        try:
            logo = Image.open('image_2.png (2).jpg')
            st.image(logo, width=200)
        except:
            st.title("🌟 Pradeep Nair")
            
    st.markdown("<h2 style='text-align: center;'>🔐 Astro Digital Wellness Login</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; font-style: italic; color: #1a237e; font-weight: bold;'>\"നിങ്ങളുടെ ഭാവി നിങ്ങൾ തീരുമാനിക്കും\"</p>", unsafe_allow_html=True)
    
    col_p1, col_p2, col_p3 = st.columns([1, 2, 1])
    with col_p2:
        password = st.text_input("Password:", type="password")
        if st.button("Login", use_container_width=True):
            if password == "pradeep": 
                st.session_state.password_correct = True
                st.rerun()
            else:
                st.error("Incorrect Password!")
    return False

if check_password():
    try:
        logo = Image.open('image_2.png (2).jpg')
        st.sidebar.image(logo, use_container_width=True)
    except:
        pass

    # CSS സ്റ്റൈലുകൾ
    st.markdown("""
        <style>
        .charts-container { display: flex; flex-wrap: wrap; justify-content: space-between; gap: 20px; margin: 20px auto; }
        .chart-box { flex: 1; min-width: 300px; text-align: center; }
        .rashi-table { width: 100%; border-collapse: collapse; border: 4px solid #1a237e; table-layout: fixed; background-color: white; }
        .rashi-td { border: 2px solid #1a237e; height: 85px; text-align: center; vertical-align: middle; font-size: 13px; font-weight: bold; color: #1a237e; }
        .empty-td { background-color: #f8f9fa; border: 2px solid #1a237e; }
        .pred-box { padding: 15px; border-radius: 12px; margin-top: 10px; font-size: 16px; line-height: 1.6; }
        .strength { background-color: #e8f5e9; border: 1px solid #4caf50; color: #1b5e20; padding: 12px; border-radius: 8px; margin-bottom: 10px; }
        .caution { background-color: #ffebee; border: 1px solid #ef5350; color: #b71c1c; padding: 12px; border-radius: 8px; }
        .shani-alert-box { background-color: #ede7f6; border: 2px solid #673ab7; padding: 15px; border-radius: 10px; margin: 15px 0; font-size: 16px; color: #4a148c; }
        .info-pill { background-color: #f1f3f4; border: 1px solid #dadce0; padding: 5px 15px; border-radius: 15px; display: inline-block; margin-right: 10px; font-weight: bold; color: #202124; }
        .current-dasha-box { background-color: #fff9c4; border: 2px dashed #fbc02d; padding: 15px; border-radius: 10px; margin: 15px 0; font-size: 16px; color: #f57f17; }
        
        .jatakam-table { width: 100%; border-collapse: collapse; margin: 20px 0; font-size: 16px; font-family: sans-serif; }
        .jatakam-table td { padding: 10px; border-bottom: 1px solid #ddd; vertical-align: top; }
        .jatakam-key { font-weight: bold; color: #1a237e; width: 40%; }
        .jatakam-val { color: #333; }

        .porutham-box { background-color: #e3f2fd; border: 2px solid #1e88e5; padding: 15px; border-radius: 10px; margin: 15px 0; font-size: 16px; color: #0d47a1; }
        .cesarean-box { background-color: #fff3e0; border: 2px solid #ff9800; padding: 15px; border-radius: 10px; margin: 15px 0; font-size: 16px; color: #e65100; }
        </style>
        """, unsafe_allow_html=True)

    swe.set_sid_mode(swe.SIDM_LAHIRI)
    
    st.header("📋 Personal Details")
    name = st.text_input("പേര്:")
    
    st.write("**ജനന തീയതി സെലക്ട് ചെയ്യുക:**")
    c_d1, c_d2, c_d3 = st.columns(3)
    with c_d1: input_day = st.selectbox("തീയതി (Day)", range(1, 32), index= datetime.date.today().day - 1)
    with c_d2: input_month = st.selectbox("മാസം (Month)", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"], index=datetime.date.today().month - 1)
    with c_d3: input_year = st.number_input("വർഷം (Year)", min_value=1900, max_value=2050, value=datetime.date.today().year)
    
    months_map = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9, "October":10, "November":11, "December":12}
    sel_month_num = months_map[input_month]
    
    try:
        dob = datetime.date(int(input_year), sel_month_num, int(input_day))
    except ValueError:
        st.error("⚠️ തെറ്റായ തീയതിയാണ് നൽകിയിരിക്കുന്നത്! ദയവായി പരിശോധിക്കുക.")
        dob = datetime.date.today()

    c_t1, c_t2, c_t3 = st.columns(3)
    with c_t1: hr = st.selectbox("Hr", range(1, 13))
    with c_t2: mi = st.selectbox("Min", range(60))
    with c_t3: ap = st.selectbox("AM/PM", ["AM", "PM"])

    DISTRICTS = {
        "Thiruvananthapuram": (8.5241, 76.9366),
        "Kochi (Cochin)": (9.9312, 76.2673),
        "Kozhikode": (11.2588, 75.7804),
        "Thrissur": (10.5276, 76.2144),
        "Kollam": (8.8932, 76.6141),
        "Kottayam": (9.5916, 76.5222),
        "Alappuzha": (9.4981, 76.3388),
        "Palakkad": (10.7867, 76.6547),
        "Malappuram": (11.0510, 76.0711),
        "Kannur": (11.8745, 75.3704)
    }
    birth_place = st.selectbox("ജനന സ്ഥലം (ജില്ല):", list(DISTRICTS.keys()))

    MAL_NAK = ["അശ്വതി", "ഭരണി", "കാർത്തിക", "രോഹിണി", "മകയിരം", "തിരുവാതിര", "പുണർതം", "പൂയം", "ആയില്യം", "മകം", "പൂരം", "ഉത്രം", "അത്തം", "ചിത്ര", "ചോതി", "വിശാഖം", "അനിഴം", "തൃക്കേട്ട", "മൂലം", "പൂരാടം", "ഉത്രാടം", "തിരുവോണം", "അവിട്ടം", "ചതയം", "പൂരുരുട്ടാതി", "ഉത്രട്ടാതി", "രേവതി"]

    # 1. പങ്കാളി പൊരുത്ത പരിശോധന (18 വയസ്സിന് മുകളിൽ ഉള്ളവർക്ക്)
    today = datetime.date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    
    partner_nak_selected = None
    if age >= 18:
        st.markdown("---")
        st.subheader("💑 പങ്കാളി പൊരുത്ത പരിശോധന (Optional)")
        check_compatibility = st.checkbox("ഭാര്യയുടെ / ഭർത്താവിന്റെ (പങ്കാളിയുടെ) നക്ഷത്ര പൊരുത്തം നോക്കണോ?")
        if check_compatibility:
            partner_nak_selected = st.selectbox("പങ്കാളിയുടെ നക്ഷത്രം സെലക്ട് ചെയ്യുക:", MAL_NAK)

    # 2. സിസേറിയൻ ബേബി ഓപ്ഷൻ (Option B) + മാതാപിതാക്കളുടെ നക്ഷത്രങ്ങൾ
    st.markdown("---")
    st.subheader("👶 ജനന രീതി പരിശോധന")
    is_cesarean = st.radio("നിങ്ങൾ ഒരു സിസേറിയൻ ബേബി (Cesarean Birth) ആണോ?", ["No", "Yes"])
    
    father_nak = None
    mother_nak = None
    if is_cesarean == "Yes":
        st.info("മാതാപിതാക്കളുടെ നക്ഷത്ര പൊരുത്തവും പിതൃദോഷ സൂചനയും കണക്കാക്കാൻ താഴെ പറയുന്ന വിവരങ്ങൾ നൽകുക:")
        c_f1, c_f2 = st.columns(2)
        with c_f1: father_nak = st.selectbox("അച്ഛന്റെ നക്ഷത്രം സെലക്ട് ചെയ്യുക:", MAL_NAK)
        with c_f2: mother_nak = st.selectbox("അമ്മയുടെ നക്ഷത്രം സെലക്ട് ചെയ്യുക:", MAL_NAK)

    st.markdown("---")
    st.subheader("💓 Step 0: Pulse Measurement")
    if st.button("⏱️ Start 1-Min Timer"):
        placeholder = st.empty()
        for seconds in range(60, 0, -1):
            placeholder.metric("Timer", f"{seconds} Sec Left")
            time.sleep(1)
        placeholder.success("Time Up! 🔔 പൾസ് താഴെ നൽകുക.")

    pulse = st.number_input("Pulse Rate:", value=72)
    
    st.markdown("---")
    st.subheader("✋ Step 1: Fingerprint Analysis")
    img_file = st.camera_input("വിരൽ ക്യാമറയിൽ അമർത്തി വെച്ച ശേഷം ഫോട്ടോ എടുക്കുക.")

    if "valid_fingerprint" not in st.session_state:
        st.session_state.valid_fingerprint = False

    if img_file:
        img = Image.open(img_file)
        img_array = np.array(img)
        avg_red = np.mean(img_array[:,:,0])
        avg_green = np.mean(img_array[:,:,1])
        
        if avg_red > avg_green + 10: 
            st.success("✅ Hand Print Captured Successfully!")
            st.session_state.valid_fingerprint = True
        else:
            st.warning("⚠️ വിരൽ ക്യാമറയിൽ അമർത്തി വെച്ച ശേഷം മാത്രം ഫോട്ടോ എടുക്കുക.")
            st.session_state.valid_fingerprint = False

    if "show_report" not in st.session_state:
        st.session_state.show_report = False

    if st.session_state.valid_fingerprint:
        if st.button("Generate Final Report"):
            if not name: 
                st.error("ദയവായി പേര് നൽകുക!")
            else:
                st.session_state.show_report = True

    if st.session_state.show_report and name:
        try:
            h = hr
            if ap == "PM" and h != 12: h += 12
            elif ap == "AM" and h == 12: h = 0
            t_ut = (h + mi/60.0) - 5.5
            jd = swe.julday(dob.year, dob.month, dob.day, t_ut)

            lat, lon = DISTRICTS[birth_place]

            res_moon, _ = swe.calc_ut(jd, swe.MOON, swe.FLG_SIDEREAL)
            nak_long = res_moon[0]
            nak_idx = int(nak_long / (13.333333)) % 27
            nak_number = nak_idx + 1 
            shareera_sankhya = (dob.year + pulse) * nak_number

            STRENGTHS = ["ഊർജ്ജസ്വലത", "ധൈര്യം", "സ്ഥിരബുദ്ധി", "സത്യസന്ധത", "ബുദ്ധിശക്തി", "പെട്ടെന്നുള്ള ചിന്ത", "ദയ", "മറ്റുള്ളവരെ സഹായിക്കാനുള്ള മനസ്സ്", "അറിവ്", "നേതൃപാടവം", "സ്നേഹം", "ക്ഷമ", "കഠിനാധ്വാനം", "കലാപരമായ കഴിവ്", "സ്വാതന്ത്ര്യം", "ലക്ഷ്യബോധം", "ഭക്തി", "തന്ത്രപരമായ ചിന്ത", "ആത്മീയത", "സമാധാനം", "ആദർശങ്ങൾ", "ചിട്ടയായ ജീവിതം", "ധീരത", "പരസഹായം", "വിശ്വസ്തത", "ശാന്തത", "മൃദുഭാഷണം"]
            CAUTIONS = ["ധൃതി", "പിടിവാശി", "പെട്ടെന്നുള്ള ദേഷ്യം", "അമിത ചിന്ത", "അസ്ഥിരത", "വൈകാരികമായ എടുത്തുചാട്ടം", "സംശയം", "അമിത ഉത്കണ്ഠ", "പക", "അഹങ്കാരം", "സങ്കടപ്പെടാനുള്ള പ്രവണത", "മടി", "ആത്മവിശ്വാസക്കുറവ്", "മറ്റുള്ളവരുടെ കാര്യത്തിൽ ഇടപെടൽ", "ഭയം", "അമിത ചെലവ്", "ഏകാന്തത", "മത്സരബുദ്ധി", "സംശയം", "ചഞ്ചലമനസ്സ്", "പിടിവാശി", "അലസത", "രഹസ്യസ്വഭാവം", "അശ്രദ്ധ", "ഭ്രമം", "വേവലാതി", "ആശങ്ക"]
            
            PLANETS = {swe.SUN: "സൂ", swe.MOON: "ച", swe.MARS: "ചൊ", swe.MERCURY: "ബു", swe.JUPITER: "വ്യാ", swe.VENUS: "ശു", swe.SATURN: "ശ"}
            rashi_names = ["മേടം", "ഇടവം", "മിഥുനം", "കർക്കിടകം", "ചിങ്ങം", "കന്നി", "തുലാം", "വൃശ്ചികം", "ധനു", "മകരം", "കുംഭം", "മീനം"]
            
            cusps, ascmc = swe.houses_ex(jd, lat, lon, b'P', swe.FLG_SIDEREAL)
            lagnam_rashi = rashi_names[int(ascmc[0]/30)]
            moon_rashi_idx = int(res_moon[0]/30)
            moon_rashi = rashi_names[moon_rashi_idx]

            res_sun, _ = swe.calc_ut(jd, swe.SUN, swe.FLG_SIDEREAL)
            sun_long = res_sun[0]
            mal_month_idx = int(sun_long / 30)
            mal_month_name = rashi_names[mal_month_idx]
            mal_date = int(sun_long % 30) + 1
            mal_year = dob.year - 824
            if dob.month < 8 or (dob.month == 8 and dob.day < 15):
                mal_year -= 1

            # പകൽ / രാത്രി ജനനം കണ്ടെത്തുന്നു (6 AM to 6 PM പകൽ, ബാക്കി രാത്രി)
            is_day_birth = True if 6 <= h < 18 else False
            birth_time_type = "പകൽ" if is_day_birth else "രാത്രി"

            st.markdown("---")
            st.markdown(f"### 📋 Wellness Report: {name}")
            st.markdown(f"""
            <div style='margin-bottom: 15px;'>
                <span class='info-pill'>📅 Year: {dob.year}</span>
                <span class='info-pill'>💓 Pulse: {pulse}</span>
                <span class='info-pill'>🔢 നക്ഷത്ര സംഖ്യ: {nak_number}</span>
                <span class='info-pill' style='background-color: #ffd700; color: #000; border: 2px solid #b8860b;'>🧬 ശരീര സംഖ്യ: {shareera_sankhya}</span>
            </div>
            """, unsafe_allow_html=True)
            
            # 📜 ജാതക വിവരങ്ങൾ
            st.markdown("#### 📜 ജാതക വിവരങ്ങൾ (Horoscope Details)")
            birth_time = f"{hr}:{mi:02d} {ap}"
            days_of_week = ["തിങ്കൾ", "ചൊവ്വ", "ബുധൻ", "വ്യാഴം", "വെള്ളി", "ശനി", "ഞായർ"]
            weekday_name = days_of_week[dob.weekday()]

            html_jatakam = f"""
            <table class="jatakam-table">
                <tr><td class="jatakam-key">പേര്</td><td class="jatakam-val">: {name}</td></tr>
                <tr><td class="jatakam-key">ജനനത്തീയതി, ആഴ്ച</td><td class="jatakam-val">: {dob.strftime('%d/%m/%Y')}, {weekday_name}</td></tr>
                <tr><td class="jatakam-key">ജനനസമയം</td><td class="jatakam-val">: {birth_time} ({birth_time_type} ജനനം)</td></tr>
                <tr><td class="jatakam-key">ജനനസ്ഥലം</td><td class="jatakam-val">: {birth_place.upper()}, KERALAM</td></tr>
                <tr><td class="jatakam-key">ഭാരതീയ ജനനദിവസം</td><td class="jatakam-val">: കൊല്ലവർഷം {mal_year} {mal_month_name} {mal_date}, {weekday_name}</td></tr>
                <tr><td class="jatakam-key">നക്ഷത്രം</td><td class="jatakam-val">: {MAL_NAK[nak_idx]}</td></tr>
                <tr><td class="jatakam-key">ലഗ്നരാശി</td><td class="jatakam-val">: {lagnam_rashi}</td></tr>
                <tr><td class="jatakam-key">ചന്ദ്രരാശി</td><td class="jatakam-val">: {moon_rashi}</td></tr>
            </table>
            """
            st.markdown(html_jatakam, unsafe_allow_html=True)
            st.markdown("---")

            # =========================================================
            # 🪐 ശനിദോഷ പരിശോധന + പകൽ/രാത്രി ആശ്വാസ ലോജിക്
            # =========================================================
            st.markdown("#### 🪐 ശനിദോഷ പരിശോധന (Saturn Transit Analysis)")
            
            relief_msg = ""
            if is_day_birth:
                relief_msg = "<br><br>💡 <b>ഒരു വലിയ ആശ്വാസം:</b> നിങ്ങൾ <b>പകൽ സമയത്ത്</b> ജനിച്ചതുകൊണ്ട് തന്നെ, ജ്യോതിഷ ശാസ്ത്രപ്രകാരം ശനിയുടെ ദോഷ കാഠിന്യം നിങ്ങളുടെ ജീവിതത്തെ അമിതമായി ബാധിക്കുകയില്ല. ദോഷങ്ങളുടെ തീവ്രത വളരെ കുറവായിരിക്കും!"
            else:
                relief_msg = "<br><br>ℹ️ നിങ്ങൾ <b>രാത്രി സമയത്ത്</b> ജനിച്ചതുകൊണ്ട് തന്നെ, ശനിദോഷ കാലങ്ങളിൽ അല്പം കൂടുതൽ ശ്രദ്ധ പുലർത്തുന്നതും ഈശ്വരപ്രാർത്ഥനകൾ നടത്തുന്നതും നന്നായിരിക്കും."

            today_jd = swe.julday(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day, 12.0)
            res_saturn, _ = swe.calc_ut(today_jd, swe.SATURN, swe.FLG_SIDEREAL)
            saturn_rashi_idx = int(res_saturn[0] / 30)
            saturn_rashi_name = rashi_names[saturn_rashi_idx]
            
            diff = (saturn_rashi_idx - moon_rashi_idx) % 12
            
            shani_status = "🟢 ഇപ്പോൾ നിങ്ങൾക്ക് ശനിയുടെ ദോഷകാലങ്ങൾ (ഏഴരശനി/കണ്ടകശനി) നിലവിലില്ല. ശുഭകരം!"
            advice = "സാധാരണ രീതിയിലുള്ള പ്രാർത്ഥനകൾ തുടരുക."
            
            if diff == 11:
                shani_status = f"⚠️ <b>നിങ്ങൾക്ക് ഇപ്പോൾ ഏഴരശനി ആരംഭിച്ചിട്ടുണ്ട് (ജന്മശനിക്ക് മുൻപുള്ള രാശിയിൽ)!</b> ശനി ഇപ്പോൾ നിൽക്കുന്നത് {saturn_rashi_name} രാശിയിലാണ്."
                advice = "ശനിയാഴ്ചകളിൽ ശാസ്താവിന് നീരാജനം അർപ്പിക്കുന്നത് ദോഷശമനത്തിന് ഉത്തമമാണ്."
            elif diff == 0:
                shani_status = f"🚨 <b>നിങ്ങൾക്ക് ഇപ്പോൾ ജന്മശനിയാണ് (ഏഴരശനിയുടെ മധ്യഘട്ടം)!</b> ശനി നിങ്ങളുടെ ചന്ദ്രരാശിയായ {saturn_rashi_name}-ൽ തന്നെ തുടരുന്നു."
                advice = "അനാവശ്യ കൂട്ടുകെട്ടുകളും എടുത്തുചാട്ടങ്ങളും ഒഴിവാക്കുക. ഹനുമാൻ ചാലീസ ജപിക്കുന്നത് നല്ലതാണ്."
            elif diff == 1:
                shani_status = f"⚠️ <b>നിങ്ങൾക്ക് ഇപ്പോൾ ഏഴരശനിയുടെ അവസാന ഘട്ടമാണ് (ഇറക്ക ശനി)!</b> ശനി ഇപ്പോൾ നിൽക്കുന്നത് {saturn_rashi_name} രാശിയിലാണ്."
                advice = "കഠിനാധ്വാനത്തിന് ഫലം ലഭിക്കുന്ന സമയമാണ്. ഈശ്വരപ്രാർത്ഥന കൈവിടരുത്."
            elif diff == 3: 
                shani_status = f"⚡ <b>നിങ്ങൾക്ക് ഇപ്പോൾ കണ്ടകശനി (4-ാം ഭാവം) നടക്കുകയാണ്!</b> ശനി ഇപ്പോൾ നിൽക്കുന്നത് {saturn_rashi_name} രാശിയിലാണ്."
                advice = "യാത്രകളിൽ കൂടുതൽ ശ്രദ്ധിക്കുക. കുടുംബത്തിൽ വിട്ടുവീഴ്ചകൾ ചെയ്യുക."
            elif diff == 6: 
                shani_status = f"⚡ <b>നിങ്ങൾക്ക് ഇപ്പോൾ കണ്ടകശനി (7-ാം ഭാവം) നടക്കുകയാണ്!</b> ശനി ഇപ്പോൾ നിൽക്കുന്നത് {saturn_rashi_name} രാശിയിലാണ്."
                advice = "കൂട്ടുകച്ചവടങ്ങളിലും ബിസിനസ്സിലും ശ്രദ്ധിക്കുക. പങ്കാളിയുമായി നല്ല ബന്ധം പുലർത്തുക."
            elif diff == 9: 
                shani_status = f"⚡ <b>നിങ്ങൾക്ക് ഇപ്പോൾ കണ്ടകശനി (10-ാം ഭാവം - കർമ്മശനി) നടക്കുകയാണ്!</b> ശനി ഇപ്പോൾ നിൽക്കുന്നത് {saturn_rashi_name} രാശിയിലാണ്."
                advice = "തൊഴിൽ രംഗത്ത് കൂടുതൽ ശ്രദ്ധയും ക്ഷമയും ആവശ്യമാണ്. മേലുദ്യോഗസ്ഥരുമായി തർക്കങ്ങൾ ഒഴിവാക്കുക."

            final_relief = relief_msg if diff in [11, 0, 1, 3, 6, 9] else ""

            st.markdown(f"""
            <div class="shani-alert-box">
                🎯 {shani_status}<br><br>
                💡 <b>പരിഹാര നിർദ്ദേശം:</b> {advice} {final_relief}
            </div>
            """, unsafe_allow_html=True)
            st.markdown("---")

            # =========================================================
            # 👶 സിസേറിയൻ + അച്ഛനമ്മമാരുടെ പിതൃദോഷ ലോജിക്
            # =========================================================
            if is_cesarean == "Yes" and father_nak and mother_nak:
                st.markdown("#### 🧬 ജനന രീതിയും മാതാപിതാക്കളുടെ പൊരുത്തവും")
                f_idx = MAL_NAK.index(father_nak)
                m_idx = MAL_NAK.index(mother_nak)
                parent_distance = (f_idx - m_idx) % 27
                
                # യോനി, വശ്യ പൊരുത്തം സിമുലേഷൻ
                has_yoni_porutham = True if parent_distance % 2 != 0 else False
                has_vashya_porutham = True if parent_distance % 3 != 0 else False
                
                cesarean_report_msg = ""
                if not has_yoni_porutham or not has_vashya_porutham:
                    cesarean_report_msg = (
                        "⚠️ <b>പിതൃദോഷ സൂചന:</b> മാതാപിതാക്കളുടെ നക്ഷത്രങ്ങൾ തമ്മിൽ വശ്യം / യോനി പൊരുത്തങ്ങളുടെ കുറവ് കാണിക്കുന്നതിനാൽ, "
                        "നിങ്ങൾ ജനിക്കേണ്ട സാധാരണ സമയത്തിന് വ്യത്യാസം ഉണ്ടാകാൻ സാധ്യതയുണ്ടായിരുന്നു. കുടുംബത്തിലെ ഈ പിതൃദോഷ സ്വാധീനം കൊണ്ടാണ് "
                        "പ്രകൃതിദത്തമായ പ്രസവ സമയത്തിൽ മാറ്റം വരികയും, ശസ്ത്രക്രിയയിലൂടെ (Cesarean) ജനനം നടക്കുകയും ചെയ്തത്."
                    )
                else:
                    cesarean_report_msg = (
                        "✅ <b>ശുഭസൂചന:</b> മാതാപിതാക്കളുടെ നക്ഷത്രങ്ങൾ തമ്മിൽ കൃത്യമായ പൊരുത്തങ്ങൾ ഉള്ളതുകൊണ്ട് തന്നെ, "
                        "പിതൃദോഷങ്ങൾ മാറിപ്പോകുകയും ദോഷങ്ങളുടെ തീവ്രത കുറയുകയും ചെയ്യുന്നു. സിസേറിയൻ ജനനമായിരുന്നു എങ്കിൽ പോലും "
                        "അത് ദോഷകരമായി ബാധിക്കുകയില്ല."
                    )
                
                st.markdown(f"""
                <div class="cesarean-box">
                    🎯 <b>സിസേറിയൻ ജാതക വിശകലനം:</b><br><br>
                    {cesarean_report_msg}
                </div>
                """, unsafe_allow_html=True)
                st.markdown("---")

            # =========================================================
            # 💑 10 പൊരുത്തം മാച്ചിംഗ് ലോജിക് (പങ്കാളി ഓപ്ഷൻ സെലക്ട് ചെയ്താൽ മാത്രം)
            # =========================================================
            if partner_nak_selected:
                st.markdown("#### 💑 നക്ഷത്ര പൊരുത്ത ഫലം (10 Porutham Analysis)")
                p_idx = MAL_NAK.index(partner_nak_selected)
                
                distance = (p_idx - nak_idx) % 27
                matched_count = 0
                porutham_details = []
                
                poruthams = ["ദിനം", "ഗണം", "മഹേന്ദ്രം", "സ്ത്രീദീർഘം", "യോനി", "രാശി", "രാശ്യാധിപൻ", "വശ്യം", "രജ്ജു", "വേധം"]
                
                for index, p_name in enumerate(poruthams):
                    if (distance + index) % 3 != 0:
                        matched_count += 1
                        porutham_details.append(f"✅ {p_name} പൊരുത്തം: ഉണ്ട്")
                    else:
                        porutham_details.append(f"❌ {p_name} പൊരുത്തം: ഇല്ല")
                
                details_html = "<br>".join(porutham_details)
                st.markdown(f"""
                <div class="porutham-box">
                    🎯 <b>പങ്കാളിയുമായുള്ള പൊരുത്തം:</b> 10-ൽ {matched_count} പൊരുത്തങ്ങൾ ഉണ്ട്.<br><br>
                    <b>വിശദവിവരങ്ങൾ:</b><br>{details_html}
                </div>
                """, unsafe_allow_html=True)
                st.markdown("---")

            # =========================================================
            # ⏳ 120 വർഷത്തെ ഫുൾ ദശയും ഇൻസ്റ്റന്റ് ട്രാക്കിംഗ് ലോജിക്കും
            # =========================================================
            st.markdown("#### ⏳ ജന്മശിഷ്ട ദശയും അപഹാരങ്ങളും (Dasha & Apaharam)")
            
            DASHA_LORDS = ["കേതു", "ശുക്രൻ", "സൂര്യൻ", "ചന്ദ്രൻ", "ചൊവ്വ", "രാഹു", "വ്യാഴം", "ശനി", "ബുധൻ"]
            DASHA_YEARS = [7, 20, 6, 10, 7, 18, 16, 19, 17]
            
            lord_idx = nak_idx % 9
            total_years = DASHA_YEARS[lord_idx]
            
            deg_in_star = nak_long % 13.333333
            rem_fraction = (13.333333 - deg_in_star) / 13.333333
            
            rem_years = rem_fraction * total_years
            r_y = int(rem_years)
            r_m = int((rem_years - r_y) * 12)
            r_d = int((((rem_years - r_y) * 12) - r_m) * 30)
            
            st.info(f"**ജന്മശിഷ്ട ദശ:** {DASHA_LORDS[lord_idx]} ദശ — {r_y} വർഷം {r_m} മാസം {r_d} ദിവസം")
            
            birth_datetime = datetime.datetime(dob.year, dob.month, dob.day, h, mi)
            current_pointer = birth_datetime + datetime.timedelta(days=rem_years * 365.25)
            
            dasha_sequence = []
            dasha_sequence.append((DASHA_LORDS[lord_idx], birth_datetime, current_pointer))
            
            idx = (lord_idx + 1) % 9
            for _ in range(9):
                d_lord = DASHA_LORDS[idx]
                d_years = DASHA_YEARS[idx]
                end_pointer = current_pointer + datetime.timedelta(days=d_years * 365.25)
                dasha_sequence.append((d_lord, current_pointer, end_pointer))
                current_pointer = end_pointer
                idx = (idx + 1) % 9

            today_dt = datetime.datetime.now()
            running_dasha = "കണ്ടെത്താൻ കഴിഞ്ഞില്ല"
            running_apaharam = "കണ്ടെത്താൻ കഴിഞ്ഞില്ല"
            
            for d_lord, s_time, e_time in dasha_sequence:
                if s_time <= today_dt <= e_time:
                    running_dasha = d_lord
                    total_dasha_days = (e_time - s_time).days
                    apaharam_pointer = s_time
                    sub_idx = DASHA_LORDS.index(d_lord)
                    
                    for k in range(9):
                        ap_lord = DASHA_LORDS[(sub_idx + k) % 9]
                        ap_years = DASHA_YEARS[(sub_idx + k) % 9]
                        ap_days = (total_dasha_days * ap_years) / 120
                        ap_end = apaharam_pointer + datetime.timedelta(days=ap_days)
                        
                        if apaharam_pointer <= today_dt <= ap_end:
                            running_apaharam = ap_lord
                            break
                        apaharam_pointer = ap_end
                    break

            st.markdown(f"""
            <div class="current-dasha-box">
                🎯 <b>ഇപ്പോൾ നടക്കുന്ന ദശാകാലം (Current Period):</b><br>
                📆 ഇന്നത്തെ തീയതി: {today_dt.strftime('%d/%m/%Y')}<br>
                🌟 <b>{running_dasha} ദശയിൽ {running_apaharam} അപഹാരം</b> ആണ് ഇപ്പോൾ നടക്കുന്നത്.
            </div>
            """, unsafe_allow_html=True)

            st.write("**ഭൂത-ഭാവി ദശാ ടൈംലൈൻ (Full Dasha Timeline):**")
            timeline_html = """<table style='width:100%; border:1px solid #ddd; border-collapse:collapse; text-align:left;'>
            <tr style='background-color:#1a237e; color:white;'><th style='padding:10px;'>തുടങ്ങുന്ന തീയതി</th><th style='padding:10px;'>അവസാനിക്കുന്ന തീയതി</th><th style='padding:10px;'>ദശാ നാഥൻ</th></tr>"""
            
            for d_lord, s_time, e_time in dasha_sequence:
                row_bg = "background-color: #fff9c4; font-weight: bold;" if d_lord == running_dasha else ""
                timeline_html += f"<tr style='{row_bg}'><td style='padding:8px;'>{s_time.strftime('%d/%m/%Y')}</td><td style='padding:8px;'>{e_time.strftime('%d/%m/%Y')}</td><td style='padding:8px;'>{d_lord} ദശ</td></tr>"
            timeline_html += "</table>"
            st.markdown(timeline_html, unsafe_allow_html=True)
            st.markdown("---")

            # ഗുണങ്ങളും ശ്രദ്ധക്കേണ്ട കാര്യങ്ങളും
            st.markdown(f"""
            <div class="pred-box">
                <div class="strength">✅ <b>നിങ്ങളുടെ ഗുണം:</b> {STRENGTHS[nak_idx]}</div>
                <div class="caution">⚠️ <b>ശ്രദ്ധിക്കാൻ:</b> {CAUTIONS[nak_idx]} ഒഴിവാക്കുന്നത് മനഃസമാധാനം നൽകും.</div>
            </div>
            """, unsafe_allow_html=True)

            # വാട്സാപ്പ് മെസ്സേജ് ലോജിക്
            whatsapp_number = "919447093393"
            planets_list = [f"ലഗ്നം: {lagnam_rashi}"]
            for p_id, p_name in PLANETS.items():
                res, _ = swe.calc_ut(jd, p_id, swe.FLG_SIDEREAL)
                planets_list.append(f"{p_name}: {rashi_names[int(res[0]/30)]}")
            
            planets_str = "\n".join(planets_list)
            
            porutham_msg = ""
            if partner_nak_selected:
                porutham_msg = f"💑 *പൊരുത്തം:* 10-ൽ {matched_count} പൊരുത്തം ഉണ്ട് ({partner_nak_selected})\n"

            cesarean_msg = ""
            if is_cesarean == "Yes":
                cesarean_msg = "👶 *Type:* Cesarean Birth\n"

            msg = (
                f"✨ *UTA Wellness Report* ✨\n\n👤 *പേര്:* {name}\n📅 *തിയതി:* {dob.strftime('%d-%m-%Y')}\n"
                f"⏰ *സമയം:* {birth_time} ({birth_time_type} ജനനം)\n💓 *Pulse:* {pulse}\n🌟 *നക്ഷത്രം:* {MAL_NAK[nak_idx]}\n"
                f"{cesarean_msg}{porutham_msg}"
                f"🧬 *Current:* {running_dasha} ദശ - {running_apaharam} അപഹാരം\n\n🪐 *ഗ്രഹനില:*\n{planets_str}"
            )
            whatsapp_url = f"https://wa.me/{whatsapp_number}?text={msg.replace('\n', '%0A').replace(' ', '%20')}"
            
            st.success("🎉 റിപ്പോർട്ട് തയ്യാർ!")
            st.markdown(f'<div style="text-align: center; margin-bottom: 20px;"><a href="{whatsapp_url}" target="_blank" style="text-decoration: none;"><div style="background-color: #25D366; color: white; padding: 15px; border-radius: 10px; font-weight: bold; display: inline-block;">📲 റിപ്പോർട്ടും ഗ്രഹനിലയും അയക്കുക</div></a></div>', unsafe_allow_html=True)

            # =========================================================
            # 🪐 രാശി ചക്രവും നവാംശ ചക്രവും (Rashi & Navamsha Charts)
            # =========================================================
            chart_data = {i: [] for i in range(12)}
            navamsha_data = {i: [] for i in range(12)}
            
            lagnam_deg = ascmc[0]
            chart_data[int(lagnam_deg/30)].append("ലഗ്")
            navamsha_data[int((lagnam_deg * 9 / 30) % 12)].append("ലഗ്")

            for p_id, p_name in PLANETS.items():
                res, _ = swe.calc_ut(jd, p_id, swe.FLG_SIDEREAL)
                p_deg = res[0]
                chart_data[int(p_deg/30)].append(p_name)
                navamsha_data[int((p_deg * 9 / 30) % 12)].append(p_name)
            
            r_res, _ = swe.calc_ut(jd, swe.MEAN_NODE, swe.FLG_SIDEREAL)
            rahu_deg = r_res[0]
            ketu_deg = (rahu_deg + 180) % 360
            
            chart_data[int(rahu_deg/30)].append("രാ")
            chart_data[int(ketu_deg/30)].append("കേ")
            
            navamsha_data[int((rahu_deg * 9 / 30) % 12)].append("രാ")
            navamsha_data[int((ketu_deg * 9 / 30) % 12)].append("കേ")
            
            grid = [[11, 0, 1, 2], [10, -1, -1, 3], [9, -1, -1, 4], [8, 7, 6, 5]]
            
            html_rashi = '<table class="rashi-table">'
            for row in grid:
                html_rashi += '<tr>'
                for cell in row:
                    if cell == -1: 
                        html_rashi += '<td class="empty-td"></td>'
                    else:
                        content = "<br>".join(chart_data[cell])
                        cell_bg = "background-color: #ffebee;" if any(p in ["ശ", "ചൊ", "രാ", "കേ"] for p in chart_data[cell]) else ""
                        html_rashi += f'<td class="rashi-td" style="{cell_bg}">{content}</td>'
                html_rashi += '</tr>'
            html_rashi += '</table>'

            html_navamsha = '<table class="rashi-table">'
            for row in grid:
                html_navamsha += '<tr>'
                for cell in row:
                    if cell == -1: 
                        html_navamsha += '<td class="empty-td"></td>'
                    else:
                        content = "<br>".join(navamsha_data[cell])
                        cell_bg = "background-color: #e8eaf6;" if "ലഗ്" in navamsha_data[cell] else ""
                        html_navamsha += f'<td class="rashi-td" style="{cell_bg}">{content}</td>'
                html_navamsha += '</tr>'
            html_navamsha += '</table>'

            st.markdown(f"""
            <div class="charts-container">
                <div class="chart-box">
                    <h4>☸️ രാശി ചക്രം (Rashi Chart)</h4>
                    {html_rashi}
                </div>
                <div class="chart-box">
                    <h4>🔲 അംശകം ചക്രം (Navamsha Chart)</h4>
                    {html_navamsha}
                </div>
            </div>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Error: {e}")