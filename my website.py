import streamlit as st
import os
import base64

# ----------------- ROBUST IMAGE FINDER -----------------
def find_image(filename):
    """
    Looks for the image in several common locations to prevent missing file errors.
    """
    candidates = [
        # Same directory as this Python script
        os.path.join(os.path.dirname(os.path.abspath(__file__)), filename),
        # OneDrive Desktop (Windows)
        os.path.join(r"C:\Users\racha\OneDrive\Desktop", filename),
        # Standard Desktop
        os.path.join(os.path.expanduser("~"), "Desktop", filename),
        # Current working directory
        os.path.join(os.getcwd(), filename),
        filename
    ]
    for path in candidates:
        if os.path.exists(path):
            return path
    return None

# Helper to encode images for HTML CSS backgrounds
def get_base64_image(image_path):
    if image_path and os.path.exists(image_path):
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

# Check for tab logo
icon_path = find_image("logo.png")

# Set browser tab title and favicon
st.set_page_config(
    page_title="Pickle Mart",
    page_icon=icon_path if icon_path else "🏺",
    layout="wide"
)

# ----------------- SIDEBAR NAVIGATION -----------------
if icon_path:
    st.sidebar.image(icon_path, width=90)
st.sidebar.title("Pickle Mart")

# Modified: FAQs and Book Franchise sections are completely removed.
menu_choice = st.sidebar.radio(
    "Go to:",
    [
        "Home",
        "About Us",
        "Menu Card",
        "Unit Franchise",
        "Gallery",
        "Contact Us"
    ]
)

