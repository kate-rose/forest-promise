"""Wrap the artifact source page into a standalone index.html for GitHub Pages.
Source: /Users/kate/Ferric/drafts/2026-09-25_forest-check-brief.html (the published artifact's file)."""
import sys, pathlib
SRC = pathlib.Path('/Users/kate/Ferric/drafts/2026-09-25_forest-check-brief.html')
OUT = pathlib.Path(__file__).resolve().parent.parent / 'index.html'
src = SRC.read_text()
head = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Independent analysis of Skamania County's federal forest payments: the Secure Rural Schools decline, how PILT's subtraction and population ceiling limit the offset, why the 1% levy lid can't backfill it, and the 29 counties in the same bind.">
<meta property="og:title" content="The Forest Promise">
<meta property="og:description" content="What the nation promised the counties that keep its forests: where Skamania's forest money went, why PILT can't replace it, and 29 counties in the same bind.">
<meta property="og:type" content="article">
<base target="_blank">
<style>*,*::before,*::after{box-sizing:border-box}html{-webkit-text-size-adjust:100%}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
<script>
(function(){try{var t=new URLSearchParams(location.search).get('theme');if(t==='light'||t==='dark')document.documentElement.setAttribute('data-theme',t)}catch(e){}})();
</script>
'''
resize = '''
<script>
(function(){
  if(window.parent===window)return;
  var last=0;
  function send(){var h=Math.ceil(document.documentElement.scrollHeight);if(h!==last){last=h;window.parent.postMessage({type:'forest-promise:height',height:h},'*')}}
  window.addEventListener('load',send);
  if(window.ResizeObserver)new ResizeObserver(send).observe(document.documentElement);
  setTimeout(send,1500);
})();
</script>
'''
i = src.index('<div class="wrap">')
OUT.write_text(head + src[:i] + '</head>\n<body>\n' + src[i:] + resize + '</body>\n</html>\n')
print('wrote', OUT, OUT.stat().st_size)
