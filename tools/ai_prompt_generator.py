#!/usr/bin/env python3
"""
AI提示词生成器 - 针对大健康行业口播脚本
生成适用于 ChatGPT/Claude 等 AI 的专业提示词
"""

def generate_prompt(topic, role="口播脚本", style="专业但通俗", duration=60):
    """生成 AI 提示词"""
    
    prompt_templates = {
        "口播脚本": f"""你是一位{role}专家。请帮我写一段{duration}秒的口播脚本。

要求：
- 语言专业但通俗易懂，像朋友聊天
- 围绕主题：{topic}
- 开头3秒抓住注意力
- 中间有干货价值
- 结尾有互动引导
- 字数：约{duration*3}字

风格：{style}

请直接输出脚本，不要多余解释。""",
        
        "选题扩展": f"""我有一个选题方向：{topic}

请帮我：
1. 列出5个具体的爆款标题（带数字、更吸引人）
2. 列出3个不同的切入角度
3. 列出2个可能的争议点（引发评论）

请用中文输出。""",
        
        "评论回复": f"""我是一位大健康行业的博主，有人评论说：{topic}

请帮我：
1. 生成3条高赞回复模板（引发二次互动）
2. 判断这条评论的潜在意图
3. 建议是否需要置顶

风格：亲切、专业、有温度""",
        
        "视频描述": f"""帮我为口播视频生成：
1. 抖音/小红书标题（带emoji，30字内）
2. 视频描述文案（带话题标签）
3. 适合的热门话题标签（5-10个）

视频主题：{topic}
时长：约{duration}秒""",

        "平台安全改写": f"""你是一位熟悉中国内容平台生态的大健康内容编辑。

请把下面这段原始文案，改写成更适合公开平台发布的版本：

原始文案：{topic}

请按以下要求输出：
1. 先指出 3-5 个风险点
2. 给出 3 个更稳妥的标题
3. 输出 1 版 60 秒口播稿
4. 输出 1 版评论区引导
5. 输出 1 版更轻的私信承接文案

要求：
- 保留专业价值
- 删除绝对化承诺、疗效式说法、夸张营销和过猛导流
- 更适合抖音 / 小红书 / 视频号公开发布
- 如涉及疾病、治疗、用药，补一句边界提醒""",
    }
    
    return prompt_templates

def main():
    print("=" * 60)
    print("🤖 AI提示词生成器")
    print("=" * 60)
    print()
    print("选择要生成的内容类型：")
    print("1. 口播脚本")
    print("2. 选题扩展")
    print("3. 评论回复")
    print("4. 视频描述")
    print("5. 平台安全改写")
    print()
    
    choice = input("请输入选项（1-5）：").strip()
    print()
    
    topics = {
        "1": "口播脚本",
        "2": "选题扩展", 
        "3": "评论回复",
        "4": "视频描述",
        "5": "平台安全改写",
    }
    
    role_type = topics.get(choice)
    if not role_type:
        print("❌ 无效选项")
        return
    
    print(f"📝 输入你的主题内容（直接回车使用示例）：")
    topic = input().strip()
    
    if not topic:
        if choice == "1":
            topic = "如何在一个月内健康减掉10斤"
        elif choice == "2":
            topic = "减肥"
        elif choice == "3":
            topic = "真的有用吗？我试了一点效果都没有"
        elif choice == "4":
            topic = "健康减脂餐的正确做法"
        elif choice == "5":
            topic = "7天瘦10斤，不节食不运动也能做到。想要方案的评论区扣1，我拉你进群。"
    
    prompt = generate_prompt(topic, role_type)[role_type]
    
    print()
    print("=" * 60)
    print("📋 生成的提示词（复制到 AI 使用）：")
    print("=" * 60)
    print()
    print(prompt)
    print()
    print("=" * 60)
    print("💡 使用方法：复制上方提示词，粘贴到 ChatGPT/Claude 等 AI 工具中")
    print("=" * 60)

if __name__ == "__main__":
    main()
