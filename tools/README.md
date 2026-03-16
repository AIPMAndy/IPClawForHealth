# 🛠️ 工具说明

本目录包含大健康行业口播IP的实用工具。

## 工具列表

### 1. topic_generator.py - 选题生成器

根据关键词生成10个爆款选题。

```bash
python3 tools/topic_generator.py
```

### 2. script_optimizer.py - 脚本优化器

将书面语转化为口语化口播稿，计算时长。

```bash
python3 tools/script_optimizer.py

# 或直接从标准输入读取一段脚本
echo "很多人减脂只看体重，其实这很容易掉进误区。" | python3 tools/script_optimizer.py
```

### 3. ai_prompt_generator.py - AI提示词生成器

生成适用于 ChatGPT/Claude 的专业提示词。

```bash
python3 tools/ai_prompt_generator.py
```

## 环境要求

- Python 3.7+
- 无需额外依赖

## 使用建议

1. **选题阶段**：用 `topic_generator.py` 生成选题方向
2. **脚本阶段**：用 `ai_prompt_generator.py` 生成初稿
3. **优化阶段**：用 `script_optimizer.py` 优化为口语化脚本
