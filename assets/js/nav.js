/* nav.js — navegação compartilhada entre todas as páginas */
(function () {
  'use strict';

  var nav    = document.querySelector('.navbar');
  var toggle = document.querySelector('.navbar__toggle');
  var links  = document.querySelector('.navbar__links');

  if (!nav) return;

  /* hamburguer */
  if (toggle) {
    toggle.addEventListener('click', function () {
      var isOpen = nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(isOpen));
    });
  }

  /* fecha ao clicar num link */
  if (links) {
    links.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', function () {
        nav.classList.remove('open');
        if (toggle) toggle.setAttribute('aria-expanded', 'false');
      });
    });
  }

  /* marca link ativo */
  var curr = location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.navbar__links a').forEach(function (a) {
    var page = (a.getAttribute('href') || '').split('/').pop().split('#')[0];
    if (page && page === curr) a.classList.add('active');
    if (curr === 'index.html' && (page === 'index.html' || page === '')) {
      a.classList.add('active');
    }
  });
})();
