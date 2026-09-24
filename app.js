/**
 * CV Interactivo - León Munitz (Versión 2)
 * Características: Modo oscuro fijo permanente, Acordeones colapsables para vista limpia,
 * Modal de Historial Técnico Detallado (14 puestos), Consultas contextuales directas,
 * y Easter Egg adaptado a móviles (Brave Android / iOS touch & click).
 */

document.addEventListener('DOMContentLoaded', () => {
  initCollapsibleCards();
  initTechnicalHistoryModal();
  initInquiryModal();
  initEasterEgg();
  initCopyButtons();
  initGlobalExpandCollapse();
  
  // Inicializar iconos de Lucide
  if (window.lucide) {
    window.lucide.createIcons();
  }
});

/* ==========================================================================
   1. ACORDEÓN DE TARJETAS DE EXPERIENCIA (VISTA LIMPIA COLAPSADA POR DEFECTO)
   ========================================================================== */
function initCollapsibleCards() {
  const toggleButtons = document.querySelectorAll('.toggle-experience-card');

  toggleButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      // Evitar que el clic en el botón active otros eventos
      e.stopPropagation();
      const card = btn.closest('.experience-card');
      if (!card) return;

      const content = card.querySelector('.collapsible-content');
      const chevron = card.querySelector('.card-chevron');
      const label = card.querySelector('.card-toggle-label');

      const isExpanded = content.classList.contains('expanded');

      if (isExpanded) {
        content.classList.remove('expanded');
        btn.setAttribute('aria-expanded', 'false');
        if (chevron) chevron.style.transform = 'rotate(0deg)';
        if (label) label.textContent = 'Ver detalles y logros ▼';
      } else {
        content.classList.add('expanded');
        btn.setAttribute('aria-expanded', 'true');
        if (chevron) chevron.style.transform = 'rotate(180deg)';
        if (label) label.textContent = 'Ocultar detalles ▲';
      }
    });
  });
}

function initGlobalExpandCollapse() {
  const btnToggleAll = document.getElementById('btn-toggle-all-cards');
  if (!btnToggleAll) return;

  let allExpanded = false;

  btnToggleAll.addEventListener('click', () => {
    allExpanded = !allExpanded;
    const cards = document.querySelectorAll('.experience-card');

    cards.forEach(card => {
      const content = card.querySelector('.collapsible-content');
      const btn = card.querySelector('.toggle-experience-card');
      const chevron = card.querySelector('.card-chevron');
      const label = card.querySelector('.card-toggle-label');

      if (allExpanded) {
        content.classList.add('expanded');
        if (btn) btn.setAttribute('aria-expanded', 'true');
        if (chevron) chevron.style.transform = 'rotate(180deg)';
        if (label) label.textContent = 'Ocultar detalles ▲';
      } else {
        content.classList.remove('expanded');
        if (btn) btn.setAttribute('aria-expanded', 'false');
        if (chevron) chevron.style.transform = 'rotate(0deg)';
        if (label) label.textContent = 'Ver detalles y logros ▼';
      }
    });

    btnToggleAll.innerHTML = allExpanded
      ? '<i data-lucide="chevrons-up" class="w-4 h-4"></i> Colapsar todas'
      : '<i data-lucide="chevrons-down" class="w-4 h-4"></i> Expandir todas';
    
    if (window.lucide) window.lucide.createIcons();
  });
}

/* ==========================================================================
   2. MODAL DE HISTORIAL TÉCNICO DETALLADO (12+ AÑOS EN TERRENO)
   ========================================================================== */
function initTechnicalHistoryModal() {
  const modal = document.getElementById('technical-history-modal');
  const btnOpen = document.getElementById('btn-open-tech-history');
  const btnClose = document.getElementById('close-tech-history-btn');
  const backdrop = document.getElementById('tech-history-backdrop');
  const searchInput = document.getElementById('tech-history-search');

  function openTechModal() {
    if (!modal) return;
    modal.classList.remove('hidden');
    modal.classList.add('flex');
    document.body.style.overflow = 'hidden';
    if (searchInput) searchInput.focus();
  }

  function closeTechModal() {
    if (!modal) return;
    modal.classList.add('hidden');
    modal.classList.remove('flex');
    document.body.style.overflow = '';
  }

  if (btnOpen) btnOpen.addEventListener('click', openTechModal);
  if (btnClose) btnClose.addEventListener('click', closeTechModal);
  if (backdrop) backdrop.addEventListener('click', closeTechModal);

  // Filtro de búsqueda rápida en el modal de puestos técnicos
  if (searchInput) {
    searchInput.addEventListener('input', () => {
      const term = searchInput.value.toLowerCase().trim();
      const techCards = document.querySelectorAll('.tech-history-item');

      techCards.forEach(item => {
        const text = item.textContent.toLowerCase();
        if (text.includes(term)) {
          item.classList.remove('hidden');
        } else {
          item.classList.add('hidden');
        }
      });
    });
  }

  // Cerrar con tecla Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal && !modal.classList.contains('hidden')) {
      closeTechModal();
    }
  });
}

