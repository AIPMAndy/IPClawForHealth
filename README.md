<div align="center">

# 🏥 IPClawForHealth

**给大健康行业创始人的开源口播 IP 内容工具箱。**

[![License](https://img.shields.io/badge/license-MIT-2f8f83.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/AIPMAndy/IPClawForHealth?style=social)](https://github.com/AIPMAndy/IPClawForHealth/stargazers)
[![Contributors](https://img.shields.io/github/contributors/AIPMAndy/IPClawForHealth)](https://github.com/AIPMAndy/IPClawForHealth/graphs/contributors)

[English](README_EN.md) | **简体中文**

<img src="assets/cover.svg" alt="IPClawForHealth cover" width="960">

</div>

> `IPClawForHealth` 不是一个已经封装好的 SaaS。
>
> 它是一套可以直接复用的开源内容资产仓，核心是把大健康行业创始人做口播 IP 需要的关键材料拆成：定位 Prompt、选题库、脚本模板、成交话术、变现设计、工作流、案例库和 3 个可运行的小工具。

## 这个仓库里现在有什么

- `prompts/`：5 个核心 Prompt，覆盖定位、选题、脚本、话术、变现。
- `workflows/`：2 套执行路径，分别解决「30 分钟出片」和「30 天系统打造」。
- `examples/案例库.md`：1 个整合案例库，用于参考内容结构和转化路径。
- `tools/`：3 个 Python CLI 工具，分别负责选题生成、AI Prompt 生成、脚本优化。
- `index.html`：1 个静态落地页，可直接作为仓库展示页或项目介绍页。

## 为什么它比泛 Prompt 包更有用

| 维度 | 通用内容模板 | IPClawForHealth |
|------|:------------:|:---------------:|
| 聚焦大健康行业 | ❌ | ✅ |
| 站在创始人/专家视角设计 | ⚠️ | ✅ |
| 从内容延伸到成交动作 | ⚠️ | ✅ |
| 提供成套工作流 | ❌ | ✅ |
| 附带可运行小工具 | ❌ | ✅ |
| 可直接作为项目展示入口 | ❌ | ✅ |

## 🚀 30 秒快速开始

```bash
git clone https://github.com/AIPMAndy/IPClawForHealth.git
cd IPClawForHealth

# 1) 本地打开介绍页
python3 -m http.server 8788
# 然后访问 http://127.0.0.1:8788

# 2) 先做定位诊断
cat prompts/定位诊断.md

# 3) 生成一轮选题
python3 tools/topic_generator.py

# 4) 让 AI 生成脚本 Prompt
python3 tools/ai_prompt_generator.py

# 5) 优化成更适合口播的版本
python3 tools/script_optimizer.py
```

## 推荐使用顺序

1. `prompts/定位诊断.md`
   明确你要服务的细分人群、专业优势和差异化表达。
2. `prompts/选题库.md`
   找到适合自己阶段的内容切口，快速进入选题状态。
3. `prompts/脚本模板.md` + `tools/ai_prompt_generator.py`
   先产出初稿，再把内容改成适合口播的视频脚本。
4. `tools/script_optimizer.py`
   估算时长、口语化替换，并给出一个更适合 60 秒试读的版本。
5. `prompts/话术库.md` + `prompts/变现设计.md`
   把内容链路延伸到私域转化、成交设计和产品承接。

## 📦 仓库结构

```text
IPClawForHealth/
├── assets/
│   └── cover.svg             # README 封面图
├── examples/
│   └── 案例库.md            # 参考案例拆解
├── prompts/
│   ├── 定位诊断.md          # 创始人 IP 定位
│   ├── 选题库.md            # 行业专属选题
│   ├── 脚本模板.md          # 口播脚本模板
│   ├── 话术库.md            # 咨询与成交话术
│   └── 变现设计.md          # 产品梯度与转化设计
├── tools/
│   ├── README.md
│   ├── topic_generator.py
│   ├── ai_prompt_generator.py
│   └── script_optimizer.py
├── workflows/
│   ├── 快速出片流.md
│   └── 深度打造流.md
├── index.html               # 静态项目介绍页
├── README.md
└── README_EN.md
```

## 适合谁

- 健身教练、营养师、中医/养生馆主、健康管理顾问等大健康从业者
- 想把专业能力转成可持续内容输出的创始人或个人品牌操盘手
- 想把内容策划、私域咨询、成交承接整理成 SOP 的团队

## 当前最值得继续补强的方向

- 增加更多细分赛道案例，尤其是睡眠、康复、心理健康、女性健康等。
- 给每个核心 Prompt 增加「输入示例 / 输出示例」，提高第一次使用成功率。
- 为 `index.html` 补充真实截图或录屏，增强 GitHub 首屏转化。

## 🗺️ Roadmap

- [x] 核心 Prompt 结构
- [x] 选题库
- [x] 脚本模板
- [x] 话术库
- [x] 变现设计 Prompt
- [x] 快速出片工作流
- [x] 深度打造工作流
- [x] Python 辅助工具
- [x] 项目介绍页
- [ ] 更多垂类案例
- [ ] Prompt 输入/输出样例
- [ ] 更强的展示素材（截图 / GIF / demo）

## 🤝 贡献

欢迎通过 [Issues](https://github.com/AIPMAndy/IPClawForHealth/issues) 提交问题或建议，也欢迎直接发起 PR。

如果你补充的是行业案例、Prompt 模板或转化 SOP，优先写清楚：

- 适用角色
- 输入条件
- 输出结果
- 是否包含合规或敏感表达风险

## 📄 License

本项目使用 [MIT License](LICENSE)。

## 👨‍💻 作者

**AI酋长Andy**

- GitHub: [AIPMAndy](https://github.com/AIPMAndy)
- 项目主页: [IPClawForHealth](https://github.com/AIPMAndy/IPClawForHealth)
