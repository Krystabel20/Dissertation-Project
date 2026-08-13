# Answers at or above these levels count as a "flag"
FREQ_FLAG = {"Often", "Almost always"}
DEGREE_FLAG = {"Moderately", "Significantly"}
IMPACT_FLAG = {"Moderate", "Significant"}

print("Flag levels loaded")

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


print("Counting functions loaded")

def route(g, female_ans, male_ans):
    general = count_general_flags(g)
    clinical = count_female_flags(female_ans) + count_male_flags(male_ans)
    has_condition = g.get("limiting_condition") == "Yes"
    has_diagnosis = len(g.get("diagnoses", [])) > 0
    on_medication = g.get("medication") == "Yes"

    # Outcome A: needs clinical assessment
    if has_condition or has_diagnosis or general >= 3 or clinical >= 2:
        return "A"

    # Outcome B: GP alongside general guidance
    if general >= 1 or clinical == 1 or on_medication:
        return "B"

    # Outcome C: lifestyle guidance, no referral
    return "C"


print("Routing function loaded")

def clear_general(**overrides):
    base = {
        "fatigue": "Never", "hard_lose": "No", "abdominal": "Never",
        "pain": "Never", "limiting_condition": "No", "medication": "No",
        "diagnoses": [],
    }
    base.update(overrides)
    return base


def clear_female(**overrides):
    base = {
        "periods": "No", "hair": "No", "acne": "No", "hormonal": "No",
        "pcos_dx": "No", "ovaries": "No", "impact": "None",
    }
    base.update(overrides)
    return base


def clear_male(**overrides):
    base = {
        "muscle": "No", "libido": "Never", "low_t": "No", "hormone": "No",
        "composition": "No", "impact": "None",
    }
    base.update(overrides)
    return base


# Quick check: a fully clear person should route to C
test_person = clear_general()
result = route(test_person, clear_female(), clear_male())
print("Clear person routes to:", result, "(should be C)")

# Each test: (description, general answers, female answers, male answers, expected outcome)
TESTS = [
    ("No symptoms at all",
     clear_general(), clear_female(), clear_male(), "C"),

    ("Condition limiting activity",
     clear_general(limiting_condition="Yes"), clear_female(), clear_male(), "A"),

    ("Existing diabetes diagnosis",
     clear_general(diagnoses=["Type 2 diabetes"]), clear_female(), clear_male(), "A"),

    ("Three general symptoms",
     clear_general(fatigue="Often", hard_lose="Significantly", abdominal="Often"),
     clear_female(), clear_male(), "A"),

    ("Woman with clear PCOS signs",
     clear_general(),
     clear_female(periods="Yes", pcos_dx="Yes", hair="Significantly"),
     clear_male(), "A"),

    ("Man with low testosterone and abnormal hormones",
     clear_general(), clear_female(),
     clear_male(low_t="Yes", hormone="Yes"), "A"),

    ("One mild general symptom",
     clear_general(fatigue="Often"), clear_female(), clear_male(), "B"),

    ("On weight-affecting medication only",
     clear_general(medication="Yes"), clear_female(), clear_male(), "B"),

    ("Woman with a single clinical sign",
     clear_general(), clear_female(acne="Yes"), clear_male(), "B"),

    ("Man with one notable symptom",
     clear_general(), clear_female(),
     clear_male(muscle="Significantly"), "B"),
]

print(f"{len(TESTS)} test cases loaded")

print("\nRunning tests")
print("=" * 55)

passed = 0
for i, (description, g, f, m, expected) in enumerate(TESTS, 1):
    got = route(g, f, m)
    if got == expected:
        passed += 1
        status = "PASS"
    else:
        status = "FAIL"
    print(f"Test {i:2d}  expected {expected}  got {got}  {status}")
    print(f"         {description}")

print("=" * 55)
print(f"{passed} of {len(TESTS)} tests passed")
