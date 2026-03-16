#!/usr/bin/env python3
"""
脚本优化器 - 大健康行业口播IP
将长脚本精简为口语化口播稿
"""

import re

def optimize_script(raw_script, target_duration=60):
    """
    优化脚本：
    1. 去除书面语，转化为口语
    2. 计算预计朗读时长
    3. 提供优化建议
    """
    # 去除多余空白
    script = re.sub(r'\s+', ' ', raw_script.strip())
    
    # 估算时长（平均每秒3-4字）
    char_count = len(script)
    estimated_seconds = char_count / 3.5
    
    # 口语化替换
   口语化替换 = {
        "因此": "所以",
        "但是": "不过",
        "因为": "为啥呢，因为",
        "所以": "所以啊",
        "非常": "特别",
        "十分": "特别",
        "需要": "得",
        "可以": "能",
        "应该": "得",
        "认为": "觉得",
        "通过": "用",
        "进行": "做",
        "关于": "对于",
        "对于": "说到",
        "也就是说": "就是",
        "实际上": "其实",
        "一般来说": "通常来说",
        "大多数": "很多人",
        "一部分": "有些人",
    }
    
    optimized = script
    for old, new in口语化替换.items():
        optimized = optimized.replace(old, new)
    
    # 计算优化后的时长
    optimized_char_count = len(optimized)
    optimized_seconds = optimized_char_count / 3.5
    
    # 断句建议
    sentences = re.split(r'[。！？]', optimized)
    sentences = [s.strip() for s in sentences if s.strip()]
    
    return {
        "original": script,
        "optimized": optimized,
        "original_chars": char_count,
        "optimized_chars": optimized_char_count,
        "original_seconds": estimated_seconds,
        "optimized_seconds": optimized_seconds,
        "sentence_count": len(sentences),
        "sentences": sentences,
    }

def print_result(result, target_duration=60):
    """打印优化结果"""
    print("=" * 60)
    print("📝 脚本优化结果")
    print("=" * 60)
    print()
    
    print(f"📊 字数统计：")
    print(f"   优化前：{result['original_chars']} 字")
    print(f"   优化后：{result['optimized_chars']} 字")
    print()
    
    print(f"⏱️ 预计时长：")
    print(f"   优化前：约 {result['original_seconds']:.0f} 秒")
    print(f"   优化后：约 {result['optimized_seconds']:.0f} 秒")
    print(f"   目标时长：{target_duration} 秒")
    print()
    
    if result['optimized_seconds'] > target_duration:
        print(f"⚠️ 超出目标时长约 {result['optimized_seconds'] - target_duration:.0f} 秒，建议精简")
    else:
        print(f"✅ 时长合适，剩余 {target_duration - result['optimized_seconds']:.0f} 秒")
    print()
    
    print("📖 优化后的脚本：")
    print("-" * 60)
    print(result['optimized'])
    print("-" * 60)
    print()
    
    print(f"📌 断句建议（共 {result['sentence_count']} 句）：")
    for i, sent in enumerate(result['sentences'], 1):
        # 每行约20字
        if len(sent) > 20:
            # 在中间位置断句
            mid = len(sent) // 2
            for j in range(mid, len(sent)):
                if sent[j] in '，、':
                    sent = sent[:j+1] + '\n       ' + sent[j+1:]
                    break
        print(f"   {i}. {sent}")
    print()

def main():
    print("=" * 60)
    print("🎬 脚本优化器")
    print("=" * 60)
    print()
    print("请输入你的脚本内容（直接回车使用示例）：")
    print()
    
    raw = input().strip()
    
    if not raw:
        # 使用示例
        raw = """很多人在减肥期间都有一个误区，认为只要不吃饭就能瘦下来。但实际上，过度节食会导致基础代谢下降，一旦恢复正常饮食，体重会快速反弹。正确的减肥方式应该是合理控制饮食搭配适量运动，比如每餐吃到七分饱，每天坚持三十分钟的有氧运动，这样才能健康持续地瘦下来。"""
        print("📝 使用示例脚本...")
        print()
    
    result = optimize_script(raw)
    print_result(result)
    
    # 再次优化选项
    print("是否需要进一步精简？(y/n)")
    if input().strip().lower() == 'y':
        # 进一步精简
        sentences = result['sentences']
        # 取最重要的前几句
        if len(sentences) > 3:
            simplified = '。'.join(sentences[:3]) + '。'
            result2 = optimize_script(simplified)
            print("\n📦 精简版脚本：")
            print("-" * 60)
            print(result2['optimized'])
            print("-" * 60)
            print(f"\n⏱️ 预计时长：约 {result2['optimized_seconds']:.0f} 秒")

if __name__ == "__main__":
    main()
