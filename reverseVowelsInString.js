function reverseVowels(str) {
    let vowelRR = str.split('').filter(x=> /[^aeiou]/i.test(x) ? '' : x).reverse()
    let vowelPH = str.split('').map(x=> /[^aeiou]/i.test(x) ? x : '#')
    let len = str.length
    let results = [];
    while(vowelPH.length > 0){
      checkChar = vowelPH.shift()
      if(checkChar=='#'){
        replChar = vowelRR.shift()
        checkChar = replChar
        results.push(checkChar)
      }else{
        results.push(checkChar)
      }
    }
    return results.join('')
  }

console.log(reverseVowels("Hello!"))//--> "Holle!"
console.log(reverseVowels("Tomatoes"))//--> "Temotaos"
console.log(reverseVowels("Reverse Vowels In A String"))//--> "RivArsI Vewols en e Streng"