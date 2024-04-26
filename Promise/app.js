let favNumber = 19;
let baseURL = "http://numbersapi.com";


// 1. Number Facts
$.getJSON(`${baseURL}/${favNumber}?json`).then(data => {
    console.log(data);
});

// 2. Multiple Number Facts
let favNumbers = [19, 20, 21];
$.getJSON(`${baseURL}/${favNumbers}?json`).then(data => {
    console.log(data);
});

// 3. Multiple Number Facts with Promise.all
Promise.all(
  Array.from({ length: 4 }, () => {
    return $.getJSON(`${baseURL}/${favNumber}?json`);
  })
).then(facts => {
    facts.forEach(data => $("body").append(`<p>${data.text}</p>`));
});
  