const translate = require('google-translate-api');
let text = 'I spea Dutch!';
translate(text).then(res =>{res.text});