# ----------------- SECTION 1: HOME -----------------
if menu_choice == "Home":
    
    # ===== PART 1: WOMEN MAKING PICKLES SLIDESHOW =====
    st.markdown("<h2 style='text-align: center; color: #8B0000; margin-bottom: 20px;'>Our Heritage: Handcrafted With Love</h2>", unsafe_allow_html=True)
    
    slideshow_images = [
        (find_image("slide1.png"), "1. Traditional handmade pickle preparation with authentic ingredients."),
        (find_image("slide2.png"), "2. Stirring and curing Andhra pickles in classic ceramic martabans."),
        (find_image("slide3.png"), "3. Fresh raw green mango cutting and ingredient preparation."),
        (find_image("slide4.png"), "4. Traditional stone-ground spices and mustard mixing."),
        (find_image("slide5.png"), "5. Pouring pure golden oil and rich chili blend into ceramic jars."),
        (find_image("slide6.png"), "6. Tying red cloth seals with jute rope and sun-maturing in rows.")
    ]
    
    if "slide_idx" not in st.session_state:
        st.session_state.slide_idx = 0
        
    slide_col1, slide_col2, slide_col3 = st.columns([1, 10, 1])
    with slide_col1:
        st.write("")
        st.write("")
        st.write("")
        if st.button("◀", key="prev_slide"):
            st.session_state.slide_idx = (st.session_state.slide_idx - 1) % len(slideshow_images)
            
    with slide_col2:
        img_path, caption = slideshow_images[st.session_state.slide_idx]
        if img_path and os.path.exists(img_path):
            st.image(img_path, caption=f"Slide {st.session_state.slide_idx + 1} of {len(slideshow_images)}: {caption}", width="stretch")
        else:
            st.warning(f"Slide {st.session_state.slide_idx + 1}: Image 'slide{st.session_state.slide_idx + 1}.png' not found. Please ensure it is saved on your Desktop.")
        
    with slide_col3:
        st.write("")
        st.write("")
        st.write("")
        if st.button("▶", key="next_slide"):
            st.session_state.slide_idx = (st.session_state.slide_idx + 1) % len(slideshow_images)
            
    st.write("")
    st.markdown("<hr style='border: 1px dashed #d97706;'>", unsafe_allow_html=True)
    st.write("")

    # ===== PART 2: ABOUT SECTION (LEFT: TEXT | RIGHT: 2 IMAGES) =====
    col_left, col_right = st.columns([6, 5], gap="large")
    
    with col_left:
        st.markdown("<h1 style='color: #8B0000; letter-spacing: 2px; margin-bottom: 0px;'>ABOUT</h1>", unsafe_allow_html=True)
        st.markdown("<div style='height: 4px; width: 140px; background: linear-gradient(90deg, #d97706, #b91c1c); margin-top: 5px; margin-bottom: 20px; border-radius: 2px;'></div>", unsafe_allow_html=True)
        st.markdown("<h3 style='color: #b91c1c; font-style: italic;'>Our Delicious Story</h3>", unsafe_allow_html=True)
        
        story_text = """
        **Pickle Mart** is a famous store in Andhra Pradesh. This picklemart has more than 100 types of homemade non-veg pickles, veg pickles, pastries, karam podulu etc. which are famous in Andhra. 
        
        Especially this Pickle Mart store has **Bhimavaram non-veg pickles** which are very famous in Andhra. 
        
        Besides, authentic traditional food products like:
        - 🍯 **Atreyapuram Putarekulu**
        - 🥟 **Kakinada Kaja**
        - 🥮 **Tapeswaram Madatha Kaja**
        - 🍬 **Dhavaleswaram Jheellu**
        - 🥛 **Gangaraju Palakova**
        
        ...are proudly available in this picklemart.
        """
        st.markdown(story_text)
        
    with col_right:
        img_right1 = find_image("about_showcase1.png")
        img_right2 = find_image("about_showcase2.png")
        
        if img_right1 and os.path.exists(img_right1):
            st.image(img_right1, caption="Traditional Andhra Sweets & Pickles Showcase", width="stretch")
        else:
            st.info("Place 'about_showcase1.png' on your Desktop to display this image.")
            
        if img_right2 and os.path.exists(img_right2):
            st.image(img_right2, caption="Authentic Bhimavaram Style Special Mango Pickle", width="stretch")
        else:
            st.info("Place 'about_showcase2.png' on your Desktop to display this image.")

    st.write("")
    st.markdown("<hr style='border: 1px dashed #d97706;'>", unsafe_allow_html=True)
    st.write("")

    # ===== PART 3: SPICES BACKGROUND =====
    bg_local_path = find_image("spices_bg.png")
    encoded_bg = get_base64_image(bg_local_path)
    
    if encoded_bg:
        bg_style = f"background-image: linear-gradient(rgba(0, 0, 0, 0.65), rgba(0, 0, 0, 0.75)), url('data:image/png;base64,{encoded_bg}');"
    else:
        bg_style = "background-color: #3b1d11;"

    st.markdown(f"""
    <div style="
        {bg_style}
        background-size: cover;
        background-position: center;
        padding: 50px 20px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-top: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    ">
        <h2 style='color: #f59e0b; font-family: Georgia, serif; margin-bottom: 8px;'>✨ The Secret Behind The Taste ✨</h2>
        <p style='font-size: 17px; max-width: 750px; margin: 0 auto; color: #fef3c7;'>
            Sun-dried Guntur red chilies, cold-pressed sesame oil, fresh green raw mangoes, and generations-old authentic recipes made fresh by hand.
        </p>
        <div style='margin-top: 25px;'>
            <span style='font-size: 26px; color: #f59e0b;'>❖ ═══ ✦ ═══ ❖</span>
        </div>
        <p style='color: #e5e7eb; font-size: 13px; margin-top: 10px; letter-spacing: 1px;'>
            PURE HANDMADE TRADITION • NO ARTIFICIAL PRESERVATIVES • DIRECT FROM ANDHRA
        </p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")

# ----------------- SECTION 2: ABOUT US -----------------
elif menu_choice == "About Us":
    st.markdown("<h1 style='text-align: center; color: #8B0000; letter-spacing: 2px;'>ABOUT US</h1>", unsafe_allow_html=True)
    st.markdown("<div style='height: 4px; width: 100px; background: linear-gradient(90deg, #d97706, #b91c1c); margin: 0 auto 30px auto; border-radius: 2px;'></div>", unsafe_allow_html=True)
    
    # ===== PART 1: MANGO TREE AND FOUNDERS PHOTO =====
    tree_img = find_image("about_mango_tree.png")
    owners_img = find_image("about_owners.png")
    
    if tree_img and os.path.exists(tree_img):
        st.image(tree_img, caption="Our Pure Roots: Orchards Full of Fresh Farm Mangoes", width="stretch")
    else:
        st.info("Place 'about_mango_tree.png' on your Desktop to display the tree photograph.")
        
    st.write("")
    
    owner_col1, owner_col2, owner_col3 = st.columns([1, 2, 1])
    with owner_col2:
        if owners_img and os.path.exists(owners_img):
            st.image(owners_img, caption="The Founders & Visionaries Behind Pickle Mart", width="stretch")
        else:
            st.info("Place 'about_owners.png' on your Desktop to display the founders' photo.")

    st.write("")
    st.markdown("<hr style='border: 1px dashed #d97706;'>", unsafe_allow_html=True)
    st.write("")

    # ===== PART 2: TWO COLUMNS (LEFT: STORY | RIGHT: STORE PHOTO) =====
    p2_col_left, p2_col_right = st.columns([7, 5], gap="large")
    
    with p2_col_left:
        st.markdown("<h2 style='color: #8B0000; margin-bottom: 5px;'>A Few Words About Us</h2>", unsafe_allow_html=True)
        st.markdown("<div style='height: 3px; width: 80px; background: #d97706; margin-bottom: 15px;'></div>", unsafe_allow_html=True)
        
        about_text = """
        **M/s Pickle mart** company will set up pickle stores named **“Pickle Mart”** *(Homemade Andhra foods)*.

        This company is established in **Eluru city center in Eluru district**, which is a Godavari catchment district in Andhra Pradesh. The company also operates other businesses. This company will move forward with a vision to expand famous foods in Andhra Pradesh to all areas of the country. **The company aims to set up 200 stores in the next two years.**

        Pickle mart store business was started by **three young entrepreneurs** who can make pickles in such a way that, each bite of rice you take with our pickles will feast your taste buds. It’s more of a tradition than business for the last 15 years. We feel that everyone should taste our pickles at least once to tell this is true. 

        We are backed by a couple of grannies, who fed a few hundred families in their decades of homemade pickling experience. Our pickles are **100% home-made** with fresh and best quality ingredients which are all sourced from nature. We make each pickle in a way that, we are making it for our own family consumption. Best quality oils are used in our pickles—they give the best taste that you experience by eating our pickles.

        *All we can say is, Taste it once and you are sure to come back for more – Our pickles are a feast to taste buds in every bite because we mix a special ingredient which no one else does and that is pure love and authentic tradition.*
        """
        st.markdown(about_text)

    with p2_col_right:
        st.write("")
        shop_img = find_image("about_shop.png")
        if shop_img and os.path.exists(shop_img):
            st.image(shop_img, caption="Pickle Mart Retail Experience Store", width="stretch")
        else:
            st.info("Place 'about_shop.png' on your Desktop to display the shop picture.")

    st.write("")
    st.markdown("<hr style='border: 1px dashed #d97706;'>", unsafe_allow_html=True)
    st.write("")

    # ===== PART 3: BUSINESS MEETING TABLE BACKGROUND =====
    biz_bg_path = find_image("about_business_bg.png")
    encoded_biz_bg = get_base64_image(biz_bg_path)
    
    if encoded_biz_bg:
        biz_bg_style = f"background-image: linear-gradient(rgba(10, 10, 10, 0.82), rgba(10, 10, 10, 0.88)), url('data:image/png;base64,{encoded_biz_bg}');"
    else:
        biz_bg_style = "background-color: #1e293b;"

    st.markdown(f"""
    <div style="
        {biz_bg_style}
        background-size: cover;
        background-position: center;
        padding: 45px 35px;
        border-radius: 16px;
        color: white;
        margin-top: 15px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.35);
    ">
        <div style="display: flex; flex-wrap: wrap; gap: 30px; justify-content: space-between;">
            <div style="flex: 1 1 45%; min-width: 290px; background: rgba(255, 255, 255, 0.08); padding: 25px; border-radius: 12px; border-left: 4px solid #f59e0b;">
                <h3 style="color: #f59e0b; margin-top: 0; font-size: 24px; font-weight: 700;">🎯 Our Mission</h3>
                <p style="font-size: 16px; line-height: 1.6; color: #f3f4f6; margin-bottom: 0;">
                    This company will move forward with a vision to expand famous foods in Andhra Pradesh to all areas of the country. 
                    The company aims to <strong>set up 200 stores in the next two years</strong>.
                </p>
            </div>
            <div style="flex: 1 1 45%; min-width: 290px; background: rgba(255, 255, 255, 0.08); padding: 25px; border-radius: 12px; border-left: 4px solid #ef4444;">
                <h3 style="color: #ef4444; margin-top: 0; font-size: 24px; font-weight: 700;">💎 Our Core Values</h3>
                <p style="font-size: 16px; line-height: 1.6; color: #f3f4f6; margin-bottom: 0;">
                    Our pickles are <strong>100% home-made</strong> with fresh and best quality ingredients which are all sourced from nature. 
                    We make each pickle in a way that, we are making it for our own family consumption. Best quality oils are used in our pickles—they give the best taste that you experience by eating our pickles.
                </p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.write("")

