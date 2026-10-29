"""Summarises meeting notes with OpenAI. Test fixture for Cranium's VCS scan guide (Part A)."""

import os

from openai import OpenAI

MODEL = "gpt-4o-mini"

SYSTEM_PROMPT = "Summarise the meeting notes as three bullet points: decisions, owners, and open questions."


def summarise(notes: str) -> str:
    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": notes},
        ],
        temperature=0.2,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    print(summarise("Agreed to ship the scan schedule on Thursday. Max owns the test plan. Open: QA timing."))
