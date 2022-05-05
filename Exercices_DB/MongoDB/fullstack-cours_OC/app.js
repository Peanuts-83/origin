const { json } = require('express');
const express = require('express');
const mongoose = require('mongoose');

const Thing = require('./thing')

const app = express()
// console.log('DBPASSWORD -', process.env.DBPASSWORD);
// CONNECT to Atlas Mongodb / database as a service
console.log('ENV -', process.env.DB_URL)
mongoose
    .connect(process.env.DB_URL,
        {
            useNewUrlParser: true,
            useUnifiedTopology: true
        })
    .then(() => console.log('Connexion à mongoDB réussie!'))
    .catch((error) => console.log('Connexion à mongoDB échouée :', error))

/* MIDDLEWARES */
// use = generic / get/post/put/patch etc...
// MUST SEND BACK res.status to avoid error

// intercept any JSON values in body request
app.use(express.json())

// Set HEADERS for all calls
app.use((req, res, next) => {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content, Accept, Content-Type, Authorization');
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE, PATCH, OPTIONS');
    next();
});

// POST create requests / display JSON from body's request
app.post('/api/stuff', (req, res, next) => {
    delete req.body._id
    const thing = new Thing({ ...req.body })
    console.log('Objet créé -\n', thing)
    thing.save()
        .then(() => res.status(200).json({ message: 'Objet créé!' }))
        .catch(error => res.status(400) / json({ error }))
})

// PUT update object
app.put('/api/stuff/:id', (req, res, next) => {
    Thing.updateOne({ _id: req.params.id }, { ...req.body, _id: req.params.id })
        .then(() => res.status(201).json({ message: 'Objet mis à jour.' }))
        .catch(error => res.status(409).json(error))
})

// DELETE object
app.delete('/api/stuff/:id', (req, res, next) => {
    Thing.deleteOne({ _id: req.params.id })
        .then(() => res.status(200).json({ message: 'Objet effacé!'}))
        .catch(error => res.status(400).json( error ))
})

// GET 1 object by id
app.get('/api/stuff/:id', (req, res, next) => {
    Thing.findOne({ _id: req.params.id })
        .then(thing => res.status(200).json(thing))
        .catch(error => res.status(404).json({ error }))
})

// GET requests
app.get('/api/stuff', (req, res, next) => {
    Thing.find()
        .then(things => res.status(200).json(things))
        .catch(error => res.status(400).json({ error }))
});


module.exports = app
