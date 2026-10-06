"""YOUR test suite — Part B (15 marks).

This file is graded by what it CATCHES, not by how much you write.

After the deadline your suite is run against five secret broken versions of
the Archive. Each contains exactly one realistic bug of a kind we have
discussed in class. You score 3 marks for each broken version your suite
detects — meaning at least one of your tests FAILS against it.

Two rules that decide whether you score at all:

  1. Your suite must PASS COMPLETELY against a correct implementation.
     A suite that fails everything "catches" all five bugs and scores ZERO.

  2. For validate_year you must include all four kinds of test data from
     Session 2: normal, abnormal, extreme, and boundary either side.

Where are the bugs? Where careless code always breaks: the edges. Test
1099/1100 and 1900/1901. Test empty strings and whitespace. Test a field
count that is wrong. Test upper case where you assumed lower.

Run yours with:   pytest tests/test_yours.py -v
"""

import pytest

from archive.errors import MalformedRecordError
from archive.storage import parse_line, load_archive, save_archive
from archive.validation import (
    validate_id,
    validate_title,
    validate_city,
    validate_year,
    validate_condition,
    validate_record,
)
from archive.queries import count_before, find_by_city, oldest, cities_summary

Sample = [
    {
        "id": "MS001",
        "title": "Tarikh al-Sudan",
        "city": "Timbuktu",
        "year": "1655",
        "condition": "fragile",
    },
    {
        "id": "MS002",
        "title": "Kitab al-Tara'if",
        "city": "Djenne",
        "year": "1590",
        "condition": "good",
    },
    {
        "id": "MS003",
        "title": "Risala fi'l-Nujum",
        "city": "TIMBUKTU",  # Uppercase city variant
        "year": "1548",
        "condition": "fragile",
    },
    {
        "id": "MS004",
        "title": "Tadhkirat al-Nisian",
        "city": "timbuktu",  # Lowercase city variant
        "year": "1548",       # Tie for oldest year (1548) with MS003
        "condition": "fair",
    },
    ]
# ====================================================== WORKED EXAMPLE
# The four kinds of test data from Session 2, shown on validate_condition.
# Study the PATTERN here, then apply it yourself to the other fields.
# These five are given. They are not enough to catch anything on their own.

def test_condition_normal():
    """NORMAL — an ordinary accepted value."""
    assert validate_condition("fragile")[0] is True


def test_condition_normal_other():
    """NORMAL — the other accepted values matter too."""
    assert validate_condition("good")[0] is True


def test_condition_abnormal():
    """ABNORMAL — a value of the wrong kind entirely."""
    assert validate_condition("excellent")[0] is False


def test_condition_empty():
    """ABNORMAL — nothing at all is still the wrong kind."""
    assert validate_condition("")[0] is False


def test_condition_case():
    """A rule the brief states: the check is case-insensitive."""
    assert validate_condition("GOOD")[0] is True


# ============================================= NOW DO THIS FOR validate_year
# Required for Part B. The year rules are where the marks are, because the
# year rules are where careless code breaks. Write all four kinds:
#
#   NORMAL     a year from the middle of the range
#   ABNORMAL   something that is not a year at all
#   EXTREME    1100 and 1900 — valid, sitting exactly on the edge
#   BOUNDARY   1099 and 1901 — one step outside, must be rejected
#
# TODO: write them here.
def test_year_normal():
    assert validate_year("1500")[0] is True

def test_year_abnormal():
    assert validate_year("not_a_year")[0] is False

def test_year_extreme():
    assert validate_year("1100")[0] is True
    assert validate_year("1900")[0] is True

def test_year_boundary():
    assert validate_year("1099")[0] is False
    assert validate_year("1901")[0] is False

# ============================================================== your tests
# Everything below is yours. Suggested coverage, in the order the marks are
# easiest to earn:
#
#   validate_id          format, length, case, empty
#   validate_title       whitespace-only, exactly 3 characters, shorter
#   validate_city        known, unknown, different case
#   validate_condition   each valid value, upper case, an invalid one
#   validate_record      a clean record, and one with several faults at once
#   parse_line           5 fields, 4 fields, 6 fields, whitespace around values
#   load_archive         missing file, the clean file, the messy file
#   save_archive         round trip: save then load gives back what you saved
#   queries              empty list, ties, case-insensitive city
def test_id_format():
    assert validate_id("MS123")[0] is True
    assert validate_id("ms123")[0] is False
    assert validate_id("M123")[0] is False
    assert validate_id("MS1234")[0] is False

def test_id_empty():
    assert validate_id("")[0] is False

def test_title_whitespace():
    assert validate_title("   ")[0] is False

def test_title_edgecase():
    assert validate_title("Try  ")[0] is True

def test_title_short():
    assert validate_title("ab       ")[0] is False

