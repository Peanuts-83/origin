import { ActivatedRoute, Router } from '@angular/router';
import { BooksService } from './../../services/books.service';
import { Component, OnInit } from '@angular/core';
import { Book } from '../../models/book.model';

@Component({
    selector: 'app-single-book',
    templateUrl: './single-book.component.html',
    styleUrls: ['./single-book.component.scss']
})
export class SingleBookComponent implements OnInit {

    book!: Book;

    constructor(
        private booksService: BooksService,
        private router: Router,
        private route: ActivatedRoute
    ) {}

    ngOnInit(): void {
        this.book = new Book('','');
        const id = this.route.snapshot.params['id'];
        console.log(id);
        this.booksService.getSingleBook(+id)
            .then((book: any) => {
                this.book = book;
            });
    }

    onBack() {
        this.router.navigate(['/books']);
    }
}
