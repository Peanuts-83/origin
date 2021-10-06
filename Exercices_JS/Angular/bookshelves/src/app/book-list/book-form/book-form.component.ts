import { BooksService } from './../../services/books.service';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Component, OnInit } from '@angular/core';
import { Book } from '../../models/book.model';
import { Router } from '@angular/router';

@Component({
    selector: 'app-book-form',
    templateUrl: './book-form.component.html',
    styleUrls: ['./book-form.component.scss']
})
export class BookFormComponent implements OnInit {

    bookForm!: FormGroup;
    fileUrl!: string;
    fileIsUploading = false;
    fileUploaded = false;

    constructor(
        private formBuilder: FormBuilder,
        private router: Router,
        private booksService:BooksService
    ) {}

    ngOnInit(): void {
        this.initForm();
    }

    initForm() {
        this.bookForm = this.formBuilder.group({
            title: ['', Validators.required],
            author: ['', Validators.required],
            synopsis: ''
        });
    }

    onSaveBook() {
        const title = this.bookForm.get('title')?.value;
        const author = this.bookForm.get('author')?.value;
        const synopsis = this.bookForm.get('synopsis')?.value;
        const newBook = new Book(title, author);
        newBook.synopsis = synopsis;
        if (this.fileUrl && this.fileUrl !== '') {
            newBook.photo = this.fileUrl;
        }
        this.booksService.createNewBook(newBook);
        this.router.navigate(['/books']);
    }

    onUploadFile(file: File) {
        this.fileIsUploading = true;
        this.booksService.uploadFile(file)
            .then((url: any) => {
                typeof url === 'string' ? this.fileUrl = url : null;
                this.fileIsUploading = false;
                this.fileUploaded = true;
            });
    }

    detectFiles(event: any) {
        this.onUploadFile(event.target.files[0]);
    }
}
