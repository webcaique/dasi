function calcular(soma1, soma2) {
    return soma1 + soma2;
}

const promise = new Promise(function (resolve, reject) {
    const soma1 = 2;
    const soma2 = 5;

    const result = calcular(soma1, soma2);

    if (result != null) {
        resolve(result);
    } else {
        reject(false);
    }
});

promise
    .then( (res) => {
        console.log(`O resultado foi: ${res}`);
    })
    .catch(function (error) {
        console.error("Houve um erro na função: ", error);
    });