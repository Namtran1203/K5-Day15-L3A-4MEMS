"""Reproducible pain-mining script for Track C1 on DisneylandReviews.csv.

Runs locally using Python's standard library (zero LLM tokens).
Computes full-dataset keyword counts, draws a seeded sample CSV for manual
verification, and prints Markdown-ready summary tables for evidence/data-mining.md.

Usage:
    python evidence/count.py
    python evidence/count.py --sample-size 200 --seed 42
    python evidence/count.py --max-rating 3 --sample-size 200 --seed 42
"""
from __future__ import annotations

import argparse
import csv
import os
import random
import re
from collections import Counter

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_INPUT = os.path.join(REPO_ROOT, "data", "DisneylandReviews.csv", "DisneylandReviews.csv")
DEFAULT_OUT = os.path.join(REPO_ROOT, "evidence", "raw-sample-200.csv")

REQUIRED_COLUMNS = ("Review_ID", "Rating", "Year_Month", "Reviewer_Location", "Review_Text", "Branch")

PAIN_RULES: tuple[tuple[str, str, str], ...] = (
    (
        "queue_crowd",
        "Xep hang qua lau / qua dong khong choi kip",
        r"\b(long\s+(?:wait|waits|queue|queues|line|lines)|wait\s+time|waiting\s+(?:in\s+line|for\s+hours|\d+)|waited\s+(?:over|for|\d+)|overcrowded|too\s+crowded|way\s+too\s+busy)\b",
    ),
    (
        "schedule_show_hours",
        "Khong du thoi gian / lo show / tro choi dong bao tri",
        r"\b(not\s+enough\s+time|ran\s+out\s+of\s+time|missed\s+(?:the\s+)?(?:show|parade|fireworks|rides?)|closed\s+for\s+(?:refurbishment|maintenance|repairs?)|under\s+refurbishment|shut\s+down|opening\s+hours|closing\s+(?:early|time))\b",
    ),
    (
        "planning_navigation",
        "Phai tu lap ke hoach ky / roi thong tin / app hoac ban do kho dung",
        r"\b(plan\s+ahead|need\s+a\s+plan|itinerary|hard\s+to\s+navigate|wasted\s+(?:so\s+much\s+)?time|fast\s*pass|fastpass|app\s+(?:crash|broken|useless|confusing|didn.?t\s+work))\b",
    ),
    (
        "cost_budget",
        "Chi phi qua dat / cam giac khong xung dang ngan sach",
        r"\b(overpriced|way\s+too\s+expensive|too\s+expensive|rip\s*-?\s*off|waste\s+of\s+money|not\s+worth\s+(?:the\s+)?(?:money|price|it)|cost\s+a\s+fortune)\b",
    ),
    (
        "weather_restrictions",
        "Anh huong thoi tiet (mua/nang) hoac gioi han chieu cao tre nho",
        r"\b(rained\s+(?:out|all\s+day)|heavy\s+rain|cancelled\s+due\s+to\s+(?:rain|weather)|pouring\s+rain|too\s+hot|height\s+(?:limit|restriction|requirement)|too\s+short\s+for)\b",
    ),
)


def compile_rules() -> dict[str, re.Pattern[str]]:
    """Compile keyword regex patterns for each pain category."""
    return {name: re.compile(pattern, re.IGNORECASE) for name, _, pattern in PAIN_RULES}


def load_reviews(csv_path: str) -> list[dict[str, str]]:
    """Load reviews from CSV, falling back from UTF-8 to latin-1."""
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Khong tim thay file data: {csv_path}")

    for enc in ("utf-8-sig", "latin-1"):
        try:
            with open(csv_path, encoding=enc, newline="") as handle:
                reader = csv.DictReader(handle)
                fieldnames = tuple(reader.fieldnames or ())
                missing = [col for col in REQUIRED_COLUMNS if col not in fieldnames]
                if missing:
                    raise ValueError(f"Thieu cot trong CSV: {missing}")
                return list(reader)
        except UnicodeDecodeError:
            continue

    raise UnicodeDecodeError("latin-1", b"", 0, 1, "Khong doc duoc file CSV bang utf-8 hoac latin-1")


