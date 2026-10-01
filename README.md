# The Archive

**Pair:** *(Luis, Imelda)* **Repository:** *(https://github.com/AfricanOlympiadAcademy/archive.git)*

> This file is Part E of the assignment — **15 marks**. Replace every placeholder below. Delete the instruction lines in italics as you go. Marks come from the reasoning, not the length.

---

## 1\. The record *(3 marks)*

*What one manuscript looks like in our system, and what we do when a field is unknown.*

| Field | Type | Example | If it is unknown, we… |
| --- | --- | --- | --- |
| id | string | `MS001` |Raise an error  |
| title | string | "Tarikh al-Sudan" | Raise an error |
| city |  string| "Timbuktu"|Raise an error|
| year | integer | 1655 | Raise an error |
| condition | string |"fragile" |Raise an error  |

---

## 2\. Our validation rules *(4 marks)*

| Field | Rule(s) | Rejects (example) |
| --- | --- | --- |
| id |length has to be 5 and first two letters:MS and the rest three characters must be 3 | MS0012 |
| title |checks the length if it is too short("3 characters not counting white space>"), if not it rejects it | A |
| city |if it is not in known cities without depending on capitalization then it gives an error | kano |
| year |strip out the white space and see if it is in the year range and also of it has the correct characters which are numbers  | c.1560 |
| condition | if it is the valid conditions we accept, if it is not we reject it | excellent |

### Who decided the year range?

*The brief gave you 1100–1900. That was a decision someone made, and it has costs. 1900 excludes a modern copy of an old text. 1100 excludes anything earlier. State whether you accept these bounds or would change them, and say what your choice throws away. An undefended range scores 1 of the 4 marks.*

We choose 1100-2026 as our range" we chose 2026 because we want to include current records because we do not want to use old data, the current data matters. we do not want to include anything before 1100 because it would be outdated and would not help us much in the modern world.

---

## 3\. The `c.1590` decision *(3 marks)*

*Record MS009 in* `data/messy.csv` has the year `c.1590` — circa, approximately. Manuscript dating is often approximate, and a scholar may genuinely only know the decade. Your program currently rejects it, so the record is lost.

*Choose one and argue for it:*

- **(a)** Reject it. Only exact years enter the catalogue.
- **(b)** Store the year as text, so anything can be recorded.
- **(c)** Store `1590` plus a separate `approximate` flag.

**Our choice:*store the year as text, so anything can be recorded*

**Why:**

**What it costs us:**

---

## 4\. Our test table *(3 marks)*

### `validate_year`

| Test data | Value | Expected | Actual | Pass? |
| --- | --- | --- | --- | --- |
| Normal | 1655 | valid |  |  |
| Abnormal |  |  |  |  |
| Extreme (low) | 1100 | valid |  |  |
| Extreme (high) |  |  |  |  |
| Boundary (below) | 1099 | invalid |  |  |
| Boundary (above) |  |  |  |  |

### `_______________` *(one other field of your choice)*

| Test data | Value | Expected | Actual | Pass? |
| --- | --- | --- | --- | --- |

---

## 5\. Collaboration reflection *(2 marks)*

*One paragraph each, written separately and signed. Do not write these together — the point is two honest accounts.*

***(partner 1 name)*:** One thing my partner did that I will steal: One thing I would do differently next time:

***(partner 2 name)*:** One thing my partner did that I will steal: One thing I would do differently next time:

---

## 6\. Declaration

*Required. See the integrity section of the brief.*

- [ ] Both of us can explain every line in this repository.

- [ ] AI assistants used for explanation only, not to generate our implementation or our tests.

**If you used an AI assistant, say what you asked and what you did with the answer:**

---

## Running this project

```bash
pytest -v                              # all tests
pytest tests/test_provided.py -v       # the given suite
pytest tests/test_yours.py -v          # your suite
python tools/check_collaboration.py    # your Part C report
```

[Link to the submission form](https://docs.google.com/forms/d/e/1FAIpQLSdO4trwNU4zPusr33LfYRhH2jvijj7sY42svbumH6f_15rCAQ/viewform?usp=preview)