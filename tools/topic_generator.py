#!/usr/bin/env python3
"""
选题生成器 - 大健康行业口播IP
根据用户输入的关键词，生成10个爆款选题
"""

import random

# 大健康行业选题模板
TOPIC_TEMPLATES = [
    "{关键词}的3个误区，第{数字}个你肯定做过",
    "为什么{人群}一定要{动作}{关键词}？",
    "{数字}个{关键词}冷知识，第{数字}个太意外了",
    "{人群}最该关注的{关键词}问题，第{数字}个最要命",
    "关于{关键词}，90%的人都搞错了",
    "{动作}这个{关键词}，{人群}越早知道越好",
    "{关键词}到底有没有用？看完这篇你就懂了",
    "{人群}必看！{关键词}的{数字}个致命错误",
    "为什么{人群}的{关键词}总是做不好？",
    "{关键词}常见的{数字}个问题，一次性解答",
]

# 关键词池
KEYWORDS = [
    "减肥", "瘦身", "健身", "增肌", "塑形",
    "睡眠", "失眠", "熬夜", "深度睡眠",
    "饮食", "营养", "食品安全", "健康饮食",
    "免疫力", "抵抗力", "感冒", "发烧",
    "血压", "血糖", "血脂", "三高",
    "养生", "补肾", "养胃", "护肝",
    "皮肤", "美容", "抗衰老", "护肤",
    "心理健康", "焦虑", "抑郁", "压力",
    "运动", "跑步", "瑜伽", "拉伸",
    "体检", "健康", "亚健康",
]

# 动作词
ACTIONS = ["赶紧", "马上", "立刻", "一定", "必须", "赶紧别", "千万别"]

# 人群词
AUDIENCES = [
    "年轻人", "中年人", "老年人", "上班族", "学生党",
    "妈妈", "爸爸", "宝爸", "宝妈", "新手妈妈",
    "健身小白", "减肥人群", "熬夜党", "久坐族",
    "创业者", "程序员", "设计师", "销售",
]

def generate_topics(keyword=None, count=10):
    """生成选题"""
    if not keyword:
        keyword = random.choice(KEYWORDS)

    topics = []
    seen = set()
    attempts = 0
    max_attempts = max(count * 20, 20)

    while len(topics) < count and attempts < max_attempts:
        template = random.choice(TOPIC_TEMPLATES)
        topic = template.replace("{关键词}", keyword)
        topic = topic.replace("{数字}", str(random.randint(1, 5)))
        topic = topic.replace("{人群}", random.choice(AUDIENCES))
        topic = topic.replace("{动作}", random.choice(ACTIONS))

        if topic not in seen:
            seen.add(topic)
            topics.append(topic)

        attempts += 1

    return topics

def main():
    print("=" * 50)
    print("🎯 大健康行业选题生成器")
    print("=" * 50)
    print()
    
    # 让用户输入关键词
    keyword = input("请输入你的领域关键词（直接回车随机）：").strip()
    
    if not keyword:
        print("\n🔄 随机生成中...\n")
    
    topics = generate_topics(keyword)
    
    print("📝 生成的选题：")
    print("-" * 50)
    for i, topic in enumerate(topics, 1):
        print(f"{i}. {topic}")
    print("-" * 50)
    print()
    print("💡 提示：选择你最感兴趣或最有话说的选题")

if __name__ == "__main__":
    main()
