let first_message = true;
let message = document.querySelector('.text');
let parent = document.querySelector('.happy-valentines');

parent.addEventListener('click', function(e) {
    fetch('/message?first_message='+ first_message)
    .then(response => response.json())
    .then(data => {
        console.log(data.msg)
        message.innerHTML = data.msg
        first_message = false
    })
}, false)