import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-post',
  templateUrl: './post.component.html',
  styleUrls: ['./post.component.scss']
})
export class PostComponent implements OnInit {
  postDate = new Date();
  @Input() postTitle!: string;
  @Input() postContent!: string;
  love = 0;

  constructor() { }

  ngOnInit(): void {
  }

  onAddLove() {
    return this.love++;
  }

  onRemLove() {
    return this.love--;
  }

}
