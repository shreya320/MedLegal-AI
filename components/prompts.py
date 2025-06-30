def build_main_prompt(context: str, scenario: str) -> str:
    return f"""
You are a medico-legal assistant trained on Indian medical law and ethics.

Given the CONTEXT and SCENARIO below, provide clear, concise, and professional guidance **to the doctor**.

Write in second-person perspective (e.g., "You must...", "You are required to...").
Present the information in a neat format, highlighting the headings. 
Include:
- Duties
- Documentation required
- Legal risks involved

Also return:
- Legal Risk Rating: High / Medium / Low
- Bullet points of key documentation
- Applicable legal forms (if any)

⚠️ Use only the context provided. If context is insufficient, clearly state so. Do not make up information.

--------------------
CONTEXT:
{context}
--------------------

SCENARIO:
{scenario.strip()}
"""


def build_followup_prompt(scenario, answer, followup):
    return f"""
The previous scenario was:
\"\"\"{scenario.strip()}\"\"\"

The AI responded with:
\"\"\"{answer}\"\"\"

Now the user wants to follow up with:
\"{followup}\"

Provide a concise, professional legal-ethical response. Continue contextually.
"""

def build_doc_prompt(scenario):
    return f"""
Based on the clinical-legal scenario below, provide a bullet-point list of exactly what the doctor should **document** to ensure legal compliance and safety.

SCENARIO: {scenario.strip()}
"""