/* ==========================================================================
   3. MODAL DE CONSULTAS DIRECTAS CONTEXTUALES (WHATSAPP & CORREO)
   ========================================================================== */
function initInquiryModal() {
  const modal = document.getElementById('inquiry-modal');
  const modalBackdrop = document.getElementById('modal-backdrop');
  const closeBtn = document.getElementById('close-modal-btn');
  const contextTitle = document.getElementById('modal-context-title');
  const contextDescription = document.getElementById('modal-context-description');
  const customMessageInput = document.getElementById('modal-custom-message');
  const sendWhatsAppBtn = document.getElementById('btn-send-whatsapp');
  const sendEmailBtn = document.getElementById('btn-send-email');

  let currentContext = {
    title: 'Consulta General',
    subject: 'Consulta sobre tu perfil profesional',
    defaultText: 'Hola León, estuve viendo tu perfil interactivo y me gustaría conversar sobre una oportunidad.'
  };

  // Delegación de eventos para botones de consulta (tanto en experiencia principal como en el historial técnico)
  document.addEventListener('click', (e) => {
    const btn = e.target.closest('.btn-inquire');
    if (!btn) return;

    e.stopPropagation();
    const topic = btn.getAttribute('data-topic') || 'Experiencia';
    const detail = btn.getAttribute('data-detail') || '';
    
    currentContext = {
      title: topic,
      subject: `Consulta sobre: ${topic}`,
      defaultText: `Hola León, estuve viendo tu CV interactivo y me interesó mucho tu experiencia en "${topic}". Me gustaría consultarte sobre: ${detail || 'cómo encaraste este desafío.'}`
    };

    if (contextTitle) contextTitle.textContent = currentContext.title;
    if (contextDescription) contextDescription.textContent = detail ? `Foco: ${detail}` : 'Envía tu consulta directamente a mi WhatsApp o Correo.';
    if (customMessageInput) customMessageInput.value = currentContext.defaultText;

    openModal();
  });

  function openModal() {
    if (!modal) return;
    modal.classList.remove('hidden');
    modal.classList.add('flex');
    document.body.style.overflow = 'hidden';
  }

  function closeModal() {
    if (!modal) return;
    modal.classList.add('hidden');
    modal.classList.remove('flex');
    document.body.style.overflow = '';
  }

  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  if (modalBackdrop) modalBackdrop.addEventListener('click', closeModal);

  // Enviar por WhatsApp
  if (sendWhatsAppBtn) {
    sendWhatsAppBtn.addEventListener('click', () => {
      const msg = customMessageInput ? customMessageInput.value.trim() : currentContext.defaultText;
      const phone = '5491164204035';
      const url = `https://wa.me/${phone}?text=${encodeURIComponent(msg)}`;
      window.open(url, '_blank');
      closeModal();
    });
  }

  // Enviar por Correo Electrónico
  if (sendEmailBtn) {
    sendEmailBtn.addEventListener('click', () => {
      const msg = customMessageInput ? customMessageInput.value.trim() : currentContext.defaultText;
      const email = 'munitz.2027@gmail.com';
      const subject = encodeURIComponent(currentContext.subject);
      const body = encodeURIComponent(msg);
      window.location.href = `mailto:${email}?subject=${subject}&body=${body}`;
      closeModal();
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal && !modal.classList.contains('hidden')) {
      closeModal();
    }
  });
}

/* ==========================================================================
   4. EASTER EGG ADAPTADO A MÓVILES (BRAVE ANDROID, TOUCH & CLICK)
   ========================================================================== */
