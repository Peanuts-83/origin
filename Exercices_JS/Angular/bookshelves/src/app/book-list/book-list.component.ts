import { Subscription } from 'rxjs';
import { Router } from '@angular/router';
import { BooksService } from './../services/books.service';
import { Component, OnInit, OnDestroy } from '@angular/core';
import { Book } from '../models/book.model';

@Component({
    selector: 'app-book-list',
    templateUrl: './book-list.component.html',
    styleUrls: ['./book-list.component.scss']
})
export class BookListComponent implements OnInit, OnDestroy {

    books!: Book[];
    booksSubscritpion!: Subscription;

    constructor(
        private booksService: BooksService,
        private router: Router) { }

    ngOnInit(): void {
        this.booksSubscritpion = this.booksService.booksSubject.subscribe(
            (books: Book[]) => {
                this.books = books;
            });
            this.booksService.emitBooks();
    }

    onNewBook() {
        this.router.navigate(['/books/new']);
    }

    onDeleteBook(book: Book) {
        this.booksService.removeBook(book);
    }

    onViewBook(id: number) {
        this.router.navigate(['/books/view', id]);
    }

    ngOnDestroy(): void {
        this.booksSubscritpion.unsubscribe();
    }
}
