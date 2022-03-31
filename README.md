# parser_cat_breed

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
and represents data into json format.

Command: scrapy breed -O filename.json
Genarates .json file which contain parsed information about cat from https://catfishes.ru/porody-koshek/ 
```

## Example
```yaml
[
    {
        "catName": "Австралийский мист или австралийская дымчатая кошка",
        "catDescription": "Австралийский мист (англ. Australian mist) или дымчатая кошка по праву носит лейбл «Made in Australia». Дело в том, что ее впервые вывели на этом континенте. Это красивые, умные, игривые кошки с очень мягким характером.",
        "cat_photo_src": "https://catfishes.ru/wp-content/uploads/2021/05/mist1.jpg"
    },
    {
        "catName": "Абиссинская кошка",
        "catDescription": "Абиссинская кошка (англ. Abyssinian cat) получила название по стране из которой она родом, нынешней Эфиопии. Эти кошки подойдут для семей и активных, самостоятельных, позитивных людей. Они недороги в содержании, уравновешены, и при этом умны и уживчивы.Легко привязываются к владельцам и наслаждаются вниманием. Активные и живые, они любят играть с хозяевами, могут даже выучить некоторые трюки. И несмотря на это, абиссинцы не шумные, уживаются с другими животными в доме, ладят с детьми.",
        "cat_photo_src": "https://catfishes.ru/wp-content/uploads/2021/06/abis11.jpg"
    },
    {
        "catName": "Египетская мау",
        "catDescription": "Египетская мау порода натуральных кошек (англ. Egyptian Mau, иногда в русском — египетская мао), шарм которой в контрасте между окрасом шерсти и темными пятнами на ней. Пятна эти индивидуальны и каждая кошка с неповторимым рисунков. Также у них есть рисунок в виде буквы М, расположенный на лбу, над глазами, а глаза как будто подведены макияжем. ",
        "cat_photo_src": "https://catfishes.ru/wp-content/uploads/2021/05/mau5.jpg"
    },
]
```