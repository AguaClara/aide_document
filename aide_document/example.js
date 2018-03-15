const translate = require('google-translate-api');

var input;

translate('I spea Dutch').then(res => {console.log(res.from.text.value);})

function trans(input) {
  translate(input).then(res => { return res.from.text.value; });
}

console.log(trans("Hello"));
