# YouTube Analytics CLI

CLI приложение для анализа CSV файлов с метриками YouTube.

## Пример запуска

```bash
python -m app.cli --files stats1.csv stats2.csv --report clickbait
```

## Clickbait report

Показывает видео:

CTR > 15
retention_rate < 40

Сортировка по CTR (убывание)
---
