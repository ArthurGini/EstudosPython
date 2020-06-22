//String que será avaliada
let string = "Bom dia a todos!";

//Declaro a maior string vazia
let big = "";

//Transformo a string em uma lista com o split, separando por espaços em branco
string.split(" ").forEach(word => {
  if (word.trim().length > big.length) {
    big = word.trim();
  }
});

console.log(big);

//Também transformo a string em uma lista com o split, mas utilizo do reduce para retornar a maior palavra
let bigger = string.split(" ").reduce( (acumulador, valorCorrente) => {
  if (acumulador.length < valorCorrente.trim().length) {
    return valorCorrente.trim();
  }

  return acumulador;
}, "");

console.log(bigger);

//Novamente o split, mas dessa fez é efetuado um for simples
let palavras = string.split(" ");
let bigFor = "";

for (word of palavras) {
  if (word.trim().length > bigFor.length) {
    bigFor = word.trim();
  }