var keySize = 256;
var ivSize = 128;
var iterations = 100;



function encrypt (msg, pass) {
  var salt = CryptoJS.lib.WordArray.random(128/8);

  var key = CryptoJS.PBKDF2(pass, salt, {
      keySize: keySize/32,
      iterations: iterations
    });

  var iv = CryptoJS.lib.WordArray.random(128/8);

  var encrypted = CryptoJS.AES.encrypt(msg, key, { 
    iv: iv, 
    padding: CryptoJS.pad.Pkcs7,
    mode: CryptoJS.mode.CBC

  });

  // salt, iv will be hex 32 in length
  // append them to the ciphertext for use  in decryption
  var transitmessage = salt.toString()+ iv.toString() + encrypted.toString();
  return transitmessage;
}



function enc(f) {
	/// Реализовать алгоритм забирания текста,
	/// шифрования и отправки на сервер.
	var page = document.forms["page"].elements["id_text_rich"].value;
	var password = "0000"
	document.forms["page"].elements["id_text_rich"].value = encrypt(page, password);
	f.submit();	
}
// ----------------------------------------------------------------