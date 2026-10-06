# The Archive

**Pair:** *(Luis, Imelda)* **Repository:** *(https://github.com/Imelda-Ikuzwe/archive.git)*

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
"""Reading and writing the Archive file.

YOU IMPLEMENT THIS FILE.

The file format is CSV with no header row. One record per line, five fields
separated by commas, in this order:

    id,title,city,year,condition
    MS001,Tarikh al-Sudan,Timbuktu,1655,fragile

Remember Session 1: a file is one long line of characters. The comma
separates fields; the newline separates records. Nothing else is doing
any work.
"""

from archive.errors import MalformedRecordError

FIELD_NAMES = ["id", "title", "city", "year", "condition"]

def parse_line(line):
   
    """Turn one CSV line into a dict with the five FIELD_NAMES as keys.

    Whitespace around the line (including the trailing newline) is stripped.
    Field values are stripped too.

    If the line does not split into exactly 5 fields, raise
    MalformedRecordError. Do not guess, do not pad with blanks — a line with
    four fields is not a record with an empty one, it is a broken line, and
    the difference matters when you report it to whoever typed it.

    Returns dict.
    """
    if not line.strip(): return None
    fields = [f.strip() for f in line.strip().split(',')]
    if len(fields) != 5:
        raise MalformedRecordError(f"Line does not contain exactly 5 fields: {line}")
    return dict(zip(FIELD_NAMES, fields))


    #raise NotImplementedError("parse_line")


def load_archive(path):
    """Read the file at `path` and return (valid_records, rejected_lines).

    valid_records   list of dicts that passed validate_record
    rejected_lines  list of the ORIGINAL line strings that did not — either
                    because they were malformed, or because validation
                    rejected them

    A file that does not exist is not an error. It means the archive is new.
    Return ([], []) and DO NOT raise. Your program must start on a machine
    where nobody has saved anything yet.

    Blank lines are skipped silently.

    Returns (list, list).
    """
    valid_records = []
    rejected_lines = []
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for original_line in f:
                # Blank lines are skipped silently
                if not original_line.strip():
                    continue
                try:
                    record = parse_line(original_line)
                    if record:
                        # Once you implement validate_record(record), add that check here:
                        # e.g., if validate_record(record):
                        valid_records.append(record)
                except MalformedRecordError:
                    rejected_lines.append(original_line)
    except FileNotFoundError:
        # A file that does not exist is not an error; returns empty lists
        return [], []
        
    return valid_records, rejected_lines
    


    #raise NotImplementedError("load_archive")


def save_archive(path, records):
    """Write every record to `path` as CSV, one per line, no header.

    Field order is FIELD_NAMES. The file is overwritten, not appended to.

    Returns None.
    """
    with open(path, 'w', encoding='utf-8') as f:
        for record in records:
            # Extract fields in exact order; default to empty string if a key is missing
            row = [str(record.get(field, '')) for field in FIELD_NAMES]
            # Join fields with commas and terminate the record with a newline character
            f.write(','.join(row) + '\n')
    return None
    #raise NotImplementedError("save_archive")
 
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