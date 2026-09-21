// Lokalisoi <title> kielivalinnan mukaan (dictin _title tai h1)
(function(){
var en=document.title;
// H1-kaannokset sisaltavat HTML:aa (<em>, &nbsp;). Tagit riisutaan ja
// entiteetit puretaan selaimella — pelkka regex jatti "&nbsp;" nakyviin.
function plain(html){
  var d=document.createElement('div');
  d.innerHTML=String(html);
  return (d.textContent||'').replace(/\s+/g,' ').trim().replace(/\.$/,'');
}
function apply(){
  var l=null;try{l=localStorage.getItem('sansox_lang')}catch(e){}
  if(!l||l==='en'){document.title=en;return;}
  var d=(typeof T!=='undefined')&&T[l];if(!d)return;
  var t=d._title||d.h1;if(!t)return;
  document.title=plain(t)+' | SansOx';}
apply();
document.addEventListener('click',function(e){
  if(e.target.closest&&e.target.closest('.lang'))setTimeout(apply,80);},true);
})();
