# 飞书课程顺序播放器

这个工具通过真实浏览器顺序播放课程，减少重复点击。每节最多播放 21 分钟，已处理课程会记录到本机 `course-history.json` 并在以后运行时跳过。它保留人工登录，并在遇到测验、考试、人脸识别或无视频页面时直接跳过，不会代答或修改学习进度。

## 安装

```bash
npm install
cp config.example.json config.json
```

## 使用

启动播放：

```bash
npm start -- "你的飞书课程链接"
```

浏览器打开后，完成登录并进入第一节课程。工具检测到课程后会自动开始，登录状态保存在本机 `.course-profile/` 中。

检查课程页结构：

```bash
npm run inspect -- "你的飞书课程链接"
```

这个命令会输出页面中的视频、可见按钮和链接。若工具找不到“下一节”，可根据输出修改 `config.json`：

```json
{
  "nextTexts": ["下一节", "继续学习"],
  "nextButtonSelectors": [".your-next-button"],
  "lessonLinkSelectors": [".course-list a"]
}
```

## 配置

- `playbackRate`：播放速度，默认 `1`。是否允许倍速取决于课程规则。
- `watchMinutesPerLesson`：每节课程最多播放的分钟数，默认 `21`。
- `pollIntervalMs`：检查播放进度的间隔。
- `blockedTexts`：无视频页面检测到这些文字时记录跳过原因。
- `nextTexts`：用于寻找下一节按钮的精确文案。
- `nextButtonSelectors`：下一节按钮的 CSS 选择器，优先级最高。
- `lessonLinkSelectors`：课程目录链接的 CSS 选择器，作为备用方式。

## 注意

页面结构可能因组织、课程平台版本和权限不同而变化。首次使用建议先运行 `inspect`，再按实际页面调整选择器。工具运行期间不要关闭浏览器窗口。
