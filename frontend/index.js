console.log('bootcamp');
const bootcamp = document.getElementsByClassName('bootcamp')[0];
bootcamp.innerText = 'Bootcamp';

function functionName1(){
    console.log('ES5 Syntax')
}
functionName1();

const functionName2 = () => {
    console.log('ES6 Syntax')
}
functionName2();

function timeout1(){
    var wait = new Promise((resolve) => {
        setTimeout(function(){
            resolve("Timeout1!");
        }, 5000);
    }).then(text => console.log(text));
}
timeout1();

const timeout2 = () => {
    const wait = new Promise((resolve) => {
        setTimeout(() => {
            resolve("Timeout2!");
        }, 5000);
    });
    wait.then(text => console.log(text));
}
timeout2();

function fetchEndpoint1(){
    fetch('https://jsonplaceholder.typicode.com/todos/1')
        .then(response => response.json())
        .then(json => console.log('ES5', json))
}
fetchEndpoint1();

const fetchEndpoint2 = () => {
    fetch('https://jsonplaceholder.typicode.com/todos')
        .then(response => response.json())
        .then(json => console.log('ES6', json))
}

function postFetchEndpoint1() {
    fetch('https://jsonplaceholder.typicode.com/posts', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            title: 'foo',
            body: 'bar',
            userId: 1,
        })
    })
    .then((response) => response.json())
    .then((json) => {
      console.log(json)
  });
  }
}
fetchEndpoint1();
postFetchEndpoint1();

const postFetchEndpoint2 = () => {
    const postRequest = fetch('https://jsonplaceholder.typicode.com/posts', {
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            title: 'foo',
            body: 'bar',
            userId: 1,
        })
    })
    .then((response) => response.json())
    .then((json) => {
      console.log(json)
  });
  }
}
fetchEndpoint2();
postFetchEndpoint2();


