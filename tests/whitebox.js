function sumar(num1, num2){
    if(typeof num1 !== "number" || typeof num2 !== "number"){
        return "Error debe ingresar un numero"
    }
    return num1 + num2;
}

 resultado = sumar(1,20)
 console.log(resultado)

 