def parse_rating(value: str) -> int | None:
    """Parse integer rating safely, returning None when invalid."""
    try:
        return int(value.strip())
    except (AttributeError, ValueError):
        return None


def classify_review(text: str, compiled_rules: dict[str, re.Pattern[str]]) -> list[str]:
    """Return all pain categories matching the review text."""
    if not text:
        return []
    return [name for name, regex in compiled_rules.items() if regex.search(text)]


def count_pain_categories(
    rows: list[dict[str, str]],
    compiled_rules: dict[str, re.Pattern[str]],
) -> tuple[Counter[str], int]:
    """Count category hits and reviews matching at least one pain category."""
    cat_counts: Counter[str] = Counter()
    any_pain = 0
    for row in rows:
        tags = classify_review(row.get("Review_Text", ""), compiled_rules)
        if tags:
            any_pain += 1
            for tag in tags:
                cat_counts[tag] += 1
    return cat_counts, any_pain


def draw_sample(
    rows: list[dict[str, str]],
    sample_size: int,
    seed: int,
    max_rating: int | None = None,
) -> list[dict[str, str]]:
    """Filter rows by optional max_rating and draw a reproducible random sample."""
    pool = rows
    if max_rating is not None:
        pool = [
            row for row in rows
            if (rating := parse_rating(row.get("Rating", ""))) is not None and rating <= max_rating
        ]
    if sample_size <= 0 or sample_size >= len(pool):
        return list(pool)
    return random.Random(seed).sample(pool, sample_size)


def pain_excerpt(
    text: str,
    compiled_rules: dict[str, re.Pattern[str]],
    max_chars: int = 280,
) -> str:
    """Extract up to two sentences centered on the first matched pain phrase."""
    cleaned = " ".join((text or "").split())
    if not cleaned:
        return ""
    sentences = re.split(r"(?<=[.!?])\s+", cleaned)
    hit_idx = 0
    for idx, sent in enumerate(sentences):
        if any(regex.search(sent) for regex in compiled_rules.values()):
            hit_idx = idx
            break
    start = hit_idx
    excerpt = " ".join(sentences[start : start + 2]).strip()
    if len(excerpt) > max_chars:
        excerpt = excerpt[: max_chars - 3].rstrip() + "..."
    return excerpt


