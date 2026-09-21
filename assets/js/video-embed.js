// Tekstitetty upotus: kieli seuraa sivuston kielivalintaa, ei nappeja.
(function(){
var v=document.getElementById('pv'); if(!v) return;
var sub=document.getElementById('pvsub');
function lang(){var l=null;try{l=localStorage.getItem('sansox_lang')}catch(e){};return l||'en';}
function tracks(){return Array.prototype.slice.call(v.textTracks);}
function render(){
  var l=lang(), t=tracks().filter(function(x){return x.language===l})[0]||tracks().filter(function(x){return x.language==='en'})[0];
  var c=t&&t.activeCues&&t.activeCues[0];
  sub.textContent=c?c.text:'';}
function arm(){tracks().forEach(function(t){t.mode='hidden';t.addEventListener('cuechange',render);});}
v.addEventListener('loadedmetadata',arm); arm();
if(window.__setLang){var old=window.__setLang;window.__setLang=function(l){old(l);render();};}
})();
