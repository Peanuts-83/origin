import { Subject } from 'rxjs';
import firebase from 'firebase';
import { Injectable } from '@angular/core';
import { Book } from '../models/book.model';
import DataSnapshot = firebase.database.DataSnapshot;

@Injectable({
    providedIn: 'root'
})
export class BooksService {
    books: Book[] = [];
    booksSubject = new Subject<Book[]>();

    constructor() {
        this.getBooks();
    }

    emitBooks() {
        this.booksSubject.next(this.books);
    }

    saveBooks() {
        firebase.database().ref('/books').set(this.books);
    }

    getBooks() {
        firebase.database().ref('/books')
            .on('value', (data: DataSnapshot) => {
                this.books === data.val() ? data.val : [];
                this.emitBooks();
            });
    }

    getSingleBook(id: number) {
        return new Promise(
            (resolve, reject) => {
                firebase.database().ref('/books' + id).once('value')
                    .then(
                        (data: DataSnapshot) => { resolve(data.val()); },
                        (error) => { reject(error); });
            });
    }

    createNewBook(newBook: Book) {
        this.books.push(newBook);
        this.saveBooks();
        this.emitBooks();
    }

    removeBook(book: Book) {
        const bookIndex = this.books.findIndex(
            (bookElem) =>  {
                if (bookElem === book) {
                    return true;
                }
                return false;
            }
        )
        this.books.splice(bookIndex, 1);
        this.saveBooks();
        this.emitBooks();
    }

}
