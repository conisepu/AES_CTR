// ==UserScript==
// @name         testing2
// @match        file:///C:/Users/ConiPum/holamundo.html
// @include       *
// @require      https://cdnjs.cloudflare.com/ajax/libs/aes-js/3.1.2/index.min.js
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.2/rollups/aes.js
// @grant        GM_setValue
// ==/UserScript==



var id,iv,texto_cifrado,key, int_termino_iv,int_termino_texto_cifrado, iv_bytes, text, encryptedBytes, aes, decryptedBytes, decryptedText

var ivid = "iv-P";
var AESid= "AES-P";
var algorithm= "algorithm";


id = document.getElementsByClassName(algorithm)[0].id;
console.log(id);

var n = id.length;
int_termino_iv = id.indexOf("b'", 0);
iv= id.substring(0,int_termino_iv);
int_termino_texto_cifrado = id.indexOf("'", int_termino_iv + 2);
texto_cifrado= id.substring(int_termino_iv + 2 ,int_termino_texto_cifrado);
key= id.substring(int_termino_texto_cifrado + 3, n-1);
//////////////////////////////////////////////////
console.log(parseInt(iv));
key = aesjs.utils.hex.toBytes(key);
console.log(key);

var aesCtr = new aesjs.ModeOfOperation.ctr(key, new aesjs.Counter(parseInt(iv)));
console.log(texto_cifrado)
decryptedBytes = aesCtr.decrypt(texto_cifrado);


// decryptedText = aesjs.utils.utf8.fromBytes(decryptedBytes);
// console.log(decryptedText);
