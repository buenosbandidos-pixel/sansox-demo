(function(){
  var h=document.querySelector('.wrap.hero'); if(!h) return;
  if(window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  var b=document.createElement('div'); b.className='bubbles'; b.setAttribute('aria-hidden','true');
  var n=window.innerWidth<641?12:22;
  for(var k=0;k<n;k++){
    var i=document.createElement('i'), s=4+Math.pow(Math.random(),2)*22;
    i.style.width=i.style.height=s+'px';
    i.style.left=(Math.random()*100)+'%';
    i.style.setProperty('--d',(9+Math.random()*12)+'s');
    i.style.setProperty('--w',(-Math.random()*20)+'s');
    i.style.setProperty('--s',((Math.random()*2-1)*28)+'px');
    i.style.setProperty('--o',(.25+Math.random()*.45).toFixed(2));
    b.appendChild(i);
  }
  h.insertBefore(b,h.firstChild);
})();
