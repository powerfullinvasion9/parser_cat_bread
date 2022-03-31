# parser_cat_bread

## Clone
```bash
git clone git@github.com:powerfullinvasion9/parser_cat_bread.git
```

## Instalation
```bash
pip install poetry
poetry install
poetry shell
```

## Usage
```bash
scrapy crawl breed -O filename.json
```

## Description
```bash
Simple application that parse: https://catfishes.ru/porody-koshek/ 
and represents data into json format
```

## Example
```yaml
[
    {
        "catName": "Австралийский мист или австралийская дымчатая кошка",
        "catDescription": "Австралийский мист (англ. Australian mist) или дымчатая кошка по праву носит лейбл «Made in Australia». Дело в том, что ее впервые вывели на этом континенте. Это красивые, умные, игривые кошки с очень мягким характером.",
        "cat_photo_src": "https://catfishes.ru/wp-content/uploads/2021/05/mist1.jpg"
    },
]
```