def write_sample_csv(
    rows: list[dict[str, str]],
    out_path: str,
    compiled_rules: dict[str, re.Pattern[str]],
) -> None:
    """Write seeded sample rows with auto_tags and an empty manual_label column."""
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    fieldnames = ["Review_ID", "Rating", "Year_Month", "Branch", "auto_tags", "manual_label", "Review_Text"]
    with open(out_path, "w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            tags = classify_review(row.get("Review_Text", ""), compiled_rules)
            writer.writerow(
                {
                    "Review_ID": row.get("Review_ID", ""),
                    "Rating": row.get("Rating", ""),
                    "Year_Month": row.get("Year_Month", ""),
                    "Branch": row.get("Branch", ""),
                    "auto_tags": "|".join(tags),
                    "manual_label": "",
                    "Review_Text": " ".join((row.get("Review_Text", "")).split()),
                }
            )


def print_summary_block(
    title: str,
    rows: list[dict[str, str]],
    compiled_rules: dict[str, re.Pattern[str]],
) -> None:
    """Print x/N (%) counts per pain category for a given review subset."""
    total = len(rows)
    print(f"\n=== {title} (N = {total}) ===")
    if total == 0:
        print("Khong co dong nao trong tap nay.")
        return

    cat_counts, any_pain = count_pain_categories(rows, compiled_rules)
    print(f"Co it nhat 1 pain tu khoa: {any_pain}/{total} ({any_pain / total * 100:.1f}%)")
    print("| Nhom pain | Mo ta | x / N | % |")
    print("|---|---|---|---|")
    for name, desc, _ in PAIN_RULES:
        hits = cat_counts[name]
        print(f"| `{name}` | {desc} | {hits}/{total} | {hits / total * 100:.1f}% |")


def print_sample_quotes(
    sample_rows: list[dict[str, str]],
    compiled_rules: dict[str, re.Pattern[str]],
    limit: int = 8,
) -> None:
    """Print up to `limit` short <=2-sentence example quotes, prioritizing low ratings."""
    print("\n=== Vi du trich dan (<=2 cau/review, uu tien Rating 1-3, bo ten) ===")
    ordered = sorted(
        sample_rows,
        key=lambda r: parse_rating(r.get("Rating", "")) or 99,
    )
    shown = 0
    for row in ordered:
        tags = classify_review(row.get("Review_Text", ""), compiled_rules)
        if not tags:
            continue
        excerpt = pain_excerpt(row.get("Review_Text", ""), compiled_rules)
        if not excerpt:
            continue
        shown += 1
        print(
            f"{shown}. \"{excerpt}\" "
            f"— Review_ID {row.get('Review_ID', '')}, Rating {row.get('Rating', '')}, "
            f"{row.get('Branch', '')} ({row.get('Year_Month', '')}) [tags: {', '.join(tags)}]"
        )
        if shown >= limit:
            break


def main() -> int:
    parser = argparse.ArgumentParser(description="Dem pain theo tu khoa va rut mau co seed tu DisneylandReviews.csv")
    parser.add_argument("--input", default=DEFAULT_INPUT, help="Duong dan toi DisneylandReviews.csv")
    parser.add_argument("--out", default=DEFAULT_OUT, help="File CSV mau xuat ra de kiem tay")
    parser.add_argument("--sample-size", type=int, default=200, help="So dong mau rut ra (mac dinh: 200)")
    parser.add_argument("--seed", type=int, default=42, help="Seed ngau nhien co dinh (mac dinh: 42)")
    parser.add_argument(
        "--max-rating",
        type=int,
        default=None,
        help="Loc toi da so sao cho tap mau (vd 3 de chi lay 1-3 sao). Mac dinh lay moi muc sao.",
    )
    args = parser.parse_args()

    compiled_rules = compile_rules()
    rows = load_reviews(args.input)

    ratings = Counter(r.get("Rating", "") for r in rows)
    branches = Counter(r.get("Branch", "") for r in rows)
    year_months = sorted(r.get("Year_Month", "") for r in rows if r.get("Year_Month") and r.get("Year_Month") != "missing")

    print(f"File: {args.input}")
    print(f"Tong so dong: {len(rows)}")
    if year_months:
        print(f"Khoang Year_Month: {year_months[0]} -> {year_months[-1]}")
    print("Phan bo Rating:", dict(sorted(ratings.items())))
    print("Phan bo Branch:", dict(branches))

    print_summary_block("Toan bo dataset (moi muc sao)", rows, compiled_rules)

    low_rating_rows = [
        r for r in rows if (rating := parse_rating(r.get("Rating", ""))) is not None and rating <= 3
    ]
    print_summary_block("Tap review 1-3 sao (nghieng ve phan nan)", low_rating_rows, compiled_rules)

    sample = draw_sample(rows, sample_size=args.sample_size, seed=args.seed, max_rating=args.max_rating)
    scope_desc = f"Rating <= {args.max_rating}" if args.max_rating is not None else "moi muc sao"
    print_summary_block(f"Tap mau seed={args.seed} ({scope_desc})", sample, compiled_rules)

    write_sample_csv(sample, args.out, compiled_rules)
    print(f"\nDa xuat {len(sample)} dong mau ra: {args.out}")
    print("Ghi chu: hay tu doc & dien cot `manual_label` cho >=30-50 dong de doi chieu voi `auto_tags`.")
    print_sample_quotes(sample, compiled_rules, limit=8)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
