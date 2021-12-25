//Комментарий к использованию:
//Вызываем функцию PrefToInf и вбиваем наше выражение
//Пример: PrefToInf("(+ 9(- 9 0)") --> 9+9-0
//пс. пробелы между операциями и числами важны

function PrefToInf(line) {
	var op = {"+":true, "-":true, "/":true, "*":true, "%":true};
	var split = line.split(/\(|\)| /);
	for(var i=0;i<split.length;i++) {
		if(split[i] === "" || split[i] === undefined) {
			split.splice(i, 1);
		}
	}
	for(var j=0;j<split.length-2;j++) {
		if(split[j] in op && /[0-9]+/.test(split[j+1]) && /[0-9]+/.test(split[j+2])) {
			var t = split[j];
			split[j] = split[j+1];
			split[j+1] = t;
		}
		else if(split[j] in op && /[0-9]+/.test(split[j+1]) && split[j+2] in op){
			var s = split[j];
			split[j] = split[j+1];
			split[j+1] = s;			
		}
	}
	return split.join(" ");
}
