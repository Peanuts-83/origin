import { Subscription } from 'rxjs';
import { Router } from '@angular/router';
import { BooksService } from '../services/books.service';
import { Component, OnInit, OnDestroy } from '@angular/core';
import { Book } from '../models/book.model';
import { AuthGuardService } from '../services/auth-guard.service';

@Component({
    selector: 'app-book-list',
    templateUrl: './book-list.component.html',
    styleUrls: ['./book-list.component.scss']
})
export class BookListComponent implements OnInit, OnDestroy {

    books!: Book[];
    booksSubscritpion!: Subscription;
    isAuth = false;

    constructor(
        private booksService: BooksService,
        private router: Router,
        private authGuardService: AuthGuardService) {
            /* alert('test running...'); */

        }

    ngOnInit(): void {
        this.booksSubscritpion = this.booksService.booksSubject.subscribe(
            (books: Book[]) => {
                this.books = books;
            }
        );
        this.booksService.emitBooks();
    }

    onNewBook() {
        this.router.navigate(['/books','new']);
    }

    onDeleteBook(book: Book) {
        this.booksService.removeBook(book);
    }

    onViewBook(id: number) {
        this.router.navigate(['/books','view', id]);
    }

    ngOnDestroy(): void {
        this.booksSubscritpion.unsubscribe();
    }
}
