class Book:
    book_name="Harry Potter"
    authors_name="J. K. Rowling"
    book_description="Book of magical world."
    release_date=26
    release_month="June"
    release_year=1997

harry=Book()
print("Name : ",harry.book_name)
print("Author : ",harry.authors_name)
print("Description : ",harry.book_description)
print(harry.release_date)
print(harry.release_month)
print(harry.release_year)