"""Pretty terminal dashboard wrapping `python run.py check` without modifying framework files.

Usage:
    py eval/view_check.py
    python eval/view_check.py
"""
from __future__ import annotations

import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
METRIC_YAML = os.path.join(ROOT, "eval", "metric_spec.yaml")

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"


def enable_ansi_windows() -> None:
    """Enable ANSI color sequences on Windows consoles."""
    if os.name == "nt":
        os.system("")


def run_official_check() -> str:
    """Run `run.py check` as a subprocess and return UTF-8 stdout."""
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = "utf-8"
    proc = subprocess.run(
        [sys.executable, os.path.join(ROOT, "run.py"), "check"],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if proc.returncode != 0 and not proc.stdout.strip():
        raise RuntimeError(proc.stderr.strip() or f"run.py check exited with {proc.returncode}")
    return proc.stdout


def parse_check_output(text: str) -> dict:
    """Extract structured metrics and warnings from `run.py check` output."""
    info = {
        "columns_ok": "Đủ 6 cột" in text,
        "total": 0,
        "thuong": 0,
        "kho": 0,
        "tu_choi": 0,
        "sources": {},
        "real_count": 0,
        "real_total": 0,
        "metrics_count": 0,
        "teams_count": 0,
        "warnings": [],
    }

    if m := re.search(r"Số câu thử:\s*(\d+)\s*·\s*thuong\s*(\d+)\s*·\s*kho\s*(\d+)\s*·\s*tu_choi\s*(\d+)", text):
        info["total"], info["thuong"], info["kho"], info["tu_choi"] = map(int, m.groups())

    if m := re.search(
        r"nguoi_dung\s*(\d+)\s*·\s*data_that\s*(\d+)\s*·\s*tu_viet\s*(\d+)\s*·\s*sinh_seed\s*(\d+)"
        r"\s*·\s*từ người dùng / data thật:\s*(\d+)/(\d+)",
        text,
    ):
        nd, dt, tv, ss, rc, rt = map(int, m.groups())
        info["sources"] = {"nguoi_dung": nd, "data_that": dt, "tu_viet": tv, "sinh_seed": ss}
        info["real_count"] = rc
        info["real_total"] = rt

    if m := re.search(r"eval/metric_spec\.yaml:\s*(\d+)\s*metric", text):
        info["metrics_count"] = int(m.group(1))

    if m := re.search(r"Kiểm TEAMS\.md\s+(\d+)\s*thành viên", text):
        info["teams_count"] = int(m.group(1))

    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("⚠️"):
            info["warnings"].append(stripped.lstrip("⚠️").strip())

    return info


def read_metric_rows() -> list[dict[str, str]]:
    """Read metric names, graders, and thresholds directly from eval/metric_spec.yaml."""
    if not os.path.exists(METRIC_YAML):
        return []
    rows: list[dict[str, str]] = []
    cur: dict[str, str] = {}
    with open(METRIC_YAML, encoding="utf-8-sig") as handle:
        for raw in handle:
            line = raw.strip()
            if not line or line.startswith("#") or line == "metrics:":
                continue
            if line.startswith("- name:"):
                if cur:
                    rows.append(cur)
                cur = {"name": line.split(":", 1)[1].strip().strip("\"'")}
            elif ":" in line and cur is not None:
                key, val = line.split(":", 1)
                cur[key.strip()] = val.strip().strip("\"'")
    if cur:
        rows.append(cur)
    return rows


def badge(ok: bool, ok_text: str = "ĐẠT", fail_text: str = "CHƯA ĐẠT", width: int = 8) -> str:
    """Return fixed-width colored status tag."""
    label = ok_text if ok else fail_text
    color = GREEN if ok else YELLOW
    return f"{color}[{label:^{width}}]{RESET}"


def divider(char: str = "─", width: int = 74) -> str:
    return f"{DIM}{char * width}{RESET}"


def render_dashboard(info: dict, metric_rows: list[dict[str, str]]) -> None:
    """Print organized, colorized check summary to terminal."""
    total = info["total"]
    real_pct = (info["real_count"] / info["real_total"] * 100) if info["real_total"] else 0.0

    cp2_ok = (
        info["columns_ok"]
        and total >= 10
        and info["kho"] >= 5
        and info["tu_choi"] >= 2
        and info["real_total"] > 0
        and info["real_count"] * 3 >= info["real_total"]
        and info["metrics_count"] >= 3
    )
    cp3_ok = cp2_ok and (20 <= total <= 30)

    print()
    print(divider("═"))
    print(f"{BOLD}{CYAN}  4MEMS · TRACK C1 — BẢNG KIỂM TRA EVAL & TEAMS{RESET}")
    print(divider("═"))

    # 1. Tong quan theo moc
    print(f"\n{BOLD}1. TRẠNG THÁI MỤC TIÊU{RESET}")
    print(f"  {badge(cp2_ok)}  CP2 (19:30 hôm nay) : ≥10 câu, ≥5 kho, ≥2 tu_choi, ≥1/3 nguồn thật, ≥3 metric")
    print(f"  {badge(cp3_ok, 'ĐẠT', 'CHỜ CP3')}  CP3 (10:00 ngày mai): mở rộng lên 20–30 câu thử")

    # 2. Benchmark summary
    print(f"\n{BOLD}2. BỘ CÂU THỬ (eval/benchmark.csv){RESET}")
    print(f"  Cột chuẩn (6 cột) : {badge(info['columns_ok'], 'ĐỦ 6 CỘT', 'THIẾU CỘT', width=9)}")
    print(
        f"  Phân loại (N={total:<2})  : "
        f"thuong = {BOLD}{info['thuong']}{RESET}  │  "
        f"kho = {BOLD}{info['kho']}{RESET} (≥5)  │  "
        f"tu_choi = {BOLD}{info['tu_choi']}{RESET} (≥2)"
    )
    src = info["sources"]
    print(
        f"  Nguồn câu thử     : "
        f"nguoi_dung={src.get('nguoi_dung', 0)} · "
        f"data_that={src.get('data_that', 0)} · "
        f"tu_viet={src.get('tu_viet', 0)} · "
        f"sinh_seed={src.get('sinh_seed', 0)}"
    )
    print(
        f"  Tỷ lệ nguồn thật  : {BOLD}{info['real_count']}/{info['real_total']} ({real_pct:.1f}%){RESET} "
        f"{badge(info['real_total'] > 0 and info['real_count'] * 3 >= info['real_total'], '>= 33.3%', '< 33.3%', width=8)}"
    )

    # 3. Metric spec table
    print(f"\n{BOLD}3. METRIC ĐO LƯỜNG (eval/metric_spec.yaml — {info['metrics_count']} metric hợp lệ){RESET}")
    if metric_rows:
        print(f"  {'Metric':<24} │ {'Grader':<8} │ {'Ngưỡng':<24}")
        print(f"  {'─'*24}─┼─{'─'*8}─┼─{'─'*24}")
        for m in metric_rows:
            print(f"  {m.get('name', ''):<24} │ {m.get('grader', ''):<8} │ {m.get('threshold', ''):<24}")
    else:
        print(f"  {YELLOW}Chưa đọc được metric nào.{RESET}")

    # 4. Categorized warnings
    teams_warns = [w for w in info["warnings"] if "TEAMS.md" in w]
    cp3_warns = [w for w in info["warnings"] if "CP3" in w]
    other_warns = [w for w in info["warnings"] if "TEAMS.md" not in w and "CP3" not in w]

    print(f"\n{BOLD}4. VIỆC CẦN XỬ LÝ{RESET}")
    if not info["warnings"]:
        print(f"  {GREEN}Không còn cảnh báo nào.{RESET}")
    else:
        if other_warns:
            print(f"  {RED}[Cần sửa ngay cho CP2]{RESET}")
            for w in other_warns:
                print(f"    • {w}")
        if cp3_warns:
            print(f"  {CYAN}[Nhắc cho mốc CP3 — sáng mai]{RESET}")
            for w in cp3_warns:
                print(f"    • {w}")
        if teams_warns:
            print(f"  {YELLOW}[TEAMS.md — chờ thành viên khác điền ({info['teams_count']} dòng)]{RESET}")
            for w in teams_warns:
                print(f"    • {w}")

    print()
    print(divider("─"))
    print(f"{DIM}  Nguồn kiểm tra chính thức: python run.py check (không sửa file khung){RESET}")
    print(divider("═"))
    print()


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    enable_ansi_windows()
    raw = run_official_check()
    info = parse_check_output(raw)
    metric_rows = read_metric_rows()
    render_dashboard(info, metric_rows)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