function initEasterEgg() {
  const btnYes = document.getElementById('btn-hire-yes');
  const btnNo = document.getElementById('btn-hire-no');
  const feedbackMsg = document.getElementById('hire-feedback');
  
  if (!btnYes || !btnNo) return;

  let noClickCount = 0;

  // Botón SÍ: Confetti festivo y apertura de contacto directo
  const handleYes = (e) => {
    if (e) e.preventDefault();
    triggerCelebration();

    if (feedbackMsg) {
      feedbackMsg.innerHTML = '🎉 <span class="font-bold text-emerald-400">¡Excelente decisión!</span> Abriendo canales de contacto directo...';
      feedbackMsg.classList.remove('hidden');
    }

    setTimeout(() => {
      const modal = document.getElementById('inquiry-modal');
      const contextTitle = document.getElementById('modal-context-title');
      const contextDescription = document.getElementById('modal-context-description');
      const customMessageInput = document.getElementById('modal-custom-message');

      if (contextTitle) contextTitle.textContent = '¡Propuesta de Contratación / Colaboración! 🚀';
      if (contextDescription) contextDescription.textContent = 'Conversemos para coordinar una reunión o entrevista.';
      if (customMessageInput) {
        customMessageInput.value = 'Hola León, revisé tu perfil y CV interactivo y me gustaría hablar contigo sobre una propuesta para sumarte a nuestro equipo.';
      }

      if (modal) {
        modal.classList.remove('hidden');
        modal.classList.add('flex');
        document.body.style.overflow = 'hidden';
      }
    }, 500);
  };

  btnYes.addEventListener('click', handleYes);

  // Manejo robusto del botón NO (compatible con Brave Android, touch y clic)
  const handleNoInteraction = (e) => {
    if (e) {
      e.preventDefault();
      e.stopPropagation();
    }

    // Vibración háptica en móviles si está soportado
    if (navigator.vibrate) {
      try { navigator.vibrate(40); } catch(err) {}
    }

    noClickCount++;
    const isMobile = window.innerWidth < 640;

    if (noClickCount === 1) {
      // Primer salto travieso (desplazamiento contenido para no salirse de pantalla en móviles)
      const xOffset = isMobile ? 32 : 65;
      const yOffset = isMobile ? -18 : -26;

      btnNo.classList.add('playful-shake');
      btnNo.style.transform = `translate(${xOffset}px, ${yOffset}px)`;
      btnNo.innerHTML = '<span>¿Seguro? Piénsalo dos veces 😉</span>';
      
      if (feedbackMsg) {
        feedbackMsg.textContent = '👀 ¡Ey! Ese botón tiene reflejos propios...';
        feedbackMsg.classList.remove('hidden');
      }

      setTimeout(() => btnNo.classList.remove('playful-shake'), 400);

    } else if (noClickCount === 2) {
      // Segundo salto travieso
      const xOffset = isMobile ? -30 : -65;
      const yOffset = isMobile ? 18 : 24;

      btnNo.classList.add('playful-shake');
      btnNo.style.transform = `translate(${xOffset}px, ${yOffset}px)`;
      btnNo.innerHTML = '<span>¡Una charla de 10 min no se le niega a nadie! ☕</span>';
      
      if (feedbackMsg) {
        feedbackMsg.textContent = '⚡ Ya se movió dos veces como me pediste... ¿seguro no querés un café virtual?';
        feedbackMsg.classList.remove('hidden');
      }

      setTimeout(() => btnNo.classList.remove('playful-shake'), 400);

    } else {
      // Tercer intento: se rinde con gracia y ofrece LinkedIn
      btnNo.style.transform = 'translate(0, 0)';
      btnNo.innerHTML = '<span>Bueno, ¡al menos charlemos en LinkedIn! 🤝</span>';
      btnNo.classList.remove('bg-rose-950/40', 'text-rose-400', 'border-rose-900/50');
      btnNo.classList.add('bg-blue-900/40', 'text-blue-300', 'border-blue-700/50');
      
      window.open('https://www.linkedin.com/in/león-munitz', '_blank');
      showToast('¡Gracias por visitar mi perfil! Te espero en LinkedIn.');
    }
  };

  // Escuchar tanto click como pointerdown / touchend para garantizar funcionamiento en Brave Android
  btnNo.addEventListener('click', handleNoInteraction);
}

function triggerCelebration() {
  if (typeof confetti === 'function') {
    confetti({
      particleCount: 90,
      spread: 65,
      origin: { y: 0.6 }
    });
    setTimeout(() => {
      confetti({
        particleCount: 45,
        angle: 60,
        spread: 50,
        origin: { x: 0 }
      });
      confetti({
        particleCount: 45,
        angle: 120,
        spread: 50,
        origin: { x: 1 }
      });
    }, 250);
  }
}

/* ==========================================================================
   5. COPIAR DATOS DE CONTACTO CON NOTIFICACIÓN TOAST
   ========================================================================== */
function initCopyButtons() {
  const copyButtons = document.querySelectorAll('.btn-copy');

  copyButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const textToCopy = btn.getAttribute('data-copy-text');
      const label = btn.getAttribute('data-copy-label') || 'Dato';

      if (navigator.clipboard && textToCopy) {
        navigator.clipboard.writeText(textToCopy).then(() => {
          showToast(`✓ ${label} copiado: ${textToCopy}`);
        }).catch(() => {
          fallbackCopy(textToCopy, label);
        });
      } else {
        fallbackCopy(textToCopy, label);
      }
    });
  });
}

function fallbackCopy(text, label) {
  const textArea = document.createElement('textarea');
  textArea.value = text;
  document.body.appendChild(textArea);
  textArea.select();
  try {
    document.execCommand('copy');
    showToast(`✓ ${label} copiado: ${text}`);
  } catch (err) {
    showToast(`Error al copiar: ${text}`);
  }
  document.body.removeChild(textArea);
}

function showToast(message) {
  let toast = document.getElementById('global-toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'global-toast';
    toast.className = 'fixed bottom-6 right-6 z-50 px-4 py-3 rounded-xl bg-slate-900 text-white shadow-2xl border border-slate-700 text-sm font-medium transition-all duration-300 transform translate-y-12 opacity-0 pointer-events-none flex items-center gap-2';
    document.body.appendChild(toast);
  }

  toast.innerHTML = `<span>${message}</span>`;
  toast.classList.remove('translate-y-12', 'opacity-0', 'pointer-events-none');
  toast.classList.add('translate-y-0', 'opacity-100');

  setTimeout(() => {
    toast.classList.remove('translate-y-0', 'opacity-100');
    toast.classList.add('translate-y-12', 'opacity-0', 'pointer-events-none');
  }, 3200);
}
