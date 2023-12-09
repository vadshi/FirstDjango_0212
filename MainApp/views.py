from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
items = [
   {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
   {"id": 2, "name": "Куртка кожаная", "quantity": 2},
   {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
   {"id": 7, "name": "Картофель фри", "quantity": 0},
   {"id": 8, "name": "Кепка", "quantity": 124},
]


author = {
    "Имя": "Иван",
    "Отчество": "Петрович",
    "Фамилия": "Иванов",
    "телефон": "8-923-600-01-02",
    "email": "vasya@mail.ru"
}


def home(request):
    # text = """
    # <h1>"Изучаем django"</h1>
    # <strong>Автор</strong>: <i>Шиховцов В.В.</i>
    # """
    # return HttpResponse(text)
    context = {
        "name": "Петров Иван Николаевич",
        "email": "my_mail@mail.ru"
    }
    return render(request, "index.html", context)


def about(request):
    text = f"""
    <header>
        / <a href="/">Home</a> / <a href="/items"> Items </a> / <a href="/about"> About </a>
    </header><br><br>
    Имя: <b>{author["Имя"]}</b><br>
    Отчество: <b>{author["Отчество"]}</b><br>
    Фамилия: <b>{author["Фамилия"]}</b><br>
    телефон: <b>{author['телефон']}</b><br>
    email: <b>{author['email']}</b><br>
    """
    return HttpResponse(text)


# url item/1
# url item/2

def get_item(request, item_id: int):
    """ По указанному id возвращаем имя и количество"""
    item = next((item for item in items if item["id"] == item_id), None)
    if item is not None:
        context = {
            "item": item
        }
        return render(request, "item_page.html", context)
    return HttpResponseNotFound(f'Item with id = {item_id} not found.')


# <ol>
#   <li> ... </li>
#   <li> ... </li>
#   <li> ... </li>
#   <li> ... </li>
# </ol>
def get_items(request):
    # result = f"<h2> Список товаров </h2><ol>"
    # for item in items:
    #     result += f"""<li><a href="/item/{item["id"]}"> {item["name"]} </a></li> """
    # result += "</ol>"
    # return HttpResponse(result)
    context = {
        "items": items
    }
    return render(request, "items_list.html", context)