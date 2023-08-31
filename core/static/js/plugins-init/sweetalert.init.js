"use strict"
const html_stuff = document.getElementById('rpnse_body')
let url = html_stuff.dataset['url_reponse']
let concurent_nom = html_stuff.dataset['concurent_nom']


document.querySelector(".sweet-wrong").onclick = function() {
        fetch(url, {
                method: 'POST',
                headers: {
                    'CONTENT-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({ 'reponse': 0, 'concurent': concurent_nom, 'question': numero_global })
            })
            .then((response) => {
                return response.json()
            })
            .then((data) => {
                if (data == 200) {
                    sweetAlert("Oops...", "Mauvaise Reponse " + concurent_nom + " !!", "error")
                    document.getElementById('confirms').style.display = 'none'
                    document.getElementById('replique').style.display = 'block'
                }
                if (data == 400) {
                    location.reload()
                }
            })

    },


    document.querySelector(".sweety-wrong").onclick = function() {
        var e = document.getElementById('replique_select').value
        fetch(url, {
                method: 'POST',
                headers: {
                    'CONTENT-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({ 'reponse': 4, 'concurent': e, 'question': numero_global })
            })
            .then((response) => {
                return response.json()
            })
            .then((data) => {
                if (data == 200) {
                    sweetAlert("Oops...", "Mauvaise Replique " + e + "!!", "error")
                }
                if (data == 400) {
                    swal("Conflit!! l'operation ne s'est pas terminee, vous essayer peut etre d'accorder une replique rate et une replique repondu a la meme personne et pour la meme question.")
                }
            })
    },
    // document.querySelector(".sweet-text").onclick = function () { swal("Hey, Here's a message !!", "It's pretty, isn't it?") },
    document.querySelector(".sweet-success").onclick = function() {
        fetch(url, {
                method: 'POST',
                headers: {
                    'CONTENT-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({ 'reponse': 1, 'question': numero_global, 'concurent': concurent_nom })
            })
            .then((response) => {
                return response.json()
            })
            .then((data) => {
                if (data == 200) {
                    swal("Bonne reponse pour !!", "Bravo Vous avez juste " + concurent_nom + " !!", "success")
                    document.getElementById('confirms').style.display = 'none'
                }
                if (data == 400) {
                    swal("Bonne reponse pour !!", "Nope il y a une erreur " + concurent_nom + " !!", "success")
                    // location.reload()
                }
            })

    },

    document.querySelector(".sweety-success").onclick = function() {
        var e = document.getElementById('replique_select').value
        fetch(url, {
                method: 'POST',
                headers: {
                    'CONTENT-Type': 'application/json',
                    'X-CSRFToken': csrftoken
                },
                body: JSON.stringify({ 'reponse': 3, 'concurent': e, 'question': numero_global })
            })
            .then((response) => {
                return response.json()
            })
            .then((data) => {
                if (data == 200) {
                    swal("Bonne replique !!", "Bravo Vous avez juste " + concurent_nom + " !!", "success")
                }
                if (data == 400) {
                    swal("Conflit!! l'operation ne s'est pas terminee, vous essayer peut etre d'accorder une replique rate et une replique repondu a la meme personne et pour la meme question.")
                }

            })
    }