/*!
* Start Bootstrap - Business Casual v7.0.8 (https://startbootstrap.com/theme/business-casual)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-business-casual/blob/master/LICENSE)
*/
// Highlights current date on contact page
window.addEventListener('DOMContentLoaded', event => {
    const listHoursArray = document.body.querySelectorAll('.list-hours li');
   
    const dayIndex = new Date().getDay();

    if (dayIndex >= 0 && dayIndex < listHoursArray.length) {
    listHoursArray[dayIndex].classList.add('today');
} })

console.log(listHoursArray.length);
console.log(dayIndex);
