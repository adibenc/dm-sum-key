# Automatic Text Summarization (ATS)

2022 Data mining project

## get articles
```
https://duckduckgo.com/?q=site%3Atirto.id+pertanian&ia=web

$(".result__url").each((i,e)=>{console.log(e.href)})

$(".news-detail-title").text()
$("article")[0].innerText

```

## triages
1. sumy
```
sumy text-rank --url=https://tirto.id/pengertian-tanaman-pangan-dan-contohnya-padi-jagung-hingga-ubi-glEd
```

2. jsonl to jsonobj
```python
import pandas as pd
jsonObj = pd.read_json(path_or_buf=file_path, lines=True)
```

## thanks
https://github.com/kata-ai/indosum
https://github.com/har07/PySastrawi
https://gist.github.com/BrambleXu/3d47bbdbd1ee4e6fc695b0ddb88cbf99#file-textrank4keyword-py
