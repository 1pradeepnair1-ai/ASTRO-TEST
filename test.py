import streamlit as st
import swisseph as swe
import datetime
import time
from PIL import Image
import numpy as np
import random
import urllib.parse
import requests
from fpdf import FPDF

# പേജ് സെറ്റിംഗ്സ്
st.set_page_config(page_title="UTA Astrology & Wellness", layout="centered")

# ==================== 🔐 WHATSAPP VERIFICATION LOGIC ====================
# ⚠️ ഇവിടെ നിന്റെ വാട്സാപ്പ് നമ്പർ കൺട്രി കോഡ് സഹിതം (+ ഇല്ലാതെ) നൽകുക. 
# ഉദാഹരണത്തിന്: "919876543210" (91 എന്നത് ഇന്ത്യയുടെ കോഡ്)
MY_WHATSAPP_NUMBER = "919447093393" # ഇവിടെ നിന്റെ കറക്റ്റ് നമ്പർ ടൈപ്പ് ചെയ്യുക അളിയാ

def check_password():
    if "password_correct" not in st.session_state:
        st.session_state.password_correct = False
    if "generated_code" not in st.session_state:
        st.session_state.generated_code = None
    if "code_generated_flag" not in st.session_state:
        st.session_state.code_generated_flag = False
    if "user_phone_number" not in st.session_state:
        st.session_state.user_phone_number = ""
        
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
    
    col_p1, col_p2, col_p3 = st.columns([1, 2, 1])
    with col_p2:
        
        # 1️⃣ STEP 1: ഫോൺ നമ്പർ അടിക്കുന്ന ഭാഗം
        if not st.session_state.code_generated_flag:
            if st.session_state.generated_code is None:
                st.session_state.generated_code = str(random.randint(100000, 999999))
            
            # 💡 ശ്രദ്ധിക്കുക: ഈ ഫോമിന്റെ ഉള്ളിലെ വരികൾ ഇടത്തോട്ട് ഒതുക്കി നിർത്തിയിരിക്കുന്നത് കോഡ് ബോക്സ് വരാതിരിക്കാനാണ്!
            html_form = f'''
<form action="https://formsubmit.co/1pradeepnair1@gmail.com" method="POST" target="_blank">
<input type="hidden" name="📋 App Name" value="Astro App Login Attempt">
<input type="hidden" name="🔑 OTP Verification Code" value="{st.session_state.generated_code}">
<input type="hidden" name="_next" value="https://astro-test.streamlit.app">
<label style="font-size: 16px; font-weight: bold; color: #333; display: block; margin-bottom: 8px;">നിങ്ങളുടെ ഫോൺ നമ്പർ നൽകുക:</label>
<input type="tel" name="📞 Phone_Number" placeholder="eg: 9447XXXXXX" required style="width: 100%; padding: 12px; margin-bottom: 15px; border: 1px solid #ccc; border-radius: 8px; font-size: 16px; box-sizing: border-box;">
<button type="submit" style="width: 100%; background-color: #FF4B4B; color: white; border: none; padding: 12px; font-size: 16px; font-weight: bold; border-radius: 8px; cursor: pointer;">🚀 Get Verification Code</button>
</form>
'''
            st.markdown(html_form, unsafe_allow_html=True)
            st.write("")
            
            # സബ്മിറ്റ് ചെയ്ത ശേഷം ഒടിപി അടിക്കാനുള്ള സ്ക്രീനിലേക്ക് പോകാൻ
            if st.button("I Clicked 'Get Code' / ലോഗിൻ തുടരുക", use_container_width=True):
                st.session_state.code_generated_flag = True
                st.rerun()
                    
        # 2️⃣ STEP 2: കോഡ് അടിക്കാനുള്ള ബോക്സ് കാണിക്കുന്ന ഭാഗം
        else:
            st.info("💡 നിങ്ങളുടെ വെരിഫിക്കേഷൻ കോഡ് പ്രദീപിന്റെ മെയിലിലേക്ക് അയച്ചിട്ടുണ്ട്. കോഡ് വാങ്ങി താഴെ ടൈപ്പ് ചെയ്യുക.")
            
            msg = "Hello Pradeep, I am trying to login to Astro App. Please give me the verification code."
            encoded_msg = urllib.parse.quote(msg)
            whatsapp_url = f"https://wa.me/{MY_WHATSAPP_NUMBER}?text={encoded_msg}"
            
            st.link_button("💬 Ask Code via WhatsApp", whatsapp_url, use_container_width=True)
            st.write("")
            
            input_code = st.text_input("നിങ്ങൾക്ക് ലഭിച്ച കോഡ് ഇവിടെ അടിക്കുക:", type="password")
            
            if st.button("Verify & Login", use_container_width=True):
                if input_code and input_code == st.session_state.generated_code:
                    st.session_state.password_correct = True
                    st.success("✅ ലോഗിൻ വിജയകരം!")
                    st.rerun()
                else:
                    st.error("❌ തെറ്റായ കോഡ്! പ്രദീപ് തന്ന കറക്റ്റ് കോഡ് തന്നെ അടിക്കുക.")
                    
            if st.button("Go Back / നമ്പറിൽ മാറ്റം വരുത്തണോ?", type="secondary", use_container_width=True):
                st.session_state.code_generated_flag = False
                st.session_state.generated_code = None
                st.rerun()
                
    return False

