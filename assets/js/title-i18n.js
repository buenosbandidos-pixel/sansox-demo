// Lokalisoi <title> kielivalinnan mukaan (dictin _title tai h1)
(function(){
var en=document.title;
function apply(){
  var l=null;try{l=localStorage.getItem('sansox_lang')}catch(e){}
  if(!l||l==='en'){document.title=en;return;}
  var d=(typeof T!=='undefined')&&T[l];if(!d)return;
  var t=d._title||d.h1;if(!t)return;
  t=String(t).replace(/<[^>]*>/g,'').replace(/\s+/g,' ').trim().replace(/\.$/,'');
  document.title=t+' | SansOx';}
apply();
document.addEventListener('click',function(e){
  if(e.target.closest&&e.target.closest('.lang'))setTimeout(apply,80);},true);
})();
