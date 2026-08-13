import streamlit as st

st.set_page_config(page_title="Weight Management Support Tool")

st.title("Physical Activity and Weight Management Support Tool")
st.caption(
    "An educational prototype. It offers indicative guidance only and does not "
    "provide a medical diagnosis. Always consult a qualified healthcare "
    "professional about personal health concerns."
)
from datetime import date

st.header("Stage 1: About you")

dob = st.date_input(
    "Date of birth",
    min_value=date(1920, 1, 1),
    max_value=date.today(),
    value=date(1990, 1, 1),
)
age = (date.today() - dob).days // 365

gender = st.radio("Gender", ["Female", "Male", "Prefer not to say"])

height_cm = st.number_input("Height (cm)", min_value=120, max_value=220, value=170)
weight_kg = st.number_input("Weight (kg)", min_value=35, max_value=250, value=75)
bmi = weight_kg / ((height_cm / 100) ** 2)

activity = st.selectbox(
    "How would you describe your current physical activity level?",
    ["Inactive", "Fairly active", "Active", "Very active"],
)

st.info(f"Calculated age: {age}    Calculated BMI: {bmi:.1f}")

st.header("Stage 2: Your health history")

st.header("Your health history")
st.write("These questions help us understand your general health.")

FREQ = ["Never", "Occasionally", "Often", "Almost always"]
DEGREE = ["Not at all", "Slightly", "Moderately", "Markedly"]
YESNO = ["No", "Yes", "Unsure"]

g = {}

g["fatigue"] = st.radio(
    "Do you experience persistent fatigue or low energy that is unrelated to how well you sleep?",
    FREQ, horizontal=True)

g["hard_lose"] = st.radio(
    "Do you find it difficult to lose weight despite consistent effort?",
    DEGREE, horizontal=True)

g["abdominal"] = st.radio(
    "Have you noticed unexplained weight gain around your middle?",
    FREQ, horizontal=True)

g["diagnoses"] = st.multiselect(
    "Have you been diagnosed with any of the following conditions? Select any that apply.",
    ["Type 2 diabetes", "Pre-diabetes", "Hypothyroidism", "Insulin resistance"])

g["medication"] = st.radio(
    "Are you currently taking any medication known to affect weight or metabolism?",
    YESNO, horizontal=True)

g["pain"] = st.radio(
    "Do you experience discomfort or pain during activity that limits what you can do?",
    FREQ, horizontal=True)

st.header("Your body and lifestyle")
st.write(
    "These questions help us understand what your body can comfortably handle, "
    "so any guidance we give suits you personally."
)

# Physical capacity
g["cardiac_resp"] = st.radio(
    "Have you been diagnosed with a heart or respiratory condition that affects "
    "how much exercise you can do?",
    YESNO, horizontal=True)

g["breathless"] = st.radio(
    "Do you become breathless during mild or moderate activity?",
    FREQ, horizontal=True)

g["mobility"] = st.radio(
    "Do you have any joint, mobility, or musculoskeletal limitations?",
    YESNO, horizontal=True)

g["mobility_detail"] = st.text_input(
    "If so, could you tell us a little more? (optional)")

# Food allergies
g["allergies"] = st.multiselect(
    "Do you have any food allergies? Select any that apply.",
    ["Nuts", "Dairy", "Gluten", "Shellfish", "Eggs", "Soya"])

g["allergies_other"] = st.text_input(
    "Any other allergies not listed above? (optional)")

# Food intolerances
g["intolerances"] = st.multiselect(
    "Are there foods that cause you discomfort, such as indigestion, heartburn, "
    "or an upset stomach? Select any that apply.",
    ["Dairy", "Spicy food", "Fried or fatty food", "Gluten", "Caffeine"])

g["intolerances_other"] = st.text_input(
    "Any other foods that disagree with you? (optional)")

# Dislikes
g["dislikes"] = st.text_input(
    "Are there any foods you strongly dislike or prefer to avoid? (optional)")

# Exercise setting preference
g["setting"] = st.radio(
    "When it comes to exercise, what do you prefer?",
    ["Indoors", "Outdoors", "Both", "No preference"], horizontal=True)

IMPACT = ["None", "Mild", "Moderate", "Significant"]

