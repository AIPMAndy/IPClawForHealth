#!/usr/bin/env python3
"""
脚本优化器 - 大健康行业口播 IP
将较长脚本整理成更适合口播的版本，并估算时长。
"""

import re
import sys
from typing import Any, Dict, List

CHARS_PER_SECOND = 3.5

SPOKEN_REPLACEMENTS = {
    "因此": "所以",
    "但是": "不过",
    "因为": "为啥呢，因为",
    "所以": "所以啊",
    "非常": "特别",
    "十分": "特别",
    "需要": "得",
    "可以": "能",
    "认为": "觉得",
    "通过": "用",
    "进行": "做",
    "关于": "说到",
    "对于": "说到",
    "也就是说": "也就是",
    "实际上": "其实",
    "一般来说": "通常来说",
    "大多数": "很多",
    "一部分": "有些",
}


def normalize_script(raw_script: str) -> str:
    """压缩多余空白，保留原有句意。"""
    return re.sub(r"\s+", " ", raw_script.strip())


def make_spoken(script: str) -> str:
    """把常见书面表达替换成更口语的说法。"""
    optimized = script
    for old, new in SPOKEN_REPLACEMENTS.items():
        optimized = optimized.replace(old, new)
    return optimized


def split_sentences(script: str) -> List[str]:
    """按中文句号、问号、感叹号切分句子。"""
    parts = re.split(r"(?<=[。！？!?])", script)
    return [part.strip() for part in parts if part.strip()]


def estimate_seconds(script: str) -> float:
    return len(script) / CHARS_PER_SECOND if script else 0.0


def trim_to_duration(sentences: List[str], target_duration: int) -> str:
    """按目标时长挑选前几句，给出一个可直接试读的精简版。"""
    max_chars = max(int(target_duration * CHARS_PER_SECOND), 1)
    trimmed: List[str] = []
    current_chars = 0

    for sentence in sentences:
        if current_chars + len(sentence) <= max_chars or not trimmed:
            trimmed.append(sentence)
            current_chars += len(sentence)
            continue
        break

    return "".join(trimmed).strip()


def optimize_script(raw_script: str, target_duration: int = 60) -> Dict[str, Any]:
    """
    优化脚本：
    1. 去除多余空白
    2. 转换为更口语的说法
    3. 估算时长并给出精简版
    """
    original = normalize_script(raw_script)
    optimized = make_spoken(original)
    sentences = split_sentences(optimized)
    trimmed = trim_to_duration(sentences, target_duration)

    return {
        "original": original,
        "optimized": optimized,
        "trimmed": trimmed,
        "original_chars": len(original),
        "optimized_chars": len(optimized),
        "trimmed_chars": len(trimmed),
        "original_seconds": estimate_seconds(original),
        "optimized_seconds": estimate_seconds(optimized),
        "trimmed_seconds": estimate_seconds(trimmed),
        "sentence_count": len(sentences),
        "sentences": sentences,
    }


def format_sentence(sentence: str) -> str:
    """长句在逗号处断开，方便试读。"""
    if len(sentence) <= 20:
        return sentence

    midpoint = len(sentence) // 2
    for index in range(midpoint, len(sentence)):
        if sentence[index] in "，、；":
            return sentence[: index + 1] + "\n       " + sentence[index + 1 :]
    return sentence


def print_result(result: Dict[str, Any], target_duration: int = 60) -> None:
    """打印优化结果。"""
    print("=" * 60)
    print("📝 脚本优化结果")
    print("=" * 60)
    print()

    print("📊 字数统计：")
    print(f"   优化前：{result['original_chars']} 字")
    print(f"   优化后：{result['optimized_chars']} 字")
    print(f"   精简版：{result['trimmed_chars']} 字")
    print()

    print("⏱️ 预计时长：")
    print(f"   优化前：约 {result['original_seconds']:.0f} 秒")
    print(f"   优化后：约 {result['optimized_seconds']:.0f} 秒")
    print(f"   精简版：约 {result['trimmed_seconds']:.0f} 秒")
    print(f"   目标时长：{target_duration} 秒")
    print()

    if result["optimized_seconds"] > target_duration:
        overflow = result["optimized_seconds"] - target_duration
        print(f"⚠️ 当前版本超出目标时长约 {overflow:.0f} 秒，建议先试读精简版。")
    else:
        remain = target_duration - result["optimized_seconds"]
        print(f"✅ 当前版本时长合适，距离目标上限还有约 {remain:.0f} 秒。")
    print()

    print("📖 优化后的脚本：")
    print("-" * 60)
    print(result["optimized"])
    print("-" * 60)
    print()

    print(f"📌 断句建议（共 {result['sentence_count']} 句）：")
    for index, sentence in enumerate(result["sentences"], start=1):
        print(f"   {index}. {format_sentence(sentence)}")
    print()

    if result["trimmed"]:
        print("📦 60 秒内优先试读版：")
        print("-" * 60)
        print(result["trimmed"])
        print("-" * 60)
        print()


def read_script() -> str:
    """支持交互输入和管道输入。"""
    if sys.stdin.isatty():
        return input().strip()
    return sys.stdin.read().strip()


def main() -> None:
    print("=" * 60)
    print("🎬 脚本优化器")
    print("=" * 60)
    print()
    print("请输入你的脚本内容（直接回车使用示例）：")
    print()

    raw = read_script()

    if not raw:
        raw = (
            "很多人在减肥期间都有一个误区，认为只要不吃饭就能瘦下来。"
            "但实际上，过度节食会导致基础代谢下降，一旦恢复正常饮食，体重会快速反弹。"
            "正确的减肥方式应该是合理控制饮食搭配适量运动，比如每餐吃到七分饱，"
            "每天坚持三十分钟的有氧运动，这样才能健康持续地瘦下来。"
        )
        print("📝 使用示例脚本...")
        print()

    result = optimize_script(raw)
    print_result(result)

    # 管道模式只输出一次结果，不再进入交互。
    if not sys.stdin.isatty():
        return

    print("是否需要进一步精简？(y/n)")
    if input().strip().lower() == "y":
        simplified = result["trimmed"] or result["optimized"]
        print("\n📦 精简版脚本：")
        print("-" * 60)
        print(simplified)
        print("-" * 60)
        print(f"\n⏱️ 预计时长：约 {estimate_seconds(simplified):.0f} 秒")


if __name__ == "__main__":
    main()
