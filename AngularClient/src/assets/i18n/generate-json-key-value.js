if(!process.argv[2]) {
	return;
}

let key = process.argv[2];
console.log("KEY RECIEVED : ", key);

var ncp = require("copy-paste");

let toTitleCase = (toTransform) => {
  return toTransform.replace(/\b([a-z])/g, (_, initial) => {
      return initial.toUpperCase();
  });
}

let replaceUnderscore = (str) => {
	return str.replace(/_/g, ' ');
}

let noUnderscore = replaceUnderscore(key.toLowerCase());
let title = toTitleCase(noUnderscore);

let result = "\""+key+"\": \""+title+"\",";

ncp.copy(result, () => {
  console.log("RESULT : ", result);
});