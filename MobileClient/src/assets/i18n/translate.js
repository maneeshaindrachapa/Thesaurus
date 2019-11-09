const translate = require('google-translate-api');
let fs = require('fs');
let engObj = JSON.parse(fs.readFileSync('en.json', 'utf8'));

let resultKeyValue = new Array();
let keyValue = new Array();
let index;

let randomInt = (min,max) => {
    return Math.floor(Math.random()*(max-min+1)+min);
}

let writeFile = () => {
	let translatedObj = {};
	resultKeyValue.forEach((obj) => {
		translatedObj[obj.key] = obj.value;
	});
	var json = JSON.stringify(translatedObj);
	fs.writeFile('si.json', json);
};

let getTranslation = (key, value) => {
	translate(value, { from: 'en', to: 'si' }).then((res) => {
		console.log(res.text);
		resultKeyValue.push({
			key: key,
			value: res.text
		});
		if(index < keyValue.length-1) {  //keyValue.length-1
			setTimeout(() => {
				index++;
				getTranslation(keyValue[index].key, keyValue[index].value)
			}, 5000 + randomInt(-5,5));
		} else {
			writeFile();
		}
			
	}).catch(err => {
		console.log(err);
		writeFile();
	});
}


for (var key in engObj) {
	keyValue.push({
		key: key,
		value: engObj[key]
	})
}



if(keyValue.length > 0) {
	index = 0;
	getTranslation(keyValue[0].key, keyValue[0].value);
}




