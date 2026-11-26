# pairwise-dereverb-tail-suppress

## 领域

游戏、图形与多媒体

## 主题

音频去混响与尾音抑制

## 说明

RT60 时变估计、早期反射保留、推理延迟自适应。

初始状态下 `av/dereverb.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
