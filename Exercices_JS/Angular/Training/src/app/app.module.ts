import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { AppareilComponent } from './appareil/appareil.component';
import { AppareilService } from './services/appareil.service';
import { AuthService } from './services/auth.service';
import { AuthComponent } from './auth/auth.component';
import { AppareilViewComponent } from './appareil-view/appareil-view.component';
import { RouterModule, Routes } from '@angular/router';
import { SingleAppareilComponent } from './single-appareil/single-appareil.component';
import { FourOfourComponent } from './four-ofour/four-ofour.component';
import { AuthGard } from './services/auth-gard.service';
import { EditAppareilComponent } from './edit-appareil/edit-appareil.component';
import { UserService } from './services/user.service';
import { UserListComponent } from './user-list/user-list.component';
import { NewUserComponent } from './new-user/new-user.component';
import { HttpClientModule } from '@angular/common/http';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

const appRoutes: Routes = [
    { path: 'appareils', component: AppareilViewComponent },
    { path: 'appareils/:id', canActivate: [AuthGard], component: SingleAppareilComponent},
    { path: 'auth', component: AuthComponent },
    { path: 'users', component: UserListComponent},
    { path: 'newUser', component: NewUserComponent},
    { path: 'editAppareil', canActivate: [AuthGard], component: EditAppareilComponent},
    { path: '', component: AppareilViewComponent},
    { path: 'not-found', component: FourOfourComponent},
    { path: '**', redirectTo: 'not-found'}
]

@NgModule({
    declarations: [
        AppComponent,
        AppareilComponent,
        AuthComponent,
        AppareilViewComponent,
        SingleAppareilComponent,
        FourOfourComponent,
        EditAppareilComponent,
        UserListComponent,
        NewUserComponent
    ],
    imports: [
        BrowserModule,
        FormsModule,
        ReactiveFormsModule,
        RouterModule.forRoot(appRoutes),
        HttpClientModule,
        BrowserAnimationsModule
    ],
    providers: [
        AuthService,
        AppareilService,
        UserService
    ],
    bootstrap: [AppComponent]
})
export class AppModule { }
