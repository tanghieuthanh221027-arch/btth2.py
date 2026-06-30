# cách 1 : vòng lặp for
from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Lê Minh Thu",
        "category": "programming",
        "year": 2022,
        "is_available" : True
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Phạm Lan Hồng",
        "category": "web",
        "year": 2021,
        "is_available" : True
    },
    {
        "id": 3,
        "title": "Database System",
        "author": "Lê Minh Huyền",
        "category": "database",
        "year": 2020,
        "is_available" : False
    },
    {
        "id": 4,
        "title": "Clean Code",
        "author": "Lê Ánh Linh",
        "category": "programming",
        "year": 2008,
        "is_available" : False
    },
    {
        "id": 5,
        "title": "Computer Network",
        "author": "Vũ Hồng Vân",
        "category": "network",
        "year": 2019,
        "is_available" : True
    }
]

@app.get("/books/available")
def get_available_book():
    available_book = []

    for book in books:
        if book["is_available"] == True :
            available_book.append(book)

    if len(available_book) == 0 :
        return {
            "message" : "Không có sách nào hiện có sẵn"
        }
    else :
        return {
            "message" : "Danh sách sách còn có thể mượn",
            "data" : available_book
        }
    
@app.get("/books/borrowed")
def get_borrowed_book():
    borrowed_book = []

    for book in books:
        if book["is_available"] == False :
            borrowed_book.append(book)

    if len(borrowed_book) == 0 :
        return {
            "message" : "Không có sách nào đang được mượn"
        }
    
    else :
        return {
            "message" : "Danh sách sách đang được mượn",
            "data" : borrowed_book
        }
    
# cách 2 : dùng list comprehension
from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Lê Minh Thu",
        "category": "programming",
        "year": 2022,
        "is_available" : True
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Phạm Lan Hồng",
        "category": "web",
        "year": 2021,
        "is_available" : True
    },
    {
        "id": 3,
        "title": "Database System",
        "author": "Lê Minh Huyền",
        "category": "database",
        "year": 2020,
        "is_available" : False
    },
    {
        "id": 4,
        "title": "Clean Code",
        "author": "Lê Ánh Linh",
        "category": "programming",
        "year": 2008,
        "is_available" : False
    },
    {
        "id": 5,
        "title": "Computer Network",
        "author": "Vũ Hồng Vân",
        "category": "network",
        "year": 2019,
        "is_available" : True
    }
]

@app.get("/books/available")
def get_available_book():
    available_book = [book for book in books if book["is_available"] == True]

    if len(available_book) == 0 :
        return {
            "message" : "Không có sách nào hiện có sẵn"
        }
    else :
        return {
            "message" : "Danh sách sách còn có thể mượn",
            "data" : available_book
        }
    
@app.get("/books/borrowed")
def get_borrowed_book():
    borrowed_book = [book for book in books if book["is_available"] == False]

    if len(borrowed_book) == 0 :
        return {
            "message" : "Không có sách nào đang được mượn"
        }
    
    else :
        return {
            "message" : "Danh sách sách đang được mượn",
            "data" : borrowed_book
        }