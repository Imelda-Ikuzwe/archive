"""Reading and writing the Archive file.

"""

from archive.errors import MalformedRecordError

FIELD_NAMES = ["id", "title", "city", "year", "condition"]

def parse_line(line):
   
    if not line.strip(): return None
    fields = [f.strip() for f in line.strip().split(',')]
    if len(fields) != 5:
        raise MalformedRecordError(f"Line does not contain exactly 5 fields: {line}")
    return dict(zip(FIELD_NAMES, fields))


    #raise NotImplementedError("parse_line")


def load_archive(path):
    """Read the file at `path` and return (valid_records, rejected_lines).
    """
    valid_records = []
    rejected_lines = []
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            for original_line in f:
                if not original_line.strip():
                    continue
                try:
                    record = parse_line(original_line)
                    if record:
                        valid_records.append(record)
                except MalformedRecordError:
                    rejected_lines.append(original_line)
    except FileNotFoundError:
        return [], []
        
    return valid_records, rejected_lines
    


    #raise NotImplementedError("load_archive")


def save_archive(path, records):
    """Write every record to `path` as CSV, one per line, no header.
    """
    with open(path, 'w', encoding='utf-8') as f:
        for record in records:
            row = [str(record.get(field, '')) for field in FIELD_NAMES]
            f.write(','.join(row) + '\n')
    return None
    #raise NotImplementedError("save_archive")
 