def ask_female():
    st.write("Thank you. A few questions about your hormonal health can help us understand your body better.")
    f = {}
    f["periods"] = st.radio(
        "Are your menstrual periods irregular, infrequent, or absent?",
        YESNO, horizontal=True, key="f1")
    f["hair"] = st.radio(
        "Have you noticed excess hair growth on your face or body?",
        DEGREE, horizontal=True, key="f2")
    f["acne"] = st.radio(
        "Do you experience persistent acne that is difficult to manage?",
        YESNO, horizontal=True, key="f3")
    f["hormonal"] = st.radio(
        "Have you been told by a clinician that you have a hormonal imbalance?",
        YESNO, horizontal=True, key="f4")
    f["pcos_dx"] = st.radio(
        "Have you been diagnosed with polycystic ovary syndrome?",
        YESNO, horizontal=True, key="f5")
    f["cyclical"] = st.radio(
        "Do you find your weight harder to manage at particular points in your cycle?",
        YESNO, horizontal=True, key="f6")
    f["fertility"] = st.radio(
        "Have you experienced difficulties or concerns relating to fertility?",
        ["No", "Yes", "Prefer not to say"], horizontal=True, key="f7")
    f["ovaries"] = st.radio(
        "Have you been told, following a scan, that you have polycystic ovaries?",
        YESNO, horizontal=True, key="f8")
    f["mood"] = st.radio(
        "Do you notice changes in your mood that seem connected to your physical health?",
        FREQ, horizontal=True, key="f9")
    f["impact"] = st.radio(
        "How much do these symptoms affect your daily life?",
        IMPACT, horizontal=True, key="f10")
    return f

def ask_male():
    st.write("Thank you. A few questions about your hormonal health can help us understand your body better.")
    m = {}
    m["muscle"] = st.radio(
        "Have you noticed a reduction in muscle mass or strength, despite staying active?",
        DEGREE, horizontal=True, key="m1")
    m["libido"] = st.radio(
        "Have you been experiencing low mood, motivation, or reduced libido?",
        FREQ, horizontal=True, key="m2")
    m["abdominal_m"] = st.radio(
        "Do you gain weight around your abdomen even when you remain active?",
        FREQ, horizontal=True, key="m3")
    m["low_t"] = st.radio(
        "Have you been diagnosed with low testosterone?",
        YESNO, horizontal=True, key="m4")
    m["energy"] = st.radio(
        "Do you experience low energy that your lifestyle does not explain?",
        FREQ, horizontal=True, key="m5")
    m["concentration"] = st.radio(
        "Have you noticed difficulty with concentration or mental clarity?",
        FREQ, horizontal=True, key="m6")
    m["hormone"] = st.radio(
        "Have you been told your hormone levels are outside the normal range?",
        YESNO, horizontal=True, key="m7")
    m["composition"] = st.radio(
        "Have you seen your body change shape without a change in your lifestyle?",
        DEGREE, horizontal=True, key="m8")
    m["impact"] = st.radio(
        "How much do these symptoms affect your daily life?",
        IMPACT, horizontal=True, key="m9")
    return m

female_ans, male_ans = {}, {}
if gender == "Female":
    female_ans = ask_female()
elif gender == "Male":
    male_ans = ask_male()
else:
    female_ans = ask_female()
    male_ans = ask_male()

FREQ_FLAG = {"Often", "Almost always"}
DEGREE_FLAG = {"Moderately", "Significantly"}
IMPACT_FLAG = {"Moderate", "Significant"}

FREQ_FLAG = {"Often", "Almost always"}
DEGREE_FLAG = {"Moderately", "Markedly", "Significantly"}
IMPACT_FLAG = {"Moderate", "Significant"}

def count_general_flags(g):
    flags = 0
    if g.get("fatigue") in FREQ_FLAG:
        flags += 1
    if g.get("hard_lose") in DEGREE_FLAG:
        flags += 1
    if g.get("abdominal") in FREQ_FLAG:
        flags += 1
    if g.get("pain") in FREQ_FLAG:
        flags += 1
    return flags

def count_female_flags(f):
    flags = 0
    for key in ["periods", "acne", "hormonal", "pcos_dx", "ovaries"]:
        if f.get(key) == "Yes":
            flags += 1
    if f.get("hair") in DEGREE_FLAG:
        flags += 1
    if f.get("impact") in IMPACT_FLAG:
        flags += 1
    return flags

def count_male_flags(m):
    flags = 0
    for key in ["low_t", "hormone"]:
        if m.get(key) == "Yes":
            flags += 1
    if m.get("muscle") in DEGREE_FLAG:
        flags += 1
    if m.get("libido") in FREQ_FLAG:
        flags += 1
    if m.get("composition") in DEGREE_FLAG:
        flags += 1
    if m.get("impact") in IMPACT_FLAG:
        flags += 1
    return flags

