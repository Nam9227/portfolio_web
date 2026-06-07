// Add smooth reveal animations on scroll
document.addEventListener('DOMContentLoaded', () => {
    // Reveal elements
    const revealElements = document.querySelectorAll('.project-card, .summary-block, .section-title');
    
    // Initial state
    revealElements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
    });

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });

    revealElements.forEach(el => {
        revealObserver.observe(el);
    });

    // Parallax effect for blobs
    window.addEventListener('scroll', () => {
        const scrolled = window.scrollY;
        const blob1 = document.querySelector('.blob-1');
        const blob2 = document.querySelector('.blob-2');
        
        if (blob1 && blob2) {
            blob1.style.transform = `translateY(${scrolled * 0.2}px)`;
            blob2.style.transform = `translateY(${scrolled * -0.1}px)`;
        }
    });
});
