/* Theme B: mobiilivalikko (hampurilainen). Ilman JS:ää valikko näkyy normaalisti. */
(function(){
  var h=document.querySelector('header'), bar=h&&h.querySelector('.bar'), nav=bar&&bar.querySelector('nav');
  if(!nav) return;
  var lang=(document.documentElement.lang||'en').slice(0,2);
  var L={en:['Menu','Close menu'],fi:['Valikko','Sulje valikko'],es:['Menú','Cerrar menú']}[lang]||['Menu','Close menu'];
  nav.id=nav.id||'site-nav';
  var b=document.createElement('button');
  b.className='menu-btn'; b.type='button';
  b.setAttribute('aria-controls',nav.id); b.setAttribute('aria-expanded','false'); b.setAttribute('aria-label',L[0]);
  var open='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg>';
  var close='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>';
  b.innerHTML=open; bar.appendChild(b); h.classList.add('js-menu');
  function set(o){h.classList.toggle('open',o); b.setAttribute('aria-expanded',o); b.setAttribute('aria-label',L[o?1:0]); b.innerHTML=o?close:open;}
  b.addEventListener('click',function(){set(!h.classList.contains('open'))});
  nav.addEventListener('click',function(e){if(e.target.closest('a')) set(false)});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&h.classList.contains('open')){set(false);b.focus()}});
})();
