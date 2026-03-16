#!/usr/bin/env python3
"""
内容风险检查器
用于扫描健康行业内容里的高风险表达，并给出更稳妥的替代建议。
"""

import argparse
import re
import sys
from typing import Dict, List, Tuple


RISK_RULES = [
    {
        "category": "快速结果承诺",
        "severity": "high",
        "patterns": ["不节食不运动", "躺着瘦", "轻松月入", "立刻见效"],
        "regex_patterns": [r"\d+天瘦\d+斤", r"\d+天见效", r"\d+天逆袭", r"\d+天变好"],
        "suggestion": "改成“先从哪些动作开始”“更容易坚持的路径”，避免速效承诺。",
    },
    {
        "category": "绝对化承诺",
        "severity": "high",
        "patterns": ["包瘦", "一定有效", "百分百", "人人适用", "绝对安全", "零副作用"],
        "suggestion": "改成“更适合谁”“通常适合什么场景”“建议结合个人情况判断”。",
    },
    {
        "category": "医疗疗效表达",
        "severity": "high",
        "patterns": ["根治", "治愈", "逆转", "彻底解决", "药到病除", "替代医生", "不用看医生"],
        "suggestion": "改成“改善习惯”“辅助管理”“如有明显不适建议就医评估”。",
    },
    {
        "category": "夸张营销",
        "severity": "medium",
        "patterns": ["震惊", "全网都在", "再不知道就晚了", "医院不会告诉你", "最后一天", "错过就亏"],
        "suggestion": "改成具体场景问题、可执行动作和适用边界，减少恐吓式词汇。",
    },
    {
        "category": "过猛导流",
        "severity": "medium",
        "patterns": ["加微信", "私信我领", "拉你进群", "评论区扣1", "扫码领取", "加我领取"],
        "suggestion": "优先用轻承接，如“评论区留关键词”“先领清单/评估表”，减少强导流。",
    },
]


PLATFORM_HINTS = {
    "common": "先保证表达专业、边界清晰，再考虑转化动作。",
    "douyin": "抖音更适合短句、场景化、直接问题切入；避免夸张疗效和强导流。",
    "xiaohongshu": "小红书更适合经验分享和生活化语气；避免硬广口吻和过强销售结构。",
    "wechat": "视频号更适合稳重、可信、关系感更强的表达；避免标题党和过于刺激的说法。",
}


SEVERITY_SCORES = {"high": 3, "medium": 2, "low": 1}


def read_content(args: argparse.Namespace) -> str:
    if args.text:
        return args.text.strip()
    if args.file:
        with open(args.file, "r", encoding="utf-8") as handle:
            return handle.read().strip()
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    return input("请输入要检查的内容：").strip()


def collect_matches(text: str) -> List[Dict[str, object]]:
    findings = []
    for rule in RISK_RULES:
        matched = []
        for pattern in rule["patterns"]:
            if pattern in text:
                matched.append(pattern)
        for regex_pattern in rule.get("regex_patterns", []):
            regex_matches = re.findall(regex_pattern, text)
            for matched_text in regex_matches:
                if matched_text not in matched:
                    matched.append(matched_text)
        if matched:
            findings.append(
                {
                    "category": rule["category"],
                    "severity": rule["severity"],
                    "matched": matched,
                    "suggestion": rule["suggestion"],
                }
            )
    return findings


def detect_level(findings: List[Dict[str, object]]) -> Tuple[str, int]:
    score = sum(SEVERITY_SCORES[item["severity"]] * len(item["matched"]) for item in findings)
    if score >= 8:
        return "high", score
    if score >= 3:
        return "medium", score
    return "low", score


def extract_sentences(text: str, keywords: List[str]) -> List[str]:
    pieces = re.split(r"(?<=[。！？!?])", text)
    result = []
    for piece in pieces:
        stripped = piece.strip()
        if stripped and any(keyword in stripped for keyword in keywords):
            result.append(stripped)
    return result


def print_report(text: str, platform: str, findings: List[Dict[str, object]]) -> None:
    level, score = detect_level(findings)
    all_keywords = []
    for item in findings:
        all_keywords.extend(item["matched"])

    print("=" * 64)
    print("🛡️ 内容风险检查报告")
    print("=" * 64)
    print("平台：{}".format(platform))
    print("内容长度：{} 字".format(len(text)))
    print("风险等级：{}（score={}）".format(level.upper(), score))
    print("平台提示：{}".format(PLATFORM_HINTS.get(platform, PLATFORM_HINTS["common"])))
    print()

    if not findings:
        print("未发现预设高风险词。")
        print("仍建议人工再检查：是否有夸大承诺、医疗结论化表达、过强导流。")
        return

    print("命中项：")
    for index, item in enumerate(findings, start=1):
        print("- {}. [{}] {}".format(index, item["severity"], item["category"]))
        print("  关键词：{}".format("、".join(item["matched"])))
        print("  建议：{}".format(item["suggestion"]))

    print()
    print("命中句子：")
    for sentence in extract_sentences(text, all_keywords):
        print("- {}".format(sentence))

    print()
    print("推荐动作：")
    if level == "high":
        print("- 先重写标题和开头，再重写结尾导流。")
        print("- 用 `prompts/平台安全改写.md` 做一版平台适配。")
    else:
        print("- 优先替换命中的风险词，再补适用边界。")
    print("- 发布前再对照 `docs/健康内容合规清单.md` 和 `docs/中国平台限流避坑指南.md`。")


def main() -> None:
    parser = argparse.ArgumentParser(description="检查健康行业内容中的高风险表达。")
    parser.add_argument("--platform", choices=["common", "douyin", "xiaohongshu", "wechat"], default="common")
    parser.add_argument("--text", help="直接传入要检查的内容")
    parser.add_argument("--file", help="从文件读取要检查的内容")
    args = parser.parse_args()

    text = read_content(args)
    if not text:
        print("❌ 没有检测到内容。")
        return

    findings = collect_matches(text)
    print_report(text, args.platform, findings)


if __name__ == "__main__":
    main()
