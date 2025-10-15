#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ダミーを含むが、ダミーには絶対当選しないルーレット
- 盤面にはダミーも表示（演出用）
- 抽選は非ダミー項目（is_dummy=False）のみから重み付きで選択
- シンプルなアニメーション付き
"""

from dataclasses import dataclass
from typing import List, Optional
import random
import time
import shutil
import math
import sys
import os, ctypes

@dataclass(frozen=True)
class Slot:
    label: str
    is_dummy: bool = False  # ダミーにするか
    weight: float = 1.0  # 当たりやすさ（ダミーの重みは無視）

# ======== 設定 ========
WHEEL: List[Slot] = [
    Slot("Hana",       True,  1.0),
    Slot("Takeshiltu", False, 1.0),
    Slot("Kotomi",     True,  1.0),
    Slot("Daiki",      True,  1.0),
    Slot("Namekuji",   False, 1.0),
    Slot("Melon",      True,  1.0),
    Slot("Kanata",     True,  1.0),
    Slot("Balu",       True,  1.0),
]

# 乱数シード（固定したいときは数値を入れる。ランダムにしたいときは None）
RANDOM_SEED: Optional[int] = None

# スピン演出の速さ（値が小さいほど速い）
SPIN_BASE_DELAY = 0.03
SPIN_DECAY = 1.06      # 徐々に減速（>1で減速）
SPIN_EXTRA_TICKS = (len(WHEEL) * 7)  # 最低何マス分回すか
# ======== 設定 ========

def _enable_ansi_on_windows():
    if os.name != "nt":
        return
    kernel32 = ctypes.windll.kernel32
    handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
    mode = ctypes.c_uint()
    if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
        ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
        kernel32.SetConsoleMode(handle, mode.value | ENABLE_VIRTUAL_TERMINAL_PROCESSING)


def pick_index_avoiding_dummies(wheel: List[Slot]) -> int:
    """ダミーを除くスロットから重み付きでインデックスを返す"""
    candidates = [(i, s.weight) for i, s in enumerate(wheel) if not s.is_dummy and s.weight > 0]
    if not candidates:
        raise ValueError("対象者がいません。WHEEL設定を見直してください。")
    indices, weights = zip(*candidates)
    # random.choicesで重み付きサンプリング
    chusen = random.choices(indices, weights=weights, k=1)[0]
    return chusen


def render_wheel_lines(wheel: List[Slot], pointer_at: int) -> tuple[str, str]:
    """
    各スロットを固定幅セルで描画し、^ をそのセルの中央に置く。
    半角英数字であればズレません（全角は端末の幅扱いによってズレる可能性あり）。
    """
    labels = [(f"  {s.label}" if s.is_dummy else s.label) for s in wheel]

    # 内側の最大幅を決定（ラベルの最長長さ）
    inner_w = max(1, max(len(x) for x in labels))
    #    セルは「左右に1スペース＋ラベル」で inner_w+2
    cell_w = inner_w + 2
    sep = "|"  # 区切り

    cells = [(" " + lbl.ljust(inner_w) + " ") for lbl in labels]

    line = sep.join(cells)

    # pointer_at のセルの先頭位置を厳密に算出
    # 先頭セルの開始位置は 0、i番目セルの開始は i*(cell_w + len(sep))
    start_pos = pointer_at * (cell_w + len(sep))

    # セル中央に ^ を置く
    caret_pos = start_pos + cell_w // 2
    pointer_line = " " * caret_pos + "^"

    return line, pointer_line


def spin(wheel: List[Slot], target_index: int) -> int:
    """スピン演出 (最終的に chusen_index に止まる)"""
    _enable_ansi_on_windows()

    # カーソル非表示
    sys.stdout.write("\x1b[?25l")
    sys.stdout.flush()

    current = random.randrange(len(wheel))
    ticks = SPIN_EXTRA_TICKS + random.randrange(len(wheel), len(wheel) * 2)
    delay = SPIN_BASE_DELAY

    line, ptr = render_wheel_lines(wheel, current)
    sys.stdout.write(line + "\n" + ptr + "\n")
    sys.stdout.flush()

    def redraw(idx: int, d: float):
        sys.stdout.write("\x1b[2A")  # 2行上へ
        sys.stdout.write("\x1b[2K"); sys.stdout.write(render_wheel_lines(wheel, idx)[0] + "\n")
        sys.stdout.write("\x1b[2K"); sys.stdout.write(render_wheel_lines(wheel, idx)[1] + "\n")
        sys.stdout.flush()
        time.sleep(d)

    for _ in range(ticks):
        redraw(current, delay)
        delay *= SPIN_DECAY
        current = (current + 1) % len(wheel)

    while current != target_index:
        redraw(current, delay)
        delay *= SPIN_DECAY
        current = (current + 1) % len(wheel)

    redraw(current, delay)

    # カーソル表示を戻す
    sys.stdout.write("\x1b[?25h")
    sys.stdout.flush()
    return current


def countdown(seconds: int = 3):
    """ルーレット開始までのカウントダウン"""
    _enable_ansi_on_windows()
    # カーソル非表示
    sys.stdout.write("\x1b[?25l")
    sys.stdout.flush()
    try:
        for t in range(seconds, 0, -1):
            sys.stdout.write(f"\r{t}...")
            sys.stdout.flush()
            time.sleep(1)
        # 行をクリア
        sys.stdout.write("\r\x1b[2K\r")
        sys.stdout.flush()
    finally:
        # カーソル再表示
        sys.stdout.write("\x1b[?25h")
        sys.stdout.flush()

def main():
    if RANDOM_SEED is not None:
        random.seed(RANDOM_SEED)

    # カウントダウン
    countdown(5)

    print("=== ルーレット開始！===\n")

    # 当選対象者を決定
    chusen_index = pick_index_avoiding_dummies(WHEEL)

    # スピン演出
    final_index = spin(WHEEL, chusen_index)

    chusen_slot = WHEEL[final_index]
    assert not chusen_slot.is_dummy, ""

    # 結果表示
    print(f"\n当選おめでとうございます!!：{chusen_slot.label}")

if __name__ == "__main__":
    main()
