from book import book
from fastapi import FastAPI
app = FastAPI()

allBooks:book = list()

# if __name__ == "__main__":
#     config = uvicorn.Config("main:app", port=8080, log_level="info")
#     server = uvicorn.Server(config)
#     server.run()

@app.post('/books')
async def post(bookjszdyhfcg:book):
    # mybook = book(title,author,year)
    allBooks.append(bookjszdyhfcg)
    return bookjszdyhfcg

@app.get('/books')
async def getAll():
    return allBooks

@app.get('/books/{id}')
async def getBookID(id:int):
    for aBook in allBooks:
        if(aBook.bookID==id):
            return aBook
    

@app.post('/books/{id}')
async def putUpdatedBook(id:int, aBook:book):
    await delete(id)
    await post(aBook)
    #use request to update

@app.delete('/books/{id}')
async def delete(id:int):
    bookToDel:book = await getBookID(id)
    print(bookToDel)
    if bookToDel:
        allBooks.remove(bookToDel)
    # bookToDel = None