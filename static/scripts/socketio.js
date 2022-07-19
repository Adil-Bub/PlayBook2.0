document.addEventListener('DOMContentLoaded', () => {
    const socket = io();

    socket.on('message', (data) => {
        const card = document.createElement('div')
        card.classList.add('card', 'mb-2')
        const card_header = document.createElement('div')
        card_header.classList.add('card-header')
        card_header.innerHTML = data[0]
        const card_body = document.createElement('div')
        card_body.classList.add('card-body')
        const card_title = document.createElement('h4')
        card_title.classList.add('card-title')
        card_title.innerHTML = data[1]
        const card_text = document.createElement('p')
        card_text.classList.add('card-text')
        card_text.innerHTML = data[2]
        card_body.append(card_title, card_text)
        card.append(card_header, card_body)
        const parent = document.getElementById('posts')
        parent.append(card)
    });

    document.querySelector('#sendMessage').onclick = () => {
        const username = document.querySelector('#username').value
        const content = document.querySelector('#content').value
        socket.send([username, content])
    }
})