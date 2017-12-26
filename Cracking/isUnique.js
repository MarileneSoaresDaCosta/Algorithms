/*
isUnique - pg 90
determine if a string has all unique characters 
*/

function isUnique(string) {
	if(string.length === 0){
		return true;
	}
	string = string.toLowerCase();
	// console.log(string, string.length);
	for (var i = 0; i < string.length - 1; i++){
		for(var j = i + 1; j < string.length; j++) {
			if(string.charAt(i) === string.charAt(j)){
				return false;
			}
		}
	}
	return true;
}


function assertEqual(actual, expected, testName){
  if(actual === expected) {
    console.log('passed [' +testName + ']');
  } else {
  	console.log('FAILED [' +testName+ '] Expected "' +expected+ '", but got "' +actual+ '"'); 
  }
}

assertEqual(isUnique('abc def'), true, 'Unique string');
assertEqual(isUnique(''), true, 'empty string');
assertEqual(isUnique('abc dea'), false, 'not Unique');