# ----------------- SECTION 3: MENU CARD -----------------
elif menu_choice == "Menu Card":
    
    # ===== PART 1: NON-VEG PICKLE BACKGROUND BANNER =====
    menu_bg_path = find_image("menu_nonveg_bg.png")
    encoded_menu_bg = get_base64_image(menu_bg_path)
    
    if encoded_menu_bg:
        menu_bg_style = f"background-image: linear-gradient(rgba(0, 0, 0, 0.68), rgba(0, 0, 0, 0.78)), url('data:image/png;base64,{encoded_menu_bg}');"
    else:
        menu_bg_style = "background: linear-gradient(135deg, #7f1d1d, #450a0a);"

    st.markdown(f"""
    <div style="
        {menu_bg_style}
        background-size: cover;
        background-position: center;
        padding: 55px 30px;
        border-radius: 16px;
        text-align: center;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.35);
    ">
        <h1 style='color: #f59e0b; font-size: 44px; letter-spacing: 2px; margin-bottom: 5px; font-weight: 800;'>Pickle Mart</h1>
        <h3 style='color: #fef08a; font-style: italic; font-size: 26px; margin-top: 0;'>Our Menu</h3>
        <p style='font-size: 18px; max-width: 850px; margin: 15px auto 0 auto; color: #f3f4f6; line-height: 1.7;'>
            Pickle Mart is a store selling famous homemade non-veg pickles, veg pickles, pastries, karam podies in Andhra Pradesh. 
            Especially this Pickle Mart store has <strong>Bhimavaram non-veg pickles</strong> which are very famous in Andhra.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col_red, col_mid_text, col_prawn = st.columns([3, 6, 3], gap="medium")
    
    with col_red:
        red_chilli_img = find_image("menu_redchilli.png")
        if red_chilli_img and os.path.exists(red_chilli_img):
            st.image(red_chilli_img, caption="Spicy Andhra Red Chilli Pickle (Pandu Mirapa)", width="stretch")
        else:
            st.info("Place 'menu_redchilli.png' on Desktop.")
            
    with col_mid_text:
        st.markdown("""
        <div style="text-align: center; padding: 25px 15px; background-color: #fffbeb; border-radius: 12px; border: 1px dashed #d97706; margin-top: 10px;">
            <h3 style="color: #8B0000; margin-bottom: 10px;">✨ Authentic Taste of Andhra ✨</h3>
            <p style="font-size: 16px; color: #451a03; line-height: 1.7; margin: 0;">
                Every jar of <strong>Pickle Mart</strong> preserves the authentic, traditional spices and pure cold-pressed oils from the heart of the Godavari region. 
                Experience a burst of fiery and rich traditional homemade flavours in every single bite!
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with col_prawn:
        prawn_img = find_image("menu_prawns.png")
        if prawn_img and os.path.exists(prawn_img):
            st.image(prawn_img, caption="Famous Bhimavaram Prawns Pickle (Royyala Pachadi)", width="stretch")
        else:
            st.info("Place 'menu_prawns.png' on Desktop.")

    st.write("")
    st.markdown("<hr style='border: 1px dashed #d97706;'>", unsafe_allow_html=True)
    st.write("")

    # ===== PART 2: THREE PICTURES (GONGURA, MUTTON, FISH) =====
    st.markdown("<h3 style='text-align: center; color: #8B0000; margin-bottom: 25px;'>Signature Specialties</h3>", unsafe_allow_html=True)
    trio_col1, trio_col2, trio_col3 = st.columns(3, gap="medium")
    
    with trio_col1:
        gongura_img = find_image("menu_gongura.png")
        if gongura_img and os.path.exists(gongura_img):
            st.image(gongura_img, caption="Traditional Gongura Pickle", width="stretch")
        else:
            st.info("Place 'menu_gongura.png' on Desktop.")
            
    with trio_col2:
        mutton_img = find_image("menu_mutton.png")
        if mutton_img and os.path.exists(mutton_img):
            st.image(mutton_img, caption="Rich Spicy Mutton Pickle", width="stretch")
        else:
            st.info("Place 'menu_mutton.png' on Desktop.")
            
    with trio_col3:
        fish_img = find_image("menu_fish.png")
        if fish_img and os.path.exists(fish_img):
            st.image(fish_img, caption="Authentic Andhra Fish Pickle", width="stretch")
        else:
            st.info("Place 'menu_fish.png' on Desktop.")

    st.write("")
    st.markdown("<hr style='border: 1px dashed #d97706;'>", unsafe_allow_html=True)
    st.write("")

    # ===== PART 3: COMPLETE MENU CARD LISTINGS =====
    st.markdown("<h2 style='text-align: center; color: #8B0000; margin-bottom: 25px;'>Pickle Mart Complete Price & Variety List</h2>", unsafe_allow_html=True)
    
    menu_tabs = st.tabs([
        "🍗 Non-Veg Pickles", 
        "🥭 Veg Pickles", 
        "🌶️ Karappodulu & Vadiyalu", 
        "🍯 Special Items"
    ])
    
    # 1. Non-Veg Pickles Tab
    with menu_tabs[0]:
        st.markdown("<h3 style='color: #8B0000;'>Bhimavaram Non-Veg Pickles (23 Varieties)</h3>", unsafe_allow_html=True)
        nv_col1, nv_col2 = st.columns(2)
        
        non_veg_items_left = [
            "CHICKEN PICKLE",
            "BONELESS CHICKEN PICKLE",
            "NATUKODI PICKLE",
            "KORAMEENU PICKLE",
            "PANDUGAPPA FISH PICKLE",
            "CRAB PICKLE",
            "SMALL PRAWN PICKLE",
            "LARGE PRAWN PICKLE",
            "MUTTON PICKLE",
            "BONELESS MUTTON PICKLE",
            "CASHEW MUTTON KHEEMA",
            "CHERUVU FISH"
        ]
        
        non_veg_items_right = [
            "CHICKEN GONGURA",
            "BONELESS CHICKEN GONGURA",
            "NATUKODI GONGURA",
            "SMALL PRAWN GONGURA",
            "LARGE PRAWN GONGURA",
            "MUTTON GONGURA",
            "BONELESS MUTTON GONGURA",
            "MUTTON KHEEMA GONGURA",
            "APOLLO FISH PICKLE",
            "CASHEW CHICKEN KHEEMA",
            "METTALLU FISH"
        ]
        
        with nv_col1:
            for item in non_veg_items_left:
                st.markdown(f"- 🥩 **{item}**")
        with nv_col2:
            for item in non_veg_items_right:
                st.markdown(f"- 🥩 **{item}**")

    # 2. Veg Pickles Tab
    with menu_tabs[1]:
        st.markdown("<h3 style='color: #8B0000;'>Traditional Homemade Veg Pickles (26 Varieties)</h3>", unsafe_allow_html=True)
        v_col1, v_col2 = st.columns(2)
        
        veg_items_left = [
            "MANGO AVAKAYA PICKLE",
            "BELLAM AVAKAYA PICKLE",
            "CORIANDER PICKLE",
            "RED CHILLI PICKLE",
            "MANGO THOKKU PICKLE",
            "GINGER PICKLE",
            "CURRY LEAVES PICKLE",
            "GARLIC PICKLE",
            "DRUMSTICKS PICKLE",
            "GREEN CHILLI PICKLE",
            "LEMON PICKLE",
            "TOMATO PICKLE",
            "CHINTAPANDU PICKLE"
        ]
        
        veg_items_right = [
            "BITTER GOURD PICKLE",
            "GONGURA PICKLE",
            "AMLA PICKLE",
            "CAULIFLOWER PICKLE",
            "PUDINA PICKLE",
            "DABBAKAYA PICKLE",
            "NALLERUKADA PICKLE",
            "RED CHILLI GONGURA",
            "VANKAYA PICKLE",
            "KANDA PICKLE",
            "PHOOL MAKHANA PICKLE",
            "CHIKKUDU KAYA PICKLE",
            "CHINTAKAYA PICKLE"
        ]
        
        with v_col1:
            for item in veg_items_left:
                st.markdown(f"- 🥭 **{item}**")
        with v_col2:
            for item in veg_items_right:
                st.markdown(f"- 🥭 **{item}**")

    # 3. Karappodulu & Vadiyalu Tab
    with menu_tabs[2]:
        kp_col1, kp_col2 = st.columns(2)
        
        with kp_col1:
            st.markdown("<h3 style='color: #8B0000;'>Traditional Karappodulu</h3>", unsafe_allow_html=True)
            karappodulu = [
                "RICE KARAPPODI",
                "IDLY KARAPPODI",
                "KANDI KARAPPODI",
                "MUNAGAKU KARAPPODI",
                "KAKARA KARAPPODI",
                "KARIVEPAKU KARAPPODI",
                "PALLI KARAPPODI",
                "NUVVULA KARAPPODI",
                "GARLIC KARAPPODI",
                "PUTNALA KARAPPODI",
                "AVISEGINJALA KARAPPODI",
                "DRY PRAWN KARAPPODI"
            ]
            for kp in karappodulu:
                st.markdown(f"- 🌶️ **{kp}**")
                
        with kp_col2:
            st.markdown("<h3 style='color: #8B0000;'>Authentic Homemade Vadiyalu</h3>", unsafe_allow_html=True)
            vadiyalu = [
                "RICE VADIYALU",
                "CARROT VADIYALU",
                "BEETROOT VADIYALU",
                "TOMATO VADIYALU",
                "RAGI VADIYALU",
                "MUNAGAKU VADIYALU",
                "KARIVEPAKU VADIYALU",
                "PUDINA VADIYALU",
                "KOTTIMEERA VADIYALU",
                "PESARA VADIYALU",
                "MINAPA VADIYALU",
                "GUMMADI VADIYALU"
            ]
            for vad in vadiyalu:
                st.markdown(f"- 🍘 **{vad}**")

    # 4. Special Items Tab
    with menu_tabs[3]:
        st.markdown("<h3 style='color: #8B0000;'>Pure & Natural Special Items</h3>", unsafe_allow_html=True)
        specials = [
            ("PURE HONEY", "100% natural, unprocessed forest honey.", "🍯"),
            ("PURE GHEE", "Traditional homemade bilona cow & buffalo ghee.", "🧈"),
            ("COLD PRESSED PALLI OIL", "Wood cold-pressed unrefined groundnut cooking oil.", "🫒")
        ]
        
        for name, desc, icon in specials:
            st.markdown(f"""
            <div style="background-color: #fefce8; border-left: 4px solid #ca8a04; padding: 15px 20px; border-radius: 8px; margin-bottom: 12px;">
                <h4 style="margin: 0; color: #854d0e;">{icon} {name}</h4>
                <p style="margin: 5px 0 0 0; color: #713f12; font-size: 15px;">{desc}</p>
            </div>
            """, unsafe_allow_html=True)

    st.write("")

# ----------------- SECTION 4: UNIT FRANCHISE -----------------
elif menu_choice == "Unit Franchise":
    
    # ===== PART 1: TOP BANNER WITH BOLD 'UNIT FRANCHISE' =====
    franchise_bg_path = find_image("franchise_bg.png")
    encoded_franchise_bg = get_base64_image(franchise_bg_path)
    
    if encoded_franchise_bg:
        franchise_bg_style = f"background-image: linear-gradient(rgba(10, 10, 10, 0.70), rgba(10, 10, 10, 0.85)), url('data:image/png;base64,{encoded_franchise_bg}');"
    else:
        franchise_bg_style = "background: linear-gradient(135deg, #8B0000, #450a0a);"

    st.markdown(f"""
    <div style="
        {franchise_bg_style}
        background-size: cover;
        background-position: center;
        padding: 70px 25px;
        border-radius: 16px;
        text-align: center;
        color: white;
        margin-bottom: 35px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.4);
    ">
        <h1 style='color: #f59e0b; font-size: 50px; letter-spacing: 3px; font-weight: 900; margin: 0; text-transform: uppercase;'>
            UNIT FRANCHISE
        </h1>
        <p style='color: #fef08a; font-size: 20px; margin-top: 10px; font-style: italic; letter-spacing: 1px;'>
            Join Andhra's Most Famous Traditional Pickle & Homemade Food Brand
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # ===== PART 2: DETAILED FRANCHISE INFORMATION =====
    st.markdown("<h2 style='color: #8B0000; border-bottom: 3px solid #d97706; padding-bottom: 8px;'>About Franchise</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    With the aim of making the very popular pickles of **Godavari district** available to all the states of our country, **Picklemart** company is going to set up stores under the name **“PICKLE MART”** in all areas. This picklemart has more than 100 types of homemade non-veg pickles, veg pickles, pastries, karam podulu etc. which are famous in Andhra. Especially this Pickle Mart store has **Bhimavaram non-veg pickles** which are very famous in Andhra.

    In the preparation of these pickles, **without adding any preservatives, without using any machinery**, the pickles are made in our homes in the traditional Andhra methods, in a hygienic environment, in a handmade process. These pickles are stored only in **ceramic jars (Jaadi)** and sold fresh from the jars to the customers from time to time. Also, pickles are prepared using quality oils and other spices using **Guntur pepper from Andhra**, which is famous in our country. They have been following the same taste and quality standards for many years.
    """)
    
    st.markdown("<hr style='border: 1px dashed #d97706;'>", unsafe_allow_html=True)
    
    # Highlight Features Grid
    f_col1, f_col2 = st.columns(2, gap="large")
    
    with f_col1:
        st.markdown("""
        ### 🌟 Lucrative Business Opportunity
        Currently this company offers **PICKLE MART franchises in all states, all district centers, towns, rural areas, and all other areas of India**. 
        Those who are interested can use this franchise opportunity and earn good income. 

        - 💼 **Who Can Apply:** Entrepreneurs, unemployed youth, women, and retired employees can use this opportunity.
        - 👤 **Single Operator Model:** Even those who have no business experience can run this business alone; **no workers or extra staff are required**.
        - 💰 **High Profit Margin:** Enjoy an attractive profit margin of **15% to 25%** on total sales made in the outlet.
        - 🤝 **Zero Royalty Fee:** After taking a franchise, you **do not have to pay any royalty** to the company!
        - 📝 **Agreement Tenure:** The official franchise agreement is for a period of **3 years**.
        """)
        
    with f_col2:
        st.markdown("""
        ### 🏪 Investment & Provided Equipment
        **Franchise Fee:** **₹2,60,000/-** only (including Brand fee and Marketing fee).
        
        With this one-time fee, all the necessary equipment and branding materials for setting up the store will be fully provided:
        - 💡 **LED Name Board** & **Lollipop Sign Board**
        - ⚖️ **Commercial Digital Weighing Machine**
        - 🧾 **Computerized Billing Machine**
        - 📦 **Packing Machine & Quality Packing Material**
        - ✨ **Interior Display Glitter Boards**
        - 🏷️ **Product Stickers, Leaflets & Promotional Materials**
        """)
        
    st.markdown("<hr style='border: 1px dashed #d97706;'>", unsafe_allow_html=True)
    
    # Store Setup, Supply & Ongoing Support
    st.markdown("""
    ### 🏢 Shop Requirements & Continuous Company Support
    
    1. **Shop Space:**
       - A minimum of **150 sq. ft.** commercial shop has to be taken on rent.
       - The shop must feature the authentic Pickle Mart brand interior theme. Complete interior design guidance is provided by the company.
       
    2. **Regular Stock Supply:**
       - Pickle Mart directly supplies fresh pickles, powders, and authentic Andhra food items to your outlet regularly from time to time.
       
    3. **Professional Field Visits & Marketing Assistance:**
       - Expert teams including the **Sales Development Team, Marketing Team, Digital Marketing Team, Quality Control Team**, and dedicated **Business Development Representatives** regularly visit your outlet to take strategic steps to grow sales.
       
    4. **Comprehensive Training & Promotion:**
       - Full end-to-end training on daily store operations, customer service, and billing.
       - High-visibility local and online digital promotion support for your franchise.
       - Continuous business advice, strategic guidance, and mentoring whenever needed.
    """)
    
    st.write("")
    if st.button("👉 Apply for Unit Franchise Now", type="primary"):
        st.info("Please navigate to the 'Contact Us' section from the sidebar to submit your formal application!")
    st.write("")

# ----------------- SECTION 5: GALLERY (BLANK) -----------------
elif menu_choice == "Gallery":
    # Modified: Gallery is left as blank with an elegant placeholder title.
    st.markdown("<h1 style='text-align: center; color: #8B0000; letter-spacing: 2px;'>GALLERY</h1>", unsafe_allow_html=True)
    st.markdown("<div style='height: 4px; width: 100px; background: linear-gradient(90deg, #d97706, #b91c1c); margin: 0 auto 30px auto; border-radius: 2px;'></div>", unsafe_allow_html=True)
    st.write("")

# ----------------- SECTION 6: CONTACT US -----------------
elif menu_choice == "Contact Us":
    
    # ===== PART 1: BANNER WITH BOLD "PICKLE MART" & "CONTACT US" =====
    contact_bg_path = find_image("contact_bg.png")
    encoded_contact_bg = get_base64_image(contact_bg_path)
    
    if encoded_contact_bg:
        contact_bg_style = f"background-image: linear-gradient(rgba(10, 10, 10, 0.7), rgba(10, 10, 10, 0.82)), url('data:image/png;base64,{encoded_contact_bg}');"
    else:
        contact_bg_style = "background: linear-gradient(135deg, #7f1d1d, #450a0a);"

    st.markdown(f"""
    <div style="
        {contact_bg_style}
        background-size: cover;
        background-position: center;
        padding: 60px 20px;
        border-radius: 16px;
        text-align: center;
        color: white;
        margin-bottom: 30px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.35);
    ">
        <h1 style='color: #f59e0b; font-size: 54px; letter-spacing: 2px; font-weight: 900; margin-bottom: 5px; text-transform: uppercase;'>
            PICKLE MART
        </h1>
        <h2 style='color: #ffffff; font-size: 32px; font-weight: 800; margin-top: 0;'>
            CONTACT US
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    # ===== OUTREACH DETAILS =====
    st.markdown("""
    <div style="text-align: center; margin-bottom: 40px; padding: 25px; background-color: #fffdf5; border: 1px solid #fef08a; border-radius: 12px; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
        <h2 style="color: #8B0000; font-weight: bold; margin-top: 0; font-size: 32px;">Are You interested?</h2>
        <h3 style="color: #b45309; font-weight: 600; margin-bottom: 25px; font-size: 24px;">Come, Connect With Us!</h3>
        <div style="display: flex; flex-wrap: wrap; justify-content: center; gap: 40px;">
            <div style="min-width: 200px; padding: 15px 25px; background: white; border-radius: 8px; border-left: 5px solid #d97706; box-shadow: 0 1px 5px rgba(0,0,0,0.08);">
                <span style="font-size: 14px; text-transform: uppercase; color: #6b7280; font-weight: 600; letter-spacing: 1px; display: block;">For Franchise</span>
                <span style="font-size: 24px; color: #1e293b; font-weight: 800; display: block; margin-top: 5px;">+91 ***********</span>
            </div>
            <div style="min-width: 200px; padding: 15px 25px; background: white; border-radius: 8px; border-left: 5px solid #b91c1c; box-shadow: 0 1px 5px rgba(0,0,0,0.08);">
                <span style="font-size: 14px; text-transform: uppercase; color: #6b7280; font-weight: 600; letter-spacing: 1px; display: block;">Business with us</span>
                <span style="font-size: 24px; color: #1e293b; font-weight: 800; display: block; margin-top: 5px;">+91 ***********</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # ===== PART 2: FORM BASED EXACTLY ON USER'S IMAGE UPLOAD =====
    form_col1, form_col2, form_col3 = st.columns([1, 4, 1])
    
    with form_col2:
        # Styled Box to give the form a professional, slightly highlighted visual presence like the target graphic
        st.markdown("""
        <style>
        /* Target input borders and spacing similar to the provided mock */
        .stTextInput > div > div > input, .stTextArea > div > div > textarea {
            border: 1px solid #a8a29e !important;
            background-color: #f3f4f6 !important;
            border-radius: 4px !important;
            padding: 10px 14px !important;
            font-size: 16px !important;
        }
        .stTextInput > label, .stTextArea > label {
            color: #4b5563 !important;
            font-weight: 600 !important;
            font-size: 15px !important;
        }
        .stForm {
            border: none !important;
            padding: 0px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        with st.form("connect_contact_form", clear_on_submit=False):
            # Form field: First Name *
            st.markdown("<p style='margin-bottom: 2px; font-weight: 600; color: #475569;'>First Name <span style='color: #ef4444;'>*</span></p>", unsafe_allow_html=True)
            first_name = st.text_input("First Name", placeholder="E.g. John", label_visibility="collapsed")
            st.write("")
            
            # Form field: Email Address *
            st.markdown("<p style='margin-bottom: 2px; font-weight: 600; color: #475569;'>Email Address <span style='color: #ef4444;'>*</span></p>", unsafe_allow_html=True)
            email_address = st.text_input("Email Address", placeholder="E.g. john@doe.com", label_visibility="collapsed")
            st.write("")
            
            # Form field: Phone Number
            st.markdown("<p style='margin-bottom: 2px; font-weight: 600; color: #475569;'>Phone Number</p>", unsafe_allow_html=True)
            phone_number = st.text_input("Phone Number", placeholder="E.g. +1 3004005000", label_visibility="collapsed")
            st.write("")
            
            # Form field: Message
            st.markdown("<p style='margin-bottom: 2px; font-weight: 600; color: #475569;'>Message</p>", unsafe_allow_html=True)
            message = st.text_area("Message", placeholder="Enter your message...", max_chars=180, height=150, label_visibility="collapsed")
            
            # Form helper message character count indicator directly underneath visual match (bottom right check)
            st.markdown(f"<p style='text-align: right; font-size: 13px; color: #9ca3af; margin-top: 2px; margin-bottom: 20px;'>{len(message)} / 180</p>", unsafe_allow_html=True)
            
            # Form actions - styling a custom flat blue submit button
            submit_btn = st.form_submit_button("Send Message")
            
            if submit_btn:
                if first_name.strip() and email_address.strip():
                    st.markdown("""
                    <div style="background-color: #f0fdf4; color: #166534; padding: 12px 18px; border-radius: 6px; border: 1px solid #bbf7d0; font-size: 15px; margin-top: 15px;">
                        Message received! We will be in touch with you shortly.
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div style="background-color: #fef2f2; color: #991b1b; padding: 12px 18px; border-radius: 6px; border: 1px solid #fca5a5; font-size: 15px; margin-top: 15px;">
                        Please provide your First Name and Email Address to continue.
                    </div>
                    """, unsafe_allow_html=True)
    st.write("")
