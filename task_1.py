"""Создать базовый шаблон для интернет-магазина,
содержащий общие элементы дизайна (шапка, меню,
подвал), и дочерние шаблоны для страниц категорий
товаров и отдельных товаров.
Например, создать страницы "Одежда", "Обувь" и "Куртка",
используя базовый шаблон."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/clothes/')
def clothes():
    head = {
        'type': 'Тип товара',
        'sex': 'Мужская / Женская',
        'size': 'Размер',
        'price': 'Стоимость'
    }
    item_list = [
        {
            'type': 'Рубашка',
            'sex': 'Женская',
            'size': 'S',
            'price': 1500
        },
        {
            'type': 'Брюки',
            'sex': 'Мужская',
            'size': 'XL',
            'price': 2000
        }
    ]
    return render_template('clothes.html', **head, item_list=item_list)


@app.route('/shoes/')
def shoes():
    head = {
        'type': 'Тип товара',
        'sex': 'Мужская / Женская',
        'size': 'Размер',
        'price': 'Стоимость'
    }
    item_list = [
        {
            'type': 'Кросовки',
            'sex': 'Женская',
            'size': 36,
            'price': 4000
        },
        {
            'type': 'Туфли',
            'sex': 'Мужская',
            'size': 42,
            'price': 3000
        }
    ]
    return render_template('shoes.html', **head, item_list=item_list)


@app.route('/jacket/')
def jacket():
    head = {
        'type': 'Тип товара',
        'sex': 'Мужская / Женская',
        'size': 'Размер',
        'price': 'Стоимость'
    }
    item_list = [
        {
            'type': 'Пуховик',
            'sex': 'Женская',
            'size': 'L',
            'price': 9000
        },
        {
            'type': 'Дубленка',
            'sex': 'Мужская',
            'size': 'XL',
            'price': 8000
        }
    ]
    return render_template('jacket.html', **head, item_list=item_list)


if __name__ == '__main__':
    app.run(debug=True)