def build_food_plan(g):
    """Suggest foods to favour, excluding the person's allergies, intolerances and dislikes."""
    exclude = set()
    for item in g.get("allergies", []) + g.get("intolerances", []):
        exclude.add(item.lower())
    for text in [g.get("allergies_other", ""), g.get("intolerances_other", ""), g.get("dislikes", "")]:
        for word in text.lower().replace(",", " ").split():
            exclude.add(word)

    # Candidate healthy foods, each tagged so we can screen them out
    candidates = [
        ("Bananas", {"banana"}),
        ("Berries", {"berry", "berries", "strawberry", "blueberry"}),
        ("Apples", {"apple"}),
        ("Oranges and citrus", {"orange", "citrus"}),
        ("Leafy greens such as spinach", {"spinach", "greens"}),
        ("Oily fish such as salmon", {"fish", "salmon", "shellfish"}),
        ("Eggs", {"egg", "eggs"}),
        ("Greek yoghurt", {"dairy", "yoghurt"}),
        ("Wholegrain oats", {"gluten", "oats"}),
        ("Lentils and beans", {"beans", "lentils"}),
        ("Nuts and seeds", {"nuts", "nut", "seeds"}),
        ("Chicken or turkey", {"chicken", "turkey"}),
    ]
    favour = [name for name, tags in candidates if not (tags & exclude)]
    return favour[:8]

def show_plan(g, activity):
    """Show a tailored exercise and dietary plan (Outcomes B and C)."""
    cardiac = g.get("cardiac_resp") == "Yes"
    breathless = g.get("breathless") in FREQ_FLAG
    mobility = g.get("mobility") == "Yes"
    setting = g.get("setting", "No preference")

    st.subheader("Moving more")
    if cardiac or breathless or mobility:
        st.write(
            "Because you have told us your body has some limits at the moment, gentler "
            "movement will suit you better than intense exercise. Building up to around "
            "8,000 steps a day at a comfortable pace is a realistic and well-evidenced "
            "goal, with rest whenever you need it. Please check with your GP before "
            "increasing your activity."
        )
        if setting == "Indoors":
            st.write("Indoor options: gentle seated exercises, short walks around the home, or a stationary bike at low resistance.")
        elif setting == "Outdoors":
            st.write("Outdoor options: flat, unhurried walks in a park, gradually extending the distance as you feel able.")
        else:
            st.write("You might mix short indoor walks on busy days with gentle outdoor walks when you have time.")
    else:
        st.write(
            "Aim to build gradually toward 150 minutes of moderate activity a week, such "
            "as brisk walking, cycling or swimming, with muscle strengthening on two days "
            "(Bull et al., 2020)."
        )
        if setting == "Indoors":
            st.write("Since you prefer indoors, home workouts, a gym, or a stationary bike would suit your routine.")
        elif setting == "Outdoors":
            st.write("Since you prefer outdoors, brisk walking, cycling or jogging outside would suit you well.")
        elif setting == "Both":
            st.write("As you are happy with either, you can do indoor workouts on work days and outdoor activity when you have more time.")

    st.subheader("Eating well")
    favour = build_food_plan(g)
    if favour:
        st.write(
            "Based on what agrees with your body, here are some foods to build meals "
            "around: " + ", ".join(favour) + "."
        )
    st.write(
        "Building up toward five portions of fruit and vegetables a day, and reducing "
        "ultra-processed foods, supports healthy weight independently of how active you "
        "are. Only around a third of adults in "
        "England currently manage five a day."
    )

st.header("Result")

if st.button("See my guidance"):

    general = count_general_flags(g)
    clinical = count_female_flags(female_ans) + count_male_flags(male_ans)
    has_diagnosis = len(g.get("diagnoses", [])) > 0
    on_medication = g.get("medication") == "Yes"
    cardiac = g.get("cardiac_resp") == "Yes"

    # Decide the outcome
    if has_diagnosis or cardiac or general >= 3 or clinical >= 2:
        outcome = "A"
    elif general >= 1 or clinical == 1 or on_medication:
        outcome = "B"
    else:
        outcome = "C"

    # Show the outcome
    if outcome == "A":
        st.error("**We would suggest speaking to your GP before making changes.**")
        st.write(
            "From what you have shared, there may be a health factor that is best "
            "reviewed by your GP before you change your activity or diet. They can "
            "look into this properly and advise you on the safest way forward."
        )
    elif outcome == "B":
        st.warning("**It would be worth speaking to your GP, alongside the guidance below.**")
        st.write(
            "Your answers suggest you can benefit from some changes, but it is worth "
            "checking in with your GP as you make them. The guidance below is a good "
            "place to begin."
        )
        show_plan(g, activity)
    else:
        st.success("**Here is some guidance tailored to you.**")
        st.write(
            "Nothing in your answers points to a health barrier standing in your way. "
            "The guidance below is suited to your body and preferences."
        )
        show_plan(g, activity)

    with st.expander("Why did I get this result?"):
        st.write(f"General symptoms noted: {general}")
        st.write(f"Clinical indicators noted: {clinical}")
        if has_diagnosis:
            st.write("You reported an existing diagnosis.")
        if cardiac:
            st.write("You reported a heart or respiratory condition affecting exercise.")
        if on_medication:
            st.write("You are taking medication that may affect weight.")

    st.caption(
        "This is a guidance tool, not a medical diagnosis. Please speak to a "
        "qualified healthcare professional about any health concerns."
    )