bookList = ['bangla book', 'english book', 'math book', 'social science book']

while True:
    create_list = input("What do you want? Enter Choice : read_book / add_book / update_book / delete_book / exit: ")
    if create_list == "exit":
        print("You exist from programme")
        break

#read your book list
    elif create_list == 'read_book':
        print("Congratulations! This is your book: ",bookList)

#add your book list
    elif create_list == 'add_book':
        bookList.append(input("Please add books to your wish list : "))
        print("This is your added list",bookList)

#delete book from your book list
    elif create_list == 'delete_book':
        dl = input("Enter deleted books to your wish list item: ",)
        if dl in bookList:
            bookList.remove(dl)
        else:
            print("Not matched item")
        print("This is your deleted list",bookList)

# update book from your book list
    elif create_list == 'update_book':
        up_wrong = input("Enter  wrong item: ", )
        up_right = input("Enter right item: ", )
        if up_wrong in bookList:
            wr = bookList.index(up_wrong)
            bookList[wr] = up_right
        else:
            print("Not matched item")
        print("This is your updated book list", bookList)

#for right command
    else:
        print("Please enter right information.")