def test_city_known():
    assert validate_city("timbuktu")[0] is True

def test_city_unknown():
    assert validate_city("Abuja")[0] is False

def test_city_case():
    assert validate_city("tImBuKtU")[0] is True

def test_condition_valid_values():
    assert validate_condition("fragile")[0] is True
    assert validate_condition("good")[0] is True
    assert validate_condition("fair")[0] is True

def test_condition_uppercase():
    assert validate_condition("FRAGILE")[0] is True
    assert validate_condition("GOOD")[0] is True
    assert validate_condition("Fair")[0] is True

def test_condition_invalid():
    assert validate_condition("I was too lazy.")[0] is False



def test_record_clean():
    record = {
        "id": "MS123",
        "title": "A Great Manuscript",
        "city": "timbuktu",
        "year": "1500",
        "condition": "good"
    }
    assert validate_record(record) == []

def test_record_multiple_faults():
    record = {
        "id": "ms123",  # lowercase
        "title": "  ",  # whitespace only
        "city": "UnknownCity",  # not in known cities
        "year": "2087",  # out of range
        "condition": "excellent"  # invalid condition
    }
    reasons = validate_record(record)
    assert len(reasons) == 5  # Expecting 5 reasons for failure



def test_parse_line_splits_five_fields():
    got = parse_line("MS012,Ibn al-Sudan,Timbuktu,1755,fragile")
    assert got["id"] == "MS012"
    assert got["title"] == "Ibn al-Sudan"
    assert got["city"] == "Timbuktu"
    assert got["year"] == "1755"
    assert got["condition"] == "fragile"

def test_parse_line_raises_on_four_fields():
    with pytest.raises(MalformedRecordError):
        parse_line("MS003,Cannot find a title,Timbuktu,good")

def test_parse_line_raises_on_six_fields():
    with pytest.raises(MalformedRecordError):
        parse_line("MS208,Mali Manuscripts,Djenne,Mali,1644,fragile")

def test_parse_line_whitespace_around_values():
    got = parse_line("  MS012 ,Ibn al-Sudan  ,Timbuktu,  1755,fragile           ")
    assert got["id"] == "MS012"
    assert got["title"] == "Ibn al-Sudan"
    assert got["city"] == "Timbuktu"
    assert got["year"] == "1755"
    assert got["condition"] == "fragile"



def test_load_archive_missing_file_returns_empty():
    records, rejected = load_archive("I_know_this_is_not_here.csv")
    assert records == []
    assert rejected == []

def test_load_archive_reads_the_clean_file():
    records, rejected = load_archive("data/archive.csv")
    assert len(records) == 20
    assert rejected == []

def test_load_archive_reads_the_messy_file():
    records, rejected = load_archive("data/messy.csv")
    assert len(records) == 4
    assert rejected == ["MS007,Ta'rikh al-Fattash,Timbuktu,,fragile","MS008,Sharh al-Mukhtasar,Djenne,1644","MS009,Al-Durr al-Manzum,Gao,c.1590,fair","MS011,Tanbih al-Ikhwan,Timbuktu,2087,good","MS013,Nayl al-Ibtihaj,Chinguetti,1901,good","MS14,Kashf al-Ghumma,Gao,1655,good","MS015,Ab,Djenne,1580,fair","MS016,Tuhfat al-Nuzzar,Kano,1720,good","MS017,Minah al-Rabb,Timbuktu,1603,excellent"]


def test_save_and_load_round_trip():
    file_path = tmp_path / "archive_out.csv"
    save_archive(file_path,Sample)
    Good_records , Rejected = load_archive(file_path)
    assert Rejected == []
    assert Good_records == Sample


def test_queries_empty_list():
    assert count_before([], 1600) == 0
    assert find_by_city([], "TIMBUKTU") == []
    assert oldest([]) == None
    assert cities_summary([]) == []

def test_queries_ties():
    assert oldest(Sample) == {"id": "MS003","title": "Risala fi'l-Nujum","city": "TIMBUKTU","year": "1548","condition": "fragile"}

def test_queries_case_insensitive_city():
    assert find_by_city(Sample, "Timbuktu") == [
{
    "id": "MS001",
    "title": "Tarikh al-Sudan",
    "city": "Timbuktu",
    "year": "1655",
    "condition": "fragile",
},
{
    "id": "MS003",
    "title": "Risala fi'l-Nujum",
    "city": "TIMBUKTU",  # Uppercase city variant
    "year": "1548",
    "condition": "fragile",
},
{
    "id": "MS004",
    "title": "Tadhkirat al-Nisian",
    "city": "timbuktu",  # Lowercase city variant
    "year": "1548",       # Tie for oldest year (1548) with MS003
    "condition": "fair",
}]



