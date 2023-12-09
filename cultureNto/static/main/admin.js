document.addEventListener('DOMContentLoaded', function()
{
    document.body.innerHTML = document.body.innerHTML.replace(new RegExp('\\bPlease correct the errors below\\b', 'g'), 'Форма заполнена неверно');
    document.body.innerHTML = document.body.innerHTML.replace(new RegExp('\\bPlease correct the error below\\b', 'g'), 'Форма заполнена неверно');
});