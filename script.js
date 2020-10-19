$(document).on('submit','#test',function(e){
	e.preventDefault();
	var name = prompt('enter your name: ')
	
	console.log('Warm greetings '+name)
	
})//to use this you must have ajax/jquery included in your project..

