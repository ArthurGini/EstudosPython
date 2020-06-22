let string = "Aquela boa e velha frase";
let maior = "";

//Separando a string por espaços
string.split(" ").forEach(word => { 
    if (word.trim().length > maior.length) {
        maior = word.trim();
    }
});

console.log(maior);

//Também transformo a string em uma lista com o split, mas utilizo do reduce para retornar a maior palavra
let bigger = string.split(" ").reduce( (acumulador, valorCorrente) => {
    if (acumulador.length < valorCorrente.trim().length) {
      return valorCorrente.trim();
    }
return acumulador;
},"");

console.log(bigger);