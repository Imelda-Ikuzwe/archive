# The Archive

**Pair:** Luis & Imelda  **Repository:** https://github.com/Imelda-Ikuzwe/archive.git

---

## 1. The record

| Field | Type | Example | If it is unknown, we… |
| --- | --- | --- | --- |
| id | string | `MS001` | Raise an error |
| title | string | "Tarikh al-Sudan" | Raise an error |
| city | string | "Timbuktu" | Raise an error |
| year | integer| 1655 | Raise an error |
| condition | string | "fragile" | Raise an error |

---

## 2. Our validation rules

| Field | Rule(s) | Rejects (example) |
| --- | --- | --- |
| id | Must start with "MS" followed by exactly 3 numbers | `MS0012` |
| title | Must have at least 3 non-space characters | `A` |
| city | Must be in our recognized list of cities (case doesn't matter) | `kano` |
| year | Must be digits only and fall between 1100 and 1900 inclusive | `c.1560` |
| condition | Must be one of our supported condition labels | `excellent` |

### Who decided the year range?

We decided to keep the 1100–1900 range because it accurately frames the historical era of the Timbuktu collection. The main drawback is that it forces us to toss out legitimate materials on both ends—anything pre-1100 gets excluded, as well as 20th-century copies or restorations of older manuscripts that scholars still care about.

---

## 3. The `c.1590` decision

**Our choice:** Reject it. Only exact years enter the catalogue.

**Why:** Allowing text strings into our year field breaks mathematical operations down the line, like sorting chronologically or checking date boundaries. Keeping years strictly numeric avoids bad data sneaking into calculations.

**What it costs us:** We lose any manuscript where historians only have an approximate era (like `c.1590`). In practice, this means throwing away valuable records just because their creation date isn't exact.

---

## 4. Our test table

### `validate_year`

| Test data | Value | Expected | Actual | Pass? |
| --- | --- | --- | --- | --- |
| Normal | 1655 | valid | valid | Pass |
| Abnormal | c.1789 | invalid | invalid | Pass |
| Extreme (low) | 1100 | valid | valid | Pass |
| Extreme (high) | 1900 | valid | valid | Pass |
| Boundary (below) | 1099 | invalid | invalid | Pass |
| Boundary (above) | 1901 | invalid | invalid | Pass |

### `validate_title`

| Test data | Value | Expected | Actual | Pass? |
| --- | --- | --- | --- | --- |
| Normal | "Tarikh al-Sudan" | valid | valid | Pass |
| Short | "A" | invalid | invalid | Pass |

---

## 5. Collaboration reflection

**Luis:** One thing I'm taking from Imelda is she structured the functions in storage; making it extra clear to any reader with very efficient techniques. One thing that I will do next time is to add more comments in my work to avoid misundertandings. I will also structure my code clearer.

**Imelda:** I think that Luis really put in a lot of work, and we worked really well on this, he is collaborating well.
---

## 6. Declaration

- [Yes] Both of us can explain every line in this repository.
- [Yes] AI assistants used for explanation only, not to generate our implementation or our tests.

**AI Usage Details:**
We used AI to look up built-in Python string methods, clarify context manager syntax, and help us understand specific exception behaviors during testing.

---

## Running this project

```bash
pytest -v                              # all tests
pytest tests/test_provided.py -v       # the given suite
pytest tests/test_yours.py -v          # your suite
python tools/check_collaboration.py    # your Part C report