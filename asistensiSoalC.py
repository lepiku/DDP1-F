from datetime import date

class Document:
    def __init__(self, authors=None, docDate=None):
        self.__authors = authors
        self.__date = docDate
    
    def getAuthors(self):
        return self.__authors
    
    def addAuthor(self, name):
        self.__authors.append(name)
    
    def getDate(self):
        return self.__date

    def __str__(self):
        return "Authors: {}, Date: {}".format(self.__authors,self.__date)

    def __lt__(self, other):
        return self.getDate() < other.getDate()
    
    def __eq__(self, other):
        return type(self) == type(other)


class Book(Document):
    def __init__(self, authors=None, docDate=None, title=None):
        super().__init__(authors, docDate)
        self.__title = title

    def getTitle(self):
        return self.__title

    def __str__(self):
        return "Authors: {}, Date: {}, Title: {}".format(self.getAuthors(),self.getDate(), self.__title)

class Email(Document):
    def __init__(self, authors=None, docDate=None, subject=None, to=None):
        super().__init__(authors, docDate)
        self.__subject = subject
        self.__to = to

    def getSubject(self):
        return self.__subject
    
    def getTo(self):
        return self.__to

    def __str__(self):
        return "Authors: {}, Date: {}, Subject: {}, To: {}".format(self.getAuthors(),self.getDate(), self.getSubject(), self.getTo())

    
a = Document()
print(a)
b = Book()
print(b)
c = Email()
print(c)
a = Document(["Chairil Anwar"], date(1990, 3, 15))
print(a)
b = Book(["Hinkle", "Elmasri"], date.today(), "Python for Dummy")
print(b)
c = Email(["Super Maung"], date(2018, 1, 5), "Latihan DDP1", "2019@cs.ui.ac.id")
print(c)
print()
print("__________________awal_____")
print(b.getAuthors())
print(b.getTitle())
print(c.getDate())
print(c.getSubject())
print()
print("_____________no 1__________")
print(dir(a))
print(dir(b))
print(dir(c))
print()
print("_____________no 2__________")
print(a.__dict__)
print(b.__dict__)
print(b.__dict__)


class DocList:
    def __init__(self, docs):
        self.dlist = docs
    
    def addDoc(self, doc):
        self.dlist.append(doc)
    
    def __str__(self):
        res = ""
        for doc in self.dlist:
            res += str(doc) + "\n"

        return res

print("--------no 3-")
aDocList = DocList([a, b])
aDocList.addDoc(c)
print(aDocList)

print('-------no 4-')
x = Document(["Aditya"], date.today())
y = Book(["Budi"], date(1990, 3, 15), "judul")
z = Email(["Budianto"], date(2018, 1, 5), "subject", "dia@cs")
aDocList2 = DocList([x, y, z])
print(aDocList2)
aDocList2.dlist.sort()
print(aDocList2)


print("--------no 5-")
x = Document(["pen1"], date.today())
y = Book(["pen1"], date.today(), "judul")
z = Email(["pen1"], date.today(), "subject", "dia@cs")

print("x doc", isinstance(x, Book))
print("y doc", isinstance(y, Email))
print("z doc", isinstance(z, Document))
print("z email", isinstance(z, Email))

print()
print(type(x)==Document)
print(type(y)==Document)
print(type(z)==Document)
print()
x2 = Document(["pen2"], date.today())

print(x == x2)
print(x == y)
print(x == z)
