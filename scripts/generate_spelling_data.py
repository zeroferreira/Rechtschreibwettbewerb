import json
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET


MAIN_NS = "http://schemas.openxmlformats.org/spreadsheetml/2006/main"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"


def _col_row(cell_ref: str):
    m = re.match(r"^([A-Z]+)(\d+)$", cell_ref)
    if not m:
        return None, None
    return m.group(1), int(m.group(2))


def _read_shared_strings(z: zipfile.ZipFile):
    if "xl/sharedStrings.xml" not in z.namelist():
        return []
    root = ET.fromstring(z.read("xl/sharedStrings.xml"))
    ns = {"m": MAIN_NS}
    shared = []
    for si in root.findall("m:si", ns):
        texts = []
        for t in si.findall(".//m:t", ns):
            texts.append(t.text or "")
        shared.append("".join(texts))
    return shared


def _cell_value(c, shared_strings):
    ns = {"m": MAIN_NS}
    t = c.get("t")
    if t == "inlineStr":
        t_el = c.find(".//m:t", ns)
        return (t_el.text or "") if t_el is not None else ""
    v_el = c.find("m:v", ns)
    if v_el is None:
        return ""
    raw = v_el.text or ""
    if t == "s":
        try:
            return shared_strings[int(raw)]
        except Exception:
            return raw
    return raw


def _read_sheet_cells(z: zipfile.ZipFile, sheet_path: str):
    ns = {"m": MAIN_NS}
    shared = _read_shared_strings(z)
    root = ET.fromstring(z.read(sheet_path))
    out = {}
    for c in root.findall(".//m:c", ns):
        ref = c.get("r")
        if not ref:
            continue
        col, row = _col_row(ref)
        if row is None:
            continue
        val = _cell_value(c, shared).strip()
        if val == "":
            continue
        out[(row, col)] = val
    return out


def extract_words_from_xlsm(xlsm_path: str):
    with zipfile.ZipFile(xlsm_path) as z:
        cells = _read_sheet_cells(z, "xl/worksheets/sheet1.xml")

    words = []
    rows = sorted({r for (r, _c) in cells.keys() if r >= 5})
    for r in rows:
        word = cells.get((r, "B"), "").strip()
        if not word:
            continue
        definition = cells.get((r, "C"), "").strip()
        example = cells.get((r, "D"), "").strip()
        words.append(
            {
                "word": word,
                "phonetic": "",
                "definition": definition,
                "example": example,
            }
        )

    return words


def write_spelling_data_js(out_path: str, language: str, words):
    payload = {
        "language": language,
        "levelAWords": words,
    }
    js = "window.SPELLING_DATA = " + json.dumps(payload, ensure_ascii=False, indent=2) + ";\n"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(js)


def main():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    targets = [
        {
            "xlsm": os.path.join(root_dir, "French", "Spelling Français 2025.xlsm"),
            "out": os.path.join(root_dir, "French", "spelling-data.js"),
            "language": "fr-FR",
        },
        {
            "xlsm": os.path.join(root_dir, "German", "Spelling Deutsch 2025.xlsm"),
            "out": os.path.join(root_dir, "German", "spelling-data.js"),
            "language": "de-DE",
        },
    ]

    for t in targets:
        words = extract_words_from_xlsm(t["xlsm"])
        write_spelling_data_js(t["out"], t["language"], words)
        print(f"Wrote {t['out']} ({len(words)} words)")


if __name__ == "__main__":
    sys.exit(main())

