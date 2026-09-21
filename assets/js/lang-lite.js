(function(){
function set(l){try{localStorage.setItem('sansox_lang',l)}catch(e){}
document.documentElement.lang=l;
['en','es','fi'].forEach(function(x){var b=document.getElementById('l-'+x);if(b)b.classList.toggle('on',x===l)});}
['en','es','fi'].forEach(function(x){var b=document.getElementById('l-'+x);if(b)b.onclick=function(){set(x)}});
var sl=null;try{sl=localStorage.getItem('sansox_lang')}catch(e){}
if(sl&&sl!=='en')set(sl);
})();