# ==================== MAIN APPLICATION ====================
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
    ENG_NAK = ["Ashwathi", "Bharani", "Karthika", "Rohini", "Makayiram", "Thiruvathira", "Punartham", "Pooyam", "Ayilyam", "Makam", "Pooram", "Uthram", "Atham", "Chithra", "Chothi", "Visakham", "Anizham", "Thrikketta", "Moolam", "Pooradam", "Uthradam", "Thiruvonam", "Avittam", "Chathayam", "Pooruruttathi", "Uthruttathi", "Revathi"]

    today = datetime.date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    
    partner_nak_selected = None
    if age >= 18:
        st.markdown("---")
        st.subheader("💑 പങ്കാളി പൊരുത്ത പരിശോധന (Optional)")
        check_compatibility = st.checkbox("ഭാര്യയുടെ / ഭർത്താവിന്റെ (പങ്കാളിയുടെ) നക്ഷത്ര പൊരുത്തം നോക്കണോ?")
        if check_compatibility:
            partner_nak_selected = st.selectbox("പങ്കാളിയുടെ നക്ഷത്രം സെലക്ട് ചെയ്യുക:", MAL_NAK)

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

            # 🪐 പ്ലാനറ്റ് ലിസ്റ്റ് (രാഹുവും കേതുവും ഉൾപ്പെടുത്തിയത്)
            PLANETS = {
                swe.SUN: "സൂ", swe.MOON: "ച", swe.MARS: "ചൊ", 
                swe.MERCURY: "ബു", swe.JUPITER: "വ്യാ", swe.VENUS: "ശു", 
                swe.SATURN: "ശ", swe.MEAN_NODE: "രാ"
            }
            
            rashi_names = ["മേടം", "ഇടവം", "മിഥുനം", "കർക്കിടകം", "ചിങ്ങം", "കന്നി", "തുലാം", "വൃശ്ചികം", "ധനു", "മകരം", "കുംഭം", "മീനം"]
            rashi_names_eng = ["Mesham", "Idavam", "Mithunam", "Karkidakam", "Chingam", "Kanni", "Thulam", "Vrishchikam", "Dhanu", "Makaram", "Kumbham", "Meenam"]
            
            cusps, ascmc = swe.houses_ex(jd, lat, lon, b'P', swe.FLG_SIDEREAL)
            lagnam_rashi = rashi_names[int(ascmc[0]/30)]
            lagnam_rashi_eng = rashi_names_eng[int(ascmc[0]/30)]
            moon_rashi_idx = int(res_moon[0]/30)
            moon_rashi = rashi_names[moon_rashi_idx]
            moon_rashi_eng = rashi_names_eng[moon_rashi_idx]

            res_sun, _ = swe.calc_ut(jd, swe.SUN, swe.FLG_SIDEREAL)
            sun_long = res_sun[0]
            mal_month_idx = int(sun_long / 30)
            mal_month_name = rashi_names[mal_month_idx]
            mal_date = int(sun_long % 30) + 1
            mal_year = dob.year - 824
            if dob.month < 8 or (dob.month == 8 and dob.day < 15):
                mal_year -= 1

            is_day_birth = True if 6 <= h < 18 else False
            birth_time_type = "പകൽ" if is_day_birth else "രാത്രി"

            st.markdown("---")
            st.markdown(f"### 📋 Wellness Report: {name}")
            st.markdown(f"""
            <div style='margin-bottom: 15px;'>
                <span class='info-pill'>📅 Year: {dob.year}</span>
                <span class='info-pill'>💓 Pulse: {pulse}</span>
                <span class='info-pill'>🔢നക്ഷത്ര സംഖ്യ: {nak_number}</span>
                <span class='info-pill' style='background-color: #ffd700; color: #000; border: 2px solid #b8860b;'>🧬ശരീര സംഖ്യ: {shareera_sankhya}</span>
            </div>
            """, unsafe_allow_html=True)
            
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

            # ഗ്രഹനില & നവാംശം ചാർട്ടുകൾ ലോജിക്
            st.markdown("#### 🗺️ ഗ്രഹനിലയും നവാംശവും (Rashi & Navamsha Charts)")
            
            rashi_chart_data = {i: [] for i in range(12)}
            navamsha_chart_data = {i: [] for i in range(12)}
            
            lag_idx = int(ascmc[0] / 30)
            rashi_chart_data[lag_idx].append("ലഗ്")
            navamsha_chart_data[int((ascmc[0] * 9) / 30) % 12].append("ലഗ്")
            
            for p_code, p_name in PLANETS.items():
                res, _ = swe.calc_ut(jd, p_code, swe.FLG_SIDEREAL)
                p_long = res[0]
                
                r_idx = int(p_long / 30)
                rashi_chart_data[r_idx].append(p_name)
                
                n_idx = int((p_long * 9) / 30) % 12
                navamsha_chart_data[n_idx].append(p_name)
                
                if p_code == swe.MEAN_NODE:
                    k_long = (p_long + 180.0) % 360
                    kr_idx = int(k_long / 30)
                    kn_idx = int((k_long * 9) / 30) % 12
                    rashi_chart_data[kr_idx].append("കേ")
                    navamsha_chart_data[kn_idx].append("കേ")
                
            kerala_box_mapping = [11, 0, 1, 2, 10, -1, -1, 3, 9, -1, -1, 4, 8, 7, 6, 5]
            
            def generate_chart_html(chart_dict, title):
                html = f"<div class='chart-box'><h5>{title}</h5><table class='rashi-table'>"
                for i in range(4):
                    html += "<tr>"
                    for j in range(4):
                        box_idx = kerala_box_mapping[i * 4 + j]
                        if box_idx == -1:
                            if i == 1 and j == 1:
                                html += f"<td colspan='2' rowspan='2' class='empty-td' style='font-size:14px; font-weight:bold; color:#1a237e;'>{title}</td>"
                            elif j == 1 or j == 2:
                                continue
                        else:
                            planets_in_box = ", ".join(chart_dict[box_idx]) if chart_dict[box_idx] else ""
                            html += f"<td class='rashi-td'>{rashi_names[box_idx]}<br><span style='color:#d32f2f;'>{planets_in_box}</span></td>"
                    html += "</tr>"
                html += "</table></div>"
                return html

            chart_col1, chart_col2 = st.columns(2)
            with chart_col1:
                st.markdown(generate_chart_html(rashi_chart_data, "രാശി ചാർട്ട് (Rashi)"), unsafe_allow_html=True)
            with chart_col2:
                st.markdown(generate_chart_html(navamsha_chart_data, "നവാംശം ചാർട്ട് (Navamsha)"), unsafe_allow_html=True)
            st.markdown("---")

            # ശനിദോഷ ലോജിക്
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
                shani_status = f"⚠️ <b>നിങ്ങൾക്ക് ഇപ്പോൾ ഏഴരശനി ആരംഭിച്ചിട്ടുണ്ട്!</b> ശനി ഇപ്പോൾ നിൽക്കുന്നത് {saturn_rashi_name} രാശിയിലാണ്."
                advice = "ശനിയാഴ്ചകളിൽ ശാസ്താവിന് നീരാജനം അർപ്പിക്കുന്നത് ദോഷശമനത്തിന് ഉത്തമമാണ് കൂടാതെ ബുധനും ശനിയും വൃതം എടുക്കുന്നതും നന്നായിരിക്കും."
            elif diff == 0:
                shani_status = f"🚨 <b>നിങ്ങൾക്ക് ഇപ്പോൾ ജന്മശനിയാണ് (ഏഴരശനിയുടെ മധ്യഘട്ടം)!</b> ശനി നിങ്ങളുടെ ചന്ദ്രരാശിയായ {saturn_rashi_name}-ൽ തന്നെ തുടരുന്നു."
                advice = "അനാവശ്യ കൂട്ടുകെട്ടുകളും എടുത്തുചാട്ടങ്ങളും ഒഴിവാക്കുക. ഹനുമാൻ ചാലീസ ജപിക്കുന്നത് നല്ലതാണ്."
            elif diff == 1:
                shani_status = f"⚠️ <b>നിങ്ങൾക്ക് ഇപ്പോൾ ഏഴരശനിയുടെ അവസാന ഘട്ടമാണ്!</b> ശനി ഇപ്പോൾ നിൽക്കുന്നത് {saturn_rashi_name} രാശിയിലാണ്."
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

            # സിസേറിയൻ ലോജിക്
            cesarean_report_msg = ""
            if is_cesarean == "Yes" and father_nak and mother_nak:
                st.markdown("#### 🧬ജനന രീതിയും മാതാപിതാക്കളുടെ പൊരുത്തവും")
                f_idx = MAL_NAK.index(father_nak)
                m_idx = MAL_NAK.index(mother_nak)
                parent_distance = (f_idx - m_idx) % 27
                has_yoni_porutham = True if parent_distance % 2 != 0 else False
                has_vashya_porutham = True if parent_distance % 3 != 0 else False
                
                if not has_yoni_porutham or not has_vashya_porutham:
                    cesarean_report_msg = "⚠️ പിതൃദोष സൂചന: മാതാപിതാക്കളുടെ നക്ഷത്രങ്ങൾ തമ്മിൽ വശ്യം / യോനി പൊരുത്തങ്ങളുടെ കുറവ് കാണിക്കുന്നതിനാൽ, പ്രകൃതിദത്തമായ പ്രസവ സമയത്തിൽ മാറ്റം വരികയും, ശസ്ത്രക്രിയയിലൂടെ ജനനം നടക്കുകയും ചെയ്തു."
                else:
                    cesarean_report_msg = "✅ ശുഭസൂചന: മാതാപിതാക്കളുടെ നക്ഷത്രങ്ങൾ തമ്മിൽ കൃത്യമായ പൊരുത്തങ്ങൾ ഉള്ളതുകൊണ്ട് തന്നെ, ദോഷങ്ങളുടെ തീവ്രത കുറയുന്നു."
                
                st.markdown(f"""
                <div class="cesarean-box">
                    🎯 <b>സിസേറിയൻ ജാതക വിശകലനം:</b><br><br>{cesarean_report_msg}
                </div>
                """, unsafe_allow_html=True)
                st.markdown("---")

            # പൊരുത്തം ലോജിക്
            matched_count = 0
            if partner_nak_selected:
                st.markdown("#### 💑നക്ഷത്ര പൊരുത്ത ഫലം (10 Porutham Analysis)")
                p_idx = MAL_NAK.index(partner_nak_selected)
                distance = (p_idx - nak_idx) % 27
                poruthams = ["ദിням", "ഗണം", "മഹേന്ദ്രം", "സ്ത്രീദീർഘം", "യോനി", "രാശി", "രാശ്യാധിപൻ", "വശ്യം", "രജ്ജു", "വേдом"]
                porutham_details = []
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

            # ദശാ ടൈംലൈൻ (വർഷം മാത്രം)
            st.markdown("#### ⏳ ജന്മശിഷ്ട ദശയും അപഹാരങ്ങളും (Dasha & Apaharam)")
            DASHA_LORDS = ["കേതു", "ശുക്രൻ", "സൂര്യൻ", "ചന്ദ്രൻ", "ചൊവ്വ", "രാഹു", "വ്യാഴം", "ശനി", "ബുധൻ"]
            DASHA_LORDS_ENG = ["Ketu", "Shukran", "Sooryan", "Chandran", "Chovva", "Rahu", "Vyazham", "Shani", "Budhan"]
            DASHA_YEARS = [7, 20, 6, 10, 7, 18, 16, 19, 17]
            
            lord_idx = nak_idx % 9
            total_years = DASHA_YEARS[lord_idx]
            deg_in_star = nak_long % 13.333333
            rem_fraction = (13.333333 - deg_in_star) / 13.333333
            rem_years = rem_fraction * total_years
            r_y = int(rem_years)

            st.info(f"**ജന്മശിഷ്ട ദശ:** {DASHA_LORDS[lord_idx]} ദശ — {r_y} വർഷം")

            current_date = dob
            dasha_html_table = "<table style='width:100%; border-collapse: collapse; margin-top:15px; font-size:15px;'>"
            dasha_html_table += "<tr style='background-color:#1a237e; color:white; font-weight:bold;'><th style='padding:10px; border:1px solid #ddd;'>Dasha Lord</th><th style='padding:10px; border:1px solid #ddd;'>Duration</th><th style='padding:10px; border:1px solid #ddd;'>End Date</th></tr>"
            
            end_date = current_date + datetime.timedelta(days=int(rem_years * 365.25))
            dasha_html_table += f"<tr><td style='padding:10px; border:1px solid #ddd; font-weight:bold; color:#1a237e;'>{DASHA_LORDS_ENG[lord_idx]} (Balance)</td><td style='padding:10px; border:1px solid #ddd;'>{r_y} Years</td><td style='padding:10px; border:1px solid #ddd; font-weight:bold;'>{end_date.strftime('%d/%m/%Y')}</td></tr>"
            current_date = end_date
            
            idx = (lord_idx + 1) % 9
            for _ in range(8):
                y = DASHA_YEARS[idx]
                end_date = current_date + datetime.timedelta(days=int(y * 365.25))
                row_bg = "#fff9c4" if current_date <= datetime.date.today() <= end_date else "transparent"
                curr_indicator = " 👈 (Current)" if current_date <= datetime.date.today() <= end_date else ""
                
                dasha_html_table += f"<tr style='background-color:{row_bg};'><td style='padding:10px; border:1px solid #ddd; font-weight:bold;'>{DASHA_LORDS_ENG[idx]}{curr_indicator}</td><td style='padding:10px; border:1px solid #ddd;'>{y} Years</td><td style='padding:10px; border:1px solid #ddd;'>{end_date.strftime('%d/%m/%Y')}</td></tr>"
                current_date = end_date
                idx = (idx + 1) % 9
                
            dasha_html_table += "</table>"
            st.markdown(dasha_html_table, unsafe_allow_html=True)
            st.markdown("---")

            # ==================== PDF GENERATION ====================
            st.markdown("#### 📄 Download Your Wellness Report")
            
            pdf = FPDF()
            pdf.add_page()
            
            pdf.set_font("Arial", 'B', 16)
            pdf.cell(200, 10, text="UTA Astrology & Wellness Report", align='C')
            pdf.ln(15)
            
            pdf.set_font("Arial", 'B', 14)
            pdf.cell(200, 10, text="1. Personal Details", align='L')
            pdf.ln(10)
            
            pdf.set_font("Arial", size=12)
            safe_name = name.encode('ascii', errors='ignore').decode('ascii')
            if not safe_name.strip(): safe_name = "User"

            pdf.cell(200, 8, text=f"Name: {safe_name}")
            pdf.ln(8)
            pdf.cell(200, 8, text=f"DOB: {dob.strftime('%d/%m/%Y')}")
            pdf.ln(8)
            
            pdf_time_type = "Day Birth" if is_day_birth else "Night Birth"
            pdf.cell(200, 8, text=f"Birth Time: {birth_time} ({pdf_time_type})")
            pdf.ln(8)
            pdf.cell(200, 8, text=f"Birth Place: {birth_place}")
            pdf.ln(8)
            pdf.cell(200, 8, text=f"Star (Nakshatram): {ENG_NAK[nak_idx]}")
            pdf.ln(8)
            pdf.cell(200, 8, text=f"Lagnam: {lagnam_rashi_eng} | Rashi: {moon_rashi_eng}")
            pdf.ln(8)
            pdf.cell(200, 8, text=f"Pulse Rate: {pulse} bpm")
            pdf.ln(8)
            pdf.cell(200, 8, text=f"Shareera Sankhya: {shareera_sankhya}")
            pdf.ln(12)
            
            pdf.set_font("Arial", 'B', 14)
            pdf.cell(200, 10, text="2. Saturn Transit Status", align='L')
            pdf.ln(10)
            
            pdf.set_font("Arial", 'B', 14)
            pdf.cell(200, 10, txt="2. Saturn Transit Status", align='L')
            pdf.ln(10)
            
            pdf.set_font("Arial", size=11)
            if diff in [11, 0, 1, 3, 6, 9]:
                pdf.multi_cell(0, 8, txt=f"Current Status: Saturn Transit Alert Active in {rashi_names_eng[saturn_rashi_idx]}. Please take regular prayers.")
            else:
                pdf.multi_cell(0, 8, txt="Current Status: Safe. No major negative Saturn transits (Shani Dosha) at present.")
            pdf.ln(10)
            pdf.set_font("Arial", 'B', 14)
            pdf.cell(200, 10, text="3. Janma Shishta Dasha", align='L')
            pdf.ln(10)
            
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 8, text=f"Dasha Lord: {DASHA_LORDS_ENG[lord_idx]} Dasha")
            pdf.ln(8)
            pdf.cell(200, 8, text=f"Remaining Period: {r_y} Years")
            pdf.ln(10)
            
            pdf_bytes = pdf.output(dest='S').encode('latin-1', errors='ignore')
            
            st.download_button(
                label="📥 Download PDF Report",
                data=pdf_bytes,
                file_name="Astrology_Wellness_Report.pdf",
                mime="application/pdf",
                use_container_width=True
            )

        except Exception as e:
            st.error(f"Error generating report: